"""WHere the data models are housed"""
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

    # instantilising data model to ensure all the columns are filled in whening the POST method is called
    def __init__(self, Title, Genre, Premiere, Run_time, IMDB_Score, Language):
        self.Title = Title
        self.Genre = Genre
        self.Premiere = Premiere
        self.Run_time = Run_time
        self.IMDB_Score = IMDB_Score
        self.Language = Language

