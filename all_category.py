import requests
from bs4 import BeautifulSoup


import book_each_category


def get_url_category(soup):
    linkUrlCategory = []

    urls = soup.find("ul", {"class": "nav nav-list"}).findAll("li")
    for url in urls:
        a = url.find("a")
        urlcategory = a["href"]
        if urlcategory == "catalogue/category/books_1/index.html":
            continue
        else:
            linkUrlCategory.append("http://books.toscrape.com/" + urlcategory)
    return linkUrlCategory


def get_all_category(url):
    URL = url
    page = requests.get(URL)
    if page.ok:
        soup = BeautifulSoup(page.content, "html.parser")
        linksUrls = get_url_category(soup)
        for linkUrl in linksUrls:
            book_each_category.searchBookCategory(linkUrl)
            


get_all_category("http://books.toscrape.com/index.html")
