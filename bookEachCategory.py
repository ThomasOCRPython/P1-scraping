import requests
from bs4 import BeautifulSoup

import searchBook 
import searchCategory as cat



def searchBookCategory(url):
    livreUrl=[]
    books=[]
    refs=cat.categoryUrl(url)
    for ref in refs:
        replaceUrl=ref.replace('/../../../','/catalogue/')
        livreUrl.append(replaceUrl)
    
    for livre in livreUrl: 
        book=searchBook.scrapBook(livre)   
        books.append(book)
    return books 
    # return livreUrl   

    
    
print(searchBookCategory("http://books.toscrape.com/catalogue/category/books/christian_43/index.html"))    