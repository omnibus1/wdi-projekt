from http.client import PROXY_AUTHENTICATION_REQUIRED
from bs4 import BeautifulSoup
from requests import get
from sys import argv
URL = "https://www.imdb.com/list/ls000634294/?sort=num_votes,asc&st_dt=&mode=detail&page=1"
page = get(URL)
bs = BeautifulSoup(page.content, 'html.parser')
for offer in bs.find_all('div', class_="lister-item mode-detail"):
    name = offer.find('h3', class_="lister-item-header")
    link = name.find('a')
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
    print(link.get_text(), link['href'], year.get_text(
    ), genre, certificate, runtime)
    print("-----------------")
