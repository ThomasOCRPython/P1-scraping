import requests
from bs4 import BeautifulSoup
from pathlib import Path
import csv


import searchBook 
import searchCategory as cat


mypath=Path('./data/Christian')

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
    #return books 
    # return livreUrl 
      
    with open('./data/Christian/Christian.csv','w',newline='') as f:
        # for book in books:
        #      f.write('{},{},{},{},{},{},{},{},{},{},{}\n'.format(book['product_page_url'],book['universal_ product_code'],book['title'],book['price_including_tax'],book['price_excluding_tax'],book['number_available'],book['product_description'],book['category'],book['review_rating'],book['image_url'],book['Tax'])) 
         fieldnames=['product_page_url','universal_ product_code','title','price_including_tax','price_excluding_tax','number_available','product_description','category','review_rating','image_url','Tax']

         writer = csv.DictWriter(f,delimiter=" ",fieldnames=fieldnames,restval='', extrasaction='ignore')
         writer.writeheader()
         writer.writerows(books)
        
        
        
        

    

searchBookCategory('http://books.toscrape.com/catalogue/category/books/christian_43/index.html')