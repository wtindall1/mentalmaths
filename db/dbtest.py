from database import HighScore, session
from datetime import datetime

#initialise session object
newSession = session()

new_record = HighScore(id=3,
                       created_at=datetime.now(),
                       user_name = 'Will',
                       level='easy',
                       score='10')

newSession.add(new_record)
newSession.commit()

from_db_scores = newSession.query(HighScore).all()

for i in from_db_scores:
    print(i)
