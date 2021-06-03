import requests
from bs4 import BeautifulSoup
from pathlib import Path
import csv
import re

import search_book
import search_category as cat


def categoryName(url):
    a = url.replace("http://books.toscrape.com/catalogue/category/books/", "")
    b = re.sub(r"[0-9]+", "", a)
    name = b.replace("_/index.html", "")
    return name


def searchImage(books, folderImage):
    for image in books:
        picture = image["image_url"]
        page = requests.get(picture)
        filename = picture.split("/")[-1]
        filepicture = Path(folderImage, filename)
        with open(filepicture, "wb") as f:
            f.write(page.content)


def searchBookCategory(url):
    livreUrl = []
    books = []

    # Clean Url
    refs = cat.categoryUrl(url)
    for ref in refs:
        replaceUrl = ref.replace("/../../../", "/catalogue/")
        livreUrl.append(replaceUrl)
    # Livre par Url
    for livre in livreUrl:
        book = search_book.scrapBook(livre)
        books.append(book)        
    # Creation chemin,dossiers et fichiers
    category = categoryName(url)
    folderCategory = Path("./data/", category)
    folderCategory.mkdir(exist_ok=True)
    folderImage = Path(folderCategory, "image")
    folderImage.mkdir(exist_ok=True)
    fileCategory = Path(folderCategory, category + ".csv")

    searchImage(books, folderImage)

    with open(fileCategory, "w", newline="") as f:
        fieldnames = books[0].keys()  
        #print(books[0].keys())
        writer = csv.DictWriter(f, delimiter=";", fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)


searchBookCategory('http://books.toscrape.com/catalogue/category/books/mystery_3/index.html')
