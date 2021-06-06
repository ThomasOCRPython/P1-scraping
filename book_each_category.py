import requests
from bs4 import BeautifulSoup
from pathlib import Path
import csv
import re

import search_book
import search_category as cat


def get_category_name(url):
    url_category_name = url.replace(
        "http://books.toscrape.com/catalogue/category/books/", ""
    )
    category_name = re.sub(r"[0-9]+", "", url_category_name)
    name = category_name.replace("_/index.html", "")
    return name


def search_image(books, folder_image):
    for image in books:
        picture = image["image_url"]
        page = requests.get(picture)
        file_name = picture.split("/")[-1]
        file_picture = Path(folder_image, file_name)
        with open(file_picture, "wb") as f:
            f.write(page.content)


def get_book_each_ategory(url):
    urls_books = []
    books = []

    clean_urls_categorys = cat.get_url_category(url)
    for clean_url_category in clean_urls_categorys:
        replace_url = clean_url_category.replace("/../../../", "/catalogue/")
        urls_books.append(replace_url)
        # print(replace_url)

    for url_book in urls_books:
        book = search_book.get_book(url_book)
        books.append(book)

    category = get_category_name(url)
    folder_category = Path("./data/", category)
    folder_category.mkdir(exist_ok=True, parents=True)
    folder_image = Path(folder_category, "image")
    folder_image.mkdir(exist_ok=True)
    file_category = Path(folder_category, category + ".csv")

    search_image(books, folder_image)

    with open(file_category, "w", encoding="utf-8", newline="") as f:
        fieldnames = books[0].keys()
        writer = csv.DictWriter(f, delimiter=";", fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)


#get_book_each_ategory('http://books.toscrape.com/catalogue/category/books/mystery_3/index.html')
