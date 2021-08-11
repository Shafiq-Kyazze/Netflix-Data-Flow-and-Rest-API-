"""MOdule where queries can be made on the database using SQLAlchemy Object Relational Mapper"""

from database import engine
from sqlalchemy.orm import sessionmaker
from models import NETFLIX

Session = sessionmaker(bind=engine)   #COnnecting
s= Session()

#Example of a query fetching all the rows from the table constructed
records = s.query(NETFLIX).all()
for record in records:
    print(record.__dict__)