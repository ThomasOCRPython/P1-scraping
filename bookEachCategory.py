import requests
from bs4 import BeautifulSoup
from pathlib import Path
import csv
import re


import searchBook 
import searchCategory as cat


mypath=Path('./data/Christian')

def categoryName(url):
    
    a=url.replace('http://books.toscrape.com/catalogue/category/books/','')
    b=re.sub(r'[0-9]+', '',a)
    name=b.replace('_/index.html','')
    return(name)


def searchBookCategory(url):a
    livreUrl=[]
    books=[]
    
    
    refs=cat.categoryUrl(url)
    for ref in refs:
        replaceUrl=ref.replace('/../../../','/catalogue/')
        livreUrl.append(replaceUrl)
    
    for livre in livreUrl: 
        book=searchBook.scrapBook(livre)
           
        books.append(book)
    #return books 
    # return livreUrl 
      
    with open('./data/Christian/Christian.csv','w',newline='') as f:
        
        fieldnames=books[0].keys()#['product_page_url','universal_ product_code','title','price_including_tax','price_excluding_tax','number_available','product_description','category','review_rating','image_url','Tax']
        print(books[0].keys())
        writer =csv.DictWriter(f,delimiter=";",fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)
        
        
        #for book in books:
            #print(book)
            #writer.writerows(book)
        
        
        
        

    

searchBookCategory('http://books.toscrape.com/catalogue/category/books/christian_43/index.html')
categoryNameUrl('http://books.toscrape.com/catalogue/category/books/young-adult_21/index.html')
