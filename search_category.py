import requests
from bs4 import BeautifulSoup
from math import *


def get_number_of_page(url):
    page = requests.get(url)
    if page.ok:
        soup = BeautifulSoup(page.text, "html.parser")
        nb_book = soup.find("form", {"class": "form-horizontal"}).find("strong").text
        if int(nb_book) > 20:
            resultat = ceil(int(nb_book) / 20)
        else:
            resultat = 1
    return resultat


def get_url_category(url):
    resultat = get_number_of_page(url)
    # print(resultat)
    links = []
    if resultat > 1:
        url1 = url.replace("index.html", "")
        for i in range(1, resultat + 1):
            URL = url1 + "page-" + str(i) + ".html"
            r = requests.get(URL)
            if r.ok:
                #print("page :" + str(i))
                soup = BeautifulSoup(r.text, "html.parser")
                articles = soup.findAll("article")
                for article in articles:
                    a = article.find("a")
                    link = a["href"]
                    links.append("http://books.toscrape.com/" + link)
    else:
        r = requests.get(url)
        if r.ok:
            soup = BeautifulSoup(r.text, "html.parser")
            articles = soup.findAll("article")
            for article in articles:
                a = article.find("a")
                link = a["href"]
                links.append("http://books.toscrape.com/" + link)
    # print(len(links))
    return links


# print(get_url_category('http://books.toscrape.com/catalogue/category/books/romance_8/index.html'))
