import requests
from bs4 import BeautifulSoup
import time


import book_each_category


def get_url_category(soup):
    url_link_category = []

    urls = soup.find("ul", {"class": "nav nav-list"}).findAll("li")
    for url in urls:
        a = url.find("a")
        url_category = a["href"]
        if url_category == "catalogue/category/books_1/index.html":
            continue
        else:
            url_link_category.append("http://books.toscrape.com/" + url_category)
    return url_link_category


def get_all_category(url):
    page = requests.get(url)
    if page.ok:
        soup = BeautifulSoup(page.content, "html.parser")
        urls_links = get_url_category(soup)

        for url_link in urls_links:
            book_each_category.get_book_each_ategory(url_link)
            # print(url_link)

get_all_category("http://books.toscrape.com/index.html")
