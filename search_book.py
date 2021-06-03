import requests
from bs4 import BeautifulSoup


def get_category(soup):
    categorys = soup.findAll("li")
    category = categorys[2].text
    categoryReplace = category.replace("\n", "")
    return categoryReplace


def get_reviewRating(soup):
    p = soup.find("div", {"class": "col-sm-6 product_main"}).find(
        "p", class_="star-rating"
    )
    rating = str(p["class"])
    star = rating[15:-1]
    starRating = eval(star)
    return starRating


def get_description(soup):
    div = soup.find("div", class_="sub-header")
    p = div.find_next_sibling()
    return p.text


def get_imageUrl(soup):
    image = soup.find("div", {"class": "item active"}).find("img")
    image_url = image["src"]
    imageUrlClean = image_url.replace("../../", "http://books.toscrape.com/")
    return imageUrlClean


def scrapBook(url):
    URL = url
    livre = requests.get(URL,timeout=10)

    if livre.ok:
        soup = BeautifulSoup(livre.content, "html.parser")
        # Title
        titre = soup.find("div", {"class": "col-sm-6 product_main"}).find("h1")
        # description
        description = get_description(soup)
        # review rating
        reviewRating = get_reviewRating(soup)
        # Upc, price tax including, price taxe excluding,Type , Tax, nb available, stock
        tds = soup.findAll("td")
        # category
        category = get_category(soup)
        # img
        image_url = get_imageUrl(soup)
        # tableau
        book = {}
        book["product_page_url"] = URL
        book["universal_ product_code"] = tds[0].text
        book["title"] = titre.text
        book["price_including_tax"] = tds[3].text
        book["price_excluding_tax"] = tds[2].text
        book["number_available"] = tds[5].text
        book["product_description"] = description
        book["category"] = category
        book["review_rating"] = reviewRating
        book["image_url"] = image_url
        book["Tax"] = tds[4].text
        return book


#print(scrapBook("http://books.toscrape.com/catalogue/in-her-wake_980/index.html"))
