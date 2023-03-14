from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from datetime import datetime

Base = declarative_base()


class HighScore(Base):
    __tablename__ = "high_score"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    user_name = Column(String)
    level = Column(String)
    score = Column(Integer)

    def __repr__(self):
        return f"HighScore(id={self.id}, created_at={self.created_at}, userName={self.user_name} level={self.level}, score={self.score})"
    
    def return_data(self):
        return f"HighScore(id={self.id}, created_at={self.created_at}, userName={self.user_name} level={self.level}, score={self.score})"


class DBManager:

    def __init__(self):
        self.engine = create_engine("sqlite+pysqlite:///mental_maths_scores.db", echo=True, future=True)
        self.session = sessionmaker(bind=self.engine)

    def save_score(self, user_name, level, score):

        #initialise session object
        newSession = self.session()

        #set newest id - valueerror if no records in table
        from_db_ids = newSession.query(HighScore.id).all()
        try:
            new_id = max(from_db_ids)[0] + 1
        except: 
            new_id = 2


        new_record = HighScore(id=new_id,
                       created_at=datetime.now(),
                       user_name=user_name,
                       level=level,
                       score=score)

        newSession.add(new_record)
        newSession.commit()

        return new_record.return_data()
    
    def get_scores(self):

        #initialise session object
        newSession = self.session()

        #get highest score and username for each level
        from_db_scores = newSession.query(HighScore.level, 
                                          HighScore.user_name, 
                                          func.max(HighScore.score)).group_by(HighScore.level).all()
        
        #return dict of scores
        high_scores = {}

        for item in from_db_scores:
            high_scores[item[0]] = {
                'userName': item[1],
                'score': item[2]
            }
        return high_scores
    
# manager = DBManager()
# print(manager.get_scores())


