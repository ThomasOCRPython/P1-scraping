import requests
from bs4 import BeautifulSoup


def get_category(soup):
    categorys = soup.findAll("li")
    category = categorys[2].text
    category_replace = category.replace("\n", "")
    return category_replace


def get_review_rating(soup):
    p = soup.find("div", {"class": "col-sm-6 product_main"}).find(
        "p", class_="star-rating"
    )
    rating = str(p["class"])
    star = rating[15:-1]
    star_rating = eval(star)
    return star_rating


def get_description(soup):
    div = soup.find("div", class_="sub-header")
    p = div.find_next_sibling()
    return p.text


def get_image_url(soup):
    image = soup.find("div", {"class": "item active"}).find("img")
    image_url = image["src"]
    image_clean_url = image_url.replace("../../", "http://books.toscrape.com/")
    return image_clean_url


def get_book(url):
    URL = url
    livre = requests.get(URL)

    if livre.ok:
        soup = BeautifulSoup(livre.content, "html.parser")

        titre = soup.find("div", {"class": "col-sm-6 product_main"}).find("h1")
        description = get_description(soup)
        review_rating = get_review_rating(soup)
        tds = soup.findAll("td")
        category = get_category(soup)
        image_url = get_image_url(soup)

        book = {}
        book["product_page_url"] = URL
        book["universal_ product_code"] = tds[0].text
        book["title"] = titre.text
        book["price_including_tax"] = tds[3].text
        book["price_excluding_tax"] = tds[2].text
        book["number_available"] = tds[5].text
        book["product_description"] = description
        book["category"] = category
        book["review_rating"] = review_rating
        book["image_url"] = image_url
        book["Tax"] = tds[4].text
        return book


#print(get_book("http://books.toscrape.com/catalogue/in-her-wake_980/index.html"))
