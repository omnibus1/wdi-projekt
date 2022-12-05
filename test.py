import requests
from bs4 import BeautifulSoup

def get_page_count(url):
    page=requests.get(url)
    bs = BeautifulSoup(page.content, 'html.parser')
    range=bs.find("span",class_="pagination-range")
    text=range.get_text().strip()
    # text="1 - 100 of 1,300"
    text=text.replace(",","")
    text=text.split("of")
    movie_count=int(text[1].strip())
    if(movie_count%100==0):
        page_count=movie_count//100
    else:
        page_count=movie_count//100+1
    return page_count
def get_list_links(url):
    links=[]
    page_count=get_page_count(url)
    base_url=url+"&sort=list_order,asc&st_dt=&mode=detail&page=1"
    for i in range(1,page_count+1):
        url=list(base_url)
        url[-1]=str(i)
        links.append("".join(url))

    return links

