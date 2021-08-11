from sqlalchemy.orm import sessionmaker
from models import Base,NETFLIX
from config import DATABASE_URI
from sqlalchemy import create_engine

import pandas as pd

#Connecting SQL alchemy to the database
engine = create_engine(DATABASE_URI, echo=True)

#Binding SQL alchemy ORM  database
Session = sessionmaker(bind=engine)
s = Session()

#Constructing table in database
Base.metadata.create_all(bind=engine)
s.commit()  #Pushing changes to the psycopg2 and sqlalchemy


file_path = r"/media/shafiq/New Volume/Dropbox/Data Science Projects/Netflix-API-Project/Netflix project/Netflix-Data-Flow-and-Rest-API-/Dataset/NetflixOriginals.csv"
df = pd.read_csv(file_path, encoding='ISO-8859-1')  #Encoding the contents so that they can be read by pandas

from datetime import datetime

"""Function that converts different datetime formats to the default python datetime format"""
def date_convertor(time):
    if "," in str(time): #if comma after day convert time this way
        new_date = datetime.strptime(time, "%B %d, %Y").date()
    elif "." in str(time):  #if fullstop after day convert time this way
        new_date = datetime.strptime(time, "%B %d. %Y").date()
    return new_date

#Applying the function to a dataframe
df['Premiere'] = df['Premiere'].apply(lambda x: date_convertor(x))

rows = list(map(tuple,df.to_numpy())) #list of all the rows in the dataset

"""Inserting the rows in the dataset into the database"""
for row in rows:
    """Inserting each row from dataset to database"""
    insertions = NETFLIX(
        Title=row[0], Genre=row[1], Premiere= row[2],
        Run_time= row[3],IMDB_Score = row[4], Language = row[5]
    )
    s.add(insertions) #adding changes to  psycopg2 and sqlalchemy

#Pushing rows to database
s.commit()
s.close() #CLosing the session