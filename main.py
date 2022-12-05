import sqlite3
from http.client import PROXY_AUTHENTICATION_REQUIRED
from bs4 import BeautifulSoup
from requests import get
from sys import argv
import pandas as pd
import time
import datetime
start=datetime.datetime.now()
base_link = ["https://www.imdb.com/title/","movie_id","/ratings?demo=imdb_users&ref_=ttrt_fltr_imdb_users"]
connection_object = sqlite3.connect('filmy.db')
cursor = connection_object.cursor()
cursor.execute("DROP TABLE IF EXISTS ALLVOTES")
cursor.execute("DROP TABLE IF EXISTS ALLMALE")
cursor.execute("DROP TABLE IF EXISTS ALLFEMALE")
cursor.execute("DROP TABLE IF EXISTS AMALE19TO29")

cursor.execute("DROP TABLE IF EXISTS ALLUNDER18")
cursor.execute("DROP TABLE IF EXISTS MALEUNDER18")
cursor.execute("DROP TABLE IF EXISTS FEMALEUNDER18")

cursor.execute("DROP TABLE IF EXISTS ALL18TO29")
cursor.execute("DROP TABLE IF EXISTS MALE18TO29")
cursor.execute("DROP TABLE IF EXISTS FEMALE18TO29")

cursor.execute("DROP TABLE IF EXISTS ALL30TO44")
cursor.execute("DROP TABLE IF EXISTS MALE30TO44")
cursor.execute("DROP TABLE IF EXISTS FEMALE30TO44")

cursor.execute("DROP TABLE IF EXISTS ALL45PLUS")
cursor.execute("DROP TABLE IF EXISTS MALE45PLUS")
cursor.execute("DROP TABLE IF EXISTS FEMALE45PLUS")

cursor.execute('CREATE TABLE ALLVOTES (movie_id VARCHAR(255),TEN real,NINE real,EIGHT real,SEVEN real,SIX real,FIVE real,FOUR real,THREE real,TWO real,ONE real,FOREIGN KEY(movie_id) REFERENCES MOVIES(movie_id))')
cursor.execute('CREATE TABLE ALLMALE (movie_id VARCHAR(255),TEN real,NINE real,EIGHT real,SEVEN real,SIX real,FIVE real,FOUR real,THREE real,TWO real,ONE real,FOREIGN KEY(movie_id) REFERENCES MOVIES(movie_id))')
cursor.execute('CREATE TABLE ALLFEMALE (movie_id VARCHAR(255),TEN real,NINE real,EIGHT real,SEVEN real,SIX real,FIVE real,FOUR real,THREE real,TWO real,ONE real,FOREIGN KEY(movie_id) REFERENCES MOVIES(movie_id))')
cursor.execute('CREATE TABLE ALLUNDER18 (movie_id VARCHAR(255),TEN real,NINE real,EIGHT real,SEVEN real,SIX real,FIVE real,FOUR real,THREE real,TWO real,ONE real,FOREIGN KEY(movie_id) REFERENCES MOVIES(movie_id))')
cursor.execute('CREATE TABLE MALEUNDER18 (movie_id VARCHAR(255),TEN real,NINE real,EIGHT real,SEVEN real,SIX real,FIVE real,FOUR real,THREE real,TWO real,ONE real,FOREIGN KEY(movie_id) REFERENCES MOVIES(movie_id))')
cursor.execute('CREATE TABLE FEMALEUNDER18 (movie_id VARCHAR(255),TEN real,NINE real,EIGHT real,SEVEN real,SIX real,FIVE real,FOUR real,THREE real,TWO real,ONE real,FOREIGN KEY(movie_id) REFERENCES MOVIES(movie_id))')
cursor.execute('CREATE TABLE ALL18TO29 (movie_id VARCHAR(255),TEN real,NINE real,EIGHT real,SEVEN real,SIX real,FIVE real,FOUR real,THREE real,TWO real,ONE real,FOREIGN KEY(movie_id) REFERENCES MOVIES(movie_id))')
cursor.execute('CREATE TABLE MALE18TO29 (movie_id VARCHAR(255),TEN real,NINE real,EIGHT real,SEVEN real,SIX real,FIVE real,FOUR real,THREE real,TWO real,ONE real,FOREIGN KEY(movie_id) REFERENCES MOVIES(movie_id))')
cursor.execute('CREATE TABLE FEMALE18TO29 (movie_id VARCHAR(255),TEN real,NINE real,EIGHT real,SEVEN real,SIX real,FIVE real,FOUR real,THREE real,TWO real,ONE real,FOREIGN KEY(movie_id) REFERENCES MOVIES(movie_id))')
cursor.execute('CREATE TABLE ALL30TO44 (movie_id VARCHAR(255),TEN real,NINE real,EIGHT real,SEVEN real,SIX real,FIVE real,FOUR real,THREE real,TWO real,ONE real,FOREIGN KEY(movie_id) REFERENCES MOVIES(movie_id))')
cursor.execute('CREATE TABLE MALE30TO44 (movie_id VARCHAR(255),TEN real,NINE real,EIGHT real,SEVEN real,SIX real,FIVE real,FOUR real,THREE real,TWO real,ONE real,FOREIGN KEY(movie_id) REFERENCES MOVIES(movie_id))')
cursor.execute('CREATE TABLE FEMALE30TO44 (movie_id VARCHAR(255),TEN real,NINE real,EIGHT real,SEVEN real,SIX real,FIVE real,FOUR real,THREE real,TWO real,ONE real,FOREIGN KEY(movie_id) REFERENCES MOVIES(movie_id))')
cursor.execute('CREATE TABLE ALL45PLUS (movie_id VARCHAR(255),TEN real,NINE real,EIGHT real,SEVEN real,SIX real,FIVE real,FOUR real,THREE real,TWO real,ONE real,FOREIGN KEY(movie_id) REFERENCES MOVIES(movie_id))')
cursor.execute('CREATE TABLE MALE45PLUS (movie_id VARCHAR(255),TEN real,NINE real,EIGHT real,SEVEN real,SIX real,FIVE real,FOUR real,THREE real,TWO real,ONE real,FOREIGN KEY(movie_id) REFERENCES MOVIES(movie_id))')
cursor.execute('CREATE TABLE FEMALE45PLUS (movie_id VARCHAR(255),TEN real,NINE real,EIGHT real,SEVEN real,SIX real,FIVE real,FOUR real,THREE real,TWO real,ONE real,FOREIGN KEY(movie_id) REFERENCES MOVIES(movie_id))')
cursor.execute('select movie_id from MOVIES')
x=cursor.fetchall()


def link_to_male(link):
    x = link.split('=')
    x[1] = "males&ref_=ttrt_fltr_males"
    y = "=".join(x)
    return y
def link_to_female(link):
    
    x = link.split('=')
    
    x[1] = "females&ref_=ttrt_fltr_females"
    y = "=".join(x)
    return y
def link_to_18_29(link):
    x = link.split('=')
    
    x[1] = "aged_18_29&ref_=ttrt_fltr_aged_18_29"
    y = "=".join(x)
    return y

def link_to_18_29_male(link):
    x = link.split('=')
    
    x[1] = "males_aged_18_29&ref_=ttrt_fltr_males_aged_18_29"
    y = "=".join(x)
    return y
def link_to_18_29_female(link):
    x = link.split('=')
    
    x[1] = "females_aged_18_29&ref_=ttrt_fltr_females_aged_18_29"
    y = "=".join(x)
    return y
def link_to_under_18_all(link):
    x = link.split('=')
    
    x[1]="aged_under_18&ref_=ttrt_fltr_aged_under_18"
    y = "=".join(x)
    return y


def link_to_under_18_male(link):
    x = link.split('=')
    
    x[1]="males_aged_under_18&ref_=ttrt_fltr_males_aged_under_18"
    y = "=".join(x)
    return y


def link_to_under_18_female(link):
    x = link.split('=')
    
    x[1]="females_aged_under_18&ref_=ttrt_fltr_females_aged_under_18"
    y = "=".join(x)
    return y

def link_to_all_30_44(link):
    x = link.split('=')
    
    x[1]="aged_30_44&ref_=ttrt_fltr_aged_30_44"
    y = "=".join(x)
    return y

def link_to_male_30_44(link):
    x = link.split('=')
    
    x[1]="males_aged_30_44&ref_=ttrt_fltr_males_aged_30_44"
    y = "=".join(x)
    return y
    

def link_to_female_30_44(link):
    x = link.split('=')
    
    x[1]="females_aged_30_44&ref_=ttrt_fltr_females_aged_30_44"
    y = "=".join(x)
    return y

def link_to_all_45_plus(link):
    x = link.split('=')
    
    x[1]="aged_45_plus&ref_=ttrt_fltr_aged_45_plus"
    y = "=".join(x)
    return y

def link_to_male_45_plus(link):
    x = link.split('=')
    
    x[1]="males_aged_45_plus&ref_=ttrt_fltr_males_aged_45_plus"
    y = "=".join(x)
    return y

def link_to_female_45_plus(link):
    x = link.split('=')
    
    x[1]="females_aged_45_plus&ref_=ttrt_fltr_females_aged_45_plus"
    y = "=".join(x)
    return y
    
    

i=0
for value in x:
    link=base_link
    link[1]=value[0]

    movie_id=link[1]
    print(link[1])
    link="".join(link)
    print(link)
    all=pd.read_html(link)
    male=pd.read_html(link_to_male(link))
    female = pd.read_html(link_to_female(link))
    all_under_18=pd.read_html(link_to_under_18_all(link))
    male_under_18=pd.read_html(link_to_under_18_male(link))
    female_under_18=pd.read_html(link_to_under_18_female(link))
    all_18_29=pd.read_html(link_to_18_29(link))
    male_18_29=pd.read_html(link_to_18_29_male(link))
    female_18_29=pd.read_html(link_to_18_29_female(link))
    all_30_44=pd.read_html(link_to_all_30_44(link))
    male_30_44=pd.read_html(link_to_male_30_44(link))
    female_30_44=pd.read_html(link_to_female_30_44(link))
    all_45_plus=pd.read_html(link_to_all_45_plus(link))
    male_45_plus=pd.read_html(link_to_male_45_plus(link))
    female_45_plus=pd.read_html(link_to_female_45_plus(link))
    
    votes=all[0]["Votes"]
    cursor.execute(f"INSERT INTO ALLVOTES VALUES('{movie_id}','{votes[0]}','{votes[1]}','{votes[2]}','{votes[3]}','{votes[4]}','{votes[5]}','{votes[6]}','{votes[7]}','{votes[8]}','{votes[9]}')")
    votes=male[0]["Votes"]
    cursor.execute(f"INSERT INTO ALLMALE VALUES('{movie_id}','{votes[0]}','{votes[1]}','{votes[2]}','{votes[3]}','{votes[4]}','{votes[5]}','{votes[6]}','{votes[7]}','{votes[8]}','{votes[9]}')")
    votes=female[0]["Votes"]
    cursor.execute(f"INSERT INTO ALLFEMALE VALUES('{movie_id}','{votes[0]}','{votes[1]}','{votes[2]}','{votes[3]}','{votes[4]}','{votes[5]}','{votes[6]}','{votes[7]}','{votes[8]}','{votes[9]}')")
    

    votes=all_under_18[0]["Votes"]
    cursor.execute(f"INSERT INTO ALLUNDER18 VALUES('{movie_id}','{votes[0]}','{votes[1]}','{votes[2]}','{votes[3]}','{votes[4]}','{votes[5]}','{votes[6]}','{votes[7]}','{votes[8]}','{votes[9]}')")
    votes=male_under_18[0]["Votes"]
    cursor.execute(f"INSERT INTO MALEUNDER18 VALUES('{movie_id}','{votes[0]}','{votes[1]}','{votes[2]}','{votes[3]}','{votes[4]}','{votes[5]}','{votes[6]}','{votes[7]}','{votes[8]}','{votes[9]}')")
    votes=female_under_18[0]["Votes"]
    cursor.execute(f"INSERT INTO FEMALEUNDER18 VALUES('{movie_id}','{votes[0]}','{votes[1]}','{votes[2]}','{votes[3]}','{votes[4]}','{votes[5]}','{votes[6]}','{votes[7]}','{votes[8]}','{votes[9]}')")

    votes=all_18_29[0]["Votes"]
    cursor.execute(f"INSERT INTO ALL18TO29 VALUES('{movie_id}','{votes[0]}','{votes[1]}','{votes[2]}','{votes[3]}','{votes[4]}','{votes[5]}','{votes[6]}','{votes[7]}','{votes[8]}','{votes[9]}')")
    votes=male_18_29[0]["Votes"]
    cursor.execute(f"INSERT INTO MALE18TO29 VALUES('{movie_id}','{votes[0]}','{votes[1]}','{votes[2]}','{votes[3]}','{votes[4]}','{votes[5]}','{votes[6]}','{votes[7]}','{votes[8]}','{votes[9]}')")
    votes=female_18_29[0]["Votes"]
    cursor.execute(f"INSERT INTO FEMALE18TO29 VALUES('{movie_id}','{votes[0]}','{votes[1]}','{votes[2]}','{votes[3]}','{votes[4]}','{votes[5]}','{votes[6]}','{votes[7]}','{votes[8]}','{votes[9]}')")

    votes=all_30_44[0]["Votes"]
    cursor.execute(f"INSERT INTO ALL30TO44 VALUES('{movie_id}','{votes[0]}','{votes[1]}','{votes[2]}','{votes[3]}','{votes[4]}','{votes[5]}','{votes[6]}','{votes[7]}','{votes[8]}','{votes[9]}')")
    votes=male_30_44[0]["Votes"]
    cursor.execute(f"INSERT INTO MALE30TO44 VALUES('{movie_id}','{votes[0]}','{votes[1]}','{votes[2]}','{votes[3]}','{votes[4]}','{votes[5]}','{votes[6]}','{votes[7]}','{votes[8]}','{votes[9]}')")
    votes=female_30_44[0]["Votes"]
    cursor.execute(f"INSERT INTO FEMALE30TO44 VALUES('{movie_id}','{votes[0]}','{votes[1]}','{votes[2]}','{votes[3]}','{votes[4]}','{votes[5]}','{votes[6]}','{votes[7]}','{votes[8]}','{votes[9]}')")

    votes=all_45_plus[0]["Votes"]
    cursor.execute(f"INSERT INTO ALL45PLUS VALUES('{movie_id}','{votes[0]}','{votes[1]}','{votes[2]}','{votes[3]}','{votes[4]}','{votes[5]}','{votes[6]}','{votes[7]}','{votes[8]}','{votes[9]}')")
    votes=male_45_plus[0]["Votes"]
    cursor.execute(f"INSERT INTO MALE45PLUS VALUES('{movie_id}','{votes[0]}','{votes[1]}','{votes[2]}','{votes[3]}','{votes[4]}','{votes[5]}','{votes[6]}','{votes[7]}','{votes[8]}','{votes[9]}')")
    votes=female_45_plus[0]["Votes"]
    cursor.execute(f"INSERT INTO FEMALE45PLUS VALUES('{movie_id}','{votes[0]}','{votes[1]}','{votes[2]}','{votes[3]}','{votes[4]}','{votes[5]}','{votes[6]}','{votes[7]}','{votes[8]}','{votes[9]}')")
    
    i+=1
    break
    if(i%50==0):
        connection_object.commit()
        print("updated")
# #
# # print(all[0]["Votes"],all[0]["Votes"][0])
# # print(male[0]["Votes"])males_under_18
# # print(female[0]["Votes"])
connection_object.commit()
end=datetime.datetime.now()
print("It took ",end-start)