from http.client import PROXY_AUTHENTICATION_REQUIRED
from bs4 import BeautifulSoup
from requests import get
from sys import argv
import pandas as pd
link = "https://www.imdb.com/title/tt7366338/ratings?demo=imdb_users&ref_=ttrt_fltr_imdb_users"


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

all=pd.read_html(link)
male=pd.read_html(link_to_male(link))
female = pd.read_html(link_to_female(link))
print(all[0]["Votes"])
print(male[0]["Votes"])
print(female[0]["Votes"])

