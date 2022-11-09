import sqlite3
from http.client import PROXY_AUTHENTICATION_REQUIRED
from bs4 import BeautifulSoup
from requests import get
from sys import argv
import pandas as pd
link = "https://www.imdb.com/title/tt7366338/ratings?demo=imdb_users&ref_=ttrt_fltr_imdb_users"
connection_object = sqlite3.connect('filmy.db')
cursor = connection_object.cursor()
cursor.execute("DROP TABLE IF EXISTS ALLVOTES")
cursor.execute("DROP TABLE IF EXISTS ALLMALE")
cursor.execute("DROP TABLE IF EXISTS ALLFEMALE")
cursor.execute('CREATE TABLE ALLVOTES (movie_id VARCHAR(255),TEN real,NINE real,EIGHT real,SEVEN real,SIX real,FIVE real,FOUR real,THREE real,TWO real,ONE real,FOREIGN KEY(movie_id) REFERENCES MOVIES(movie_id))')
cursor.execute('CREATE TABLE ALLMALE (movie_id VARCHAR(255),TEN real,NINE real,EIGHT real,SEVEN real,SIX real,FIVE real,FOUR real,THREE real,TWO real,ONE real,FOREIGN KEY(movie_id) REFERENCES MOVIES(movie_id))')
cursor.execute('CREATE TABLE ALLFEMALE (movie_id VARCHAR(255),TEN real,NINE real,EIGHT real,SEVEN real,SIX real,FIVE real,FOUR real,THREE real,TWO real,ONE real,FOREIGN KEY(movie_id) REFERENCES MOVIES(movie_id))')
cursor.execute('select movie_id from MOVIES')
x=cursor.fetchall()
for value in x:
    print(value[0])
# def link_to_male(link):
#     x = link.split('=')
#     x[1] = "males&ref_=ttrt_fltr_males"
#     y = "=".join(x)
#     return y
# def link_to_female(link):
    
#     x = link.split('=')
    
#     x[1] = "females&ref_=ttrt_fltr_females"
#     y = "=".join(x)
#     return y

# all=pd.read_html(link)
# male=pd.read_html(link_to_male(link))
# female = pd.read_html(link_to_female(link))
# print(all[0]["Votes"])
# print(male[0]["Votes"])
# print(female[0]["Votes"])
connection_object.commit()
