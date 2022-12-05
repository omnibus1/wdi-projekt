import csv
import sys
from http.client import PROXY_AUTHENTICATION_REQUIRED
from bs4 import BeautifulSoup
from requests import get
from sys import argv
from test import get_list_links
import requests
import sqlite3
connection_object=sqlite3.connect('filmy.db')
cursor=connection_object.cursor()
cursor.execute("DROP TABLE IF EXISTS MOVIES")
cursor.execute("DROP TABLE IF EXISTS GENRE")
cursor.execute("CREATE TABLE GENRE (movie_id VARCHAR(255),genre VARCHAR(255),FOREIGN KEY(movie_id) REFERENCES MOVIES(movie_id))")
cursor.execute("CREATE TABLE MOVIES (name VARCHAR(255),movie_id VARCHAR(255),year real,rating VARCHAR(255),length real)")
list_urls=["https://www.imdb.com/list/ls000634294/?ref_=rltls_1","https://www.imdb.com/list/ls070104965/?ref_=rltls_1","https://www.imdb.com/list/ls095146097/?ref_=rltls_4","https://www.imdb.com/list/ls003224162/?ref_=rltls_19"]

urls=[]
for list_url in list_urls:
   urls+=get_list_links(list_url)


headers = {"Accept-Language": "en-US,en;q=0.5"}




for url in urls:
    print(url)
    page = requests.get(url,headers=headers)
    bs = BeautifulSoup(page.content, 'html.parser')


    for offer in bs.find_all('div', class_="lister-item mode-detail"):
        name = offer.find('h3', class_="lister-item-header")
        movie_id = name.find('a')
        year = offer.find('span', class_="lister-item-year text-muted unbold")
        genre = offer.find('span', class_='genre')
        certificate = offer.find('span', class_='certificate')
        runtime = offer.find('span', class_='runtime')
        if genre is None:
            genre = "Null"
        else:
            genre = genre.get_text()
        if certificate is None:
            certificate = "Null"
        else:
            certificate = certificate.get_text()
        if runtime is None:
            runtime = "Null"
        else:
            runtime = runtime.get_text()
        year = year.get_text()

        name = movie_id.get_text()
        name=name.replace("'"," ")
        movie_id = movie_id['href'][7:-1]
        genre=genre[1:]
        runtime=runtime[:-4]
        one=year.find('1')
        two=year.find('2')
        print(year,one,two)
        if(one<two and one!=-1 or two==-1):
            year=year[one:one+4]
        if(two<one and two!=-1 or one==-1):
            year=year[two:two+4]

        genre=genre.strip()
        print(name, "-", movie_id, "-", year, "-",
            genre, "-", certificate, "-", runtime,"-")
        cursor.execute(f"SELECT movie_id from MOVIES where movie_id='{movie_id}'")
        x=cursor.fetchall()

        if(len(x)==0):
            for genre in genre.split(","):
                curr_genre=genre.strip()
                cursor.execute(f"INSERT INTO GENRE VALUES('{movie_id}','{curr_genre}')")


            cursor.execute(f"INSERT INTO MOVIES values('{name}','{movie_id}','{year}','{certificate}','{runtime}')")
        else:
            print("*****duplicate**********")
    print("-----------------")

connection_object.commit()