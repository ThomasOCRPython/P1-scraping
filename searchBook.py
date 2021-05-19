import requests
from bs4 import BeautifulSoup

def get_category(soup):

    categorys=soup.findAll('li')
    category=categorys[2].text
    categoryReplace=category.replace('\n','')
    return categoryReplace

def get_review_rating(url):
    URL=url
    livre= requests.get(URL)

    if livre.ok: 
        soup= BeautifulSoup(livre.text,"html.parser")
        #p=soup.find('div',{'class':'col-sm-6 product_main'}).find('p').find_next().find_next().find_next()
        p=soup.find('div',{'class':'col-sm-6 product_main'}).find("p",class_="star-rating")
        rating=str(p["class"])
        starRating=rating[15:-1]
        print ("coucou: "+ starRating)



def scrapBook(url):
    
    URL=url
    livre= requests.get(URL)

    if livre.ok: 
        soup= BeautifulSoup(livre.text,"html.parser")
        #Title
        titre= soup.find('div',{'class':'col-sm-6 product_main'}).find('h1')

        #Description
        #productDescription=soup.findAll('div',{'class':'product_description'}).find_next_sibling("p")
        #print(productDescription)
        ###############################################################################

        #Upc, price tax including, price taxe excluding,Type , Tax, nb available, stock
        tds=soup.findAll('td')

        #img
        image=soup.find('div',{'class':'item active'}).find('img')
        image_url=image['src']

        #review_rating
        ###############################################################################

        book={}
        book['product_page_url']=URL
        book['universal_ product_code']=tds[0].text
        book['title']=titre.text
        book['price_including_tax']=tds[3].text
        book['price_excluding_tax']=tds[2].text
        book['number_available']=tds[5].text
        #book['product_description']=productDescription
        book['category']= get_category(soup)
        #book['review_rating']=image_url
        book['image_url']=image_url
        book['Tax']=tds[4].text

        print(book)

#scrapBook("http://books.toscrape.com/catalogue/security_925/index.html")
get_review_rating("http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")

     
    
