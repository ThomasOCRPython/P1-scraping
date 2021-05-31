import requests
from bs4 import BeautifulSoup

import book_each_category as b

def get_url_category(url):
    linkUrlCategory=[]
    
    URL=url
    page= requests.get(URL)
    if page.ok:
        soup= BeautifulSoup(page.text,"html.parser")
        urls=soup.find('ul',{'class':'nav nav-list'}).findAll('li')
        for url in urls:
            a=url.find('a')
            urlcategory=a['href']
            if (b=='catalogue/category/books_1/index.html'):
                continue
            else:
                linkUrlCategory.append("http://books.toscrape.com/"+ urlcategory) 
    return linkUrlCategory
    
 

def get_all_category(url):
    linksUrls=get_url_category(url)
    for linkUrl in linksUrls:
        b.searchBookCategory(linkUrl)
    
#get_all_category('http://books.toscrape.com/index.html')