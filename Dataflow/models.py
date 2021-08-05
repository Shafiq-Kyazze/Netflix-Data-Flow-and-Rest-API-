from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Date,Float

#Base to construct table
Base = declarative_base()

class NETFLIX(Base):
    """Model for Netflix table"""

    __tablename__ = "netflix"
    id = Column(Integer, primary_key=True, autoincrement=True)
    Title = Column(String)
    Genre = Column(String)
    Premiere = Column(Date)
    Run_time = Column(Integer)
    IMDB_Score = Column(Float)
    Language = Column(String)


