import csv
from http.client import PROXY_AUTHENTICATION_REQUIRED
from bs4 import BeautifulSoup
from requests import get
from sys import argv
import sqlite3
connection_object=sqlite3.connect('filmy.db')
cursor=connection_object.cursor()
cursor.execute("DROP TABLE IF EXISTS MOVIES")
cursor.execute("CREATE TABLE MOVIES (name VARCHAR(255),movie_id VARCHAR(255),year real,genre VARCHAR(255),rating VARCHAR(255),length real)")
URL = "https://www.imdb.com/list/ls000634294/?sort=num_votes,asc&st_dt=&mode=detail&page=1"
page = get(URL)
with open('movies.txt', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['adas', 'piesek'])
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
    # if year[0]!='(':
    #     year=[int(s) for s in year.split() if s.isdigit()]
    # else:
    #     year=year[3:]
    genre=genre.strip()
    print(name, "-", movie_id, "-", year, "-",
        genre, "-", certificate, "-", runtime,"-")
    cursor.execute(f"INSERT INTO MOVIES values('{name}','{movie_id}','{year}','{genre}','{certificate}','{runtime}')")
    print("-----------------")
connection_object.commit()