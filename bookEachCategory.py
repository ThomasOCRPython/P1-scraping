import requests
from bs4 import BeautifulSoup
from pathlib import Path
import csv
import re


import searchBook 
import searchCategory as cat




def categoryName(url):
    
    a=url.replace('http://books.toscrape.com/catalogue/category/books/','')
    b=re.sub(r'[0-9]+', '',a)
    name=b.replace('_/index.html','')
    return(name)

def searchImage(books,folderImage):
    for image in books:
        picture=image['image_url']
        page=requests.get(picture)
        filename=picture.split('/')[-1]
        filepicture=Path(folderImage,filename)
        with open(filepicture, 'wb') as f:
            f.write(page.content)

def searchBookCategory(url):
    livreUrl=[]
    books=[]

    #Clean Url
    refs=cat.categoryUrl(url)
    for ref in refs:
        replaceUrl=ref.replace('/../../../','/catalogue/')
        livreUrl.append(replaceUrl)

    #Livre par Url
    for livre in livreUrl: 
        book=searchBook.scrapBook(livre)    
        books.append(book)
        
    
    #Creation chemin,dossiers et fichiers
    category=categoryName(url)
    folderCategory=Path('./data/',category)
    folderCategory.mkdir(exist_ok=True)
    folderImage=Path(folderCategory,'image')
    folderImage.mkdir(exist_ok=True)
    fileCategory=Path(folderCategory,category+'.csv')

    #partie image
    
    searchImage(books,folderImage)
    
    #partie csv  
    with open(fileCategory,'w',newline='') as f:
        
        fieldnames=books[0].keys()#['product_page_url','universal_ product_code','title','price_including_tax','price_excluding_tax','number_available','product_description','category','review_rating','image_url','Tax']
        print(books[0].keys())
        writer =csv.DictWriter(f,delimiter=";",fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)
        
        
        
        
        
        
        

    

searchBookCategory('http://books.toscrape.com/catalogue/category/books/romance_8/index.html')

