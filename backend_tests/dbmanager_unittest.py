import unittest
import sys
from sqlalchemy import func, create_engine
from sqlalchemy.orm import sessionmaker 

sys.path.append('C:/Users/wtind/projects/mental_maths_project/mentalmaths')
from db.db_manager import HighScore, DBManager

class TestDatabaseManager(unittest.TestCase):

    def test_score_saved(self):

        #query starting number of records
        engine = create_engine("sqlite+pysqlite:///mental_maths_scores.db", echo=True, future=True)
        session = sessionmaker(bind=engine)
        testSession = session()
        count_rows_start = testSession.query(func.count(HighScore.id)).all()[0][0]
        
        manager = DBManager()
        manager.save_score('Will', 'easy', '5')

        #query to check score was saved
        count_rows_end = testSession.query(func.count(HighScore.id)).all()[0][0]

        self.assertTrue(count_rows_end - count_rows_start == 1)

if __name__ == '__main__':
    unittest.main()
        
        

        
