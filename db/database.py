from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite+pysqlite:///mental_maths_scores.db", echo=True, future=True)
session = sessionmaker(bind=engine)
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
    
#create schema
Base.metadata.create_all(engine)
