from database import engine
from sqlalchemy.orm import sessionmaker
from models import NETFLIX

Session = sessionmaker(bind=engine)
s= Session()

records = s.query(NETFLIX).all()
for record in records:
    print(record.__dict__)