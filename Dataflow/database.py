from sqlalchemy.orm import sessionmaker
from models import Base,NETFLIX
from config import DATABASE_URI
from sqlalchemy import create_engine

import pandas as pd

#Creating engine and connecting it to database
engine = create_engine(DATABASE_URI, echo=True)

#Binding session to engine/database
Session = sessionmaker(bind=engine)
s = Session()

#Constructing table in database
Base.metadata.create_all(bind=engine)
s.commit()


file_path = r"/home/shafiq/Dropbox/Data Science Projects/Netflix project/Netflix-Data-Flow-and-Rest-API-/Dataset/NetflixOriginals.csv"
df = pd.read_csv(file_path, encoding='ISO-8859-1')

from datetime import datetime
"""Function that converts different datetime formarts to the default python datetime format"""
def date_convertor(time):
    if "," in str(time): #if comma after day convert time this way
        new_date = datetime.strptime(time, "%B %d, %Y").date()
    elif "." in str(time):  #if fullstop after day convert time this way
        new_date = datetime.strptime(time, "%B %d. %Y").date()
    return new_date

#Applying the function to a dataframe
df['Premiere'] = df['Premiere'].apply(lambda x: date_convertor(x))

rows = list(map(tuple,df.to_numpy())) # list of all the rows in the dataset

"""Inserting the rows in the dataset into the database"""
for row in rows:
    """Inserting each row from dataset to database"""
    insertions = NETFLIX(
        Title=row[0], Genre=row[1], Premiere= row[2],
        Run_time= row[3],IMDB_Score = row[4], Language = row[5]
    )
    s.add(insertions) #adding rows

#Pushing rows to database
s.commit()
s.close()