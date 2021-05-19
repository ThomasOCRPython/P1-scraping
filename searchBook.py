import requests
from bs4 import BeautifulSoup

def get_category(soup):

    categorys=soup.findAll('li')
    category=categorys[2].text
    categoryReplace=category.replace('\n','')
    return categoryReplace

def get_reviewRating(soup):
  
    #p=soup.find('div',{'class':'col-sm-6 product_main'}).find('p').find_next().find_next().find_next()
    p= soup.find('div',{'class':'col-sm-6 product_main'}).find("p",class_="star-rating")
    rating=str(p["class"])
    star=rating[15:-1]
    starRating=eval(star)
    return starRating

def get_description(url):
    URL=url
    livre= requests.get(URL)

    if livre.ok: 
        soup= BeautifulSoup(livre.text,"html.parser")

        paragraphs=soup.findAll('p')

        p=paragraphs[3].encode('utf-8')
        
        print(p)    



def scrapBook(url):

    
    URL=url
    livre= requests.get(URL)

    if livre.ok: 
        soup= BeautifulSoup(livre.text,"html.parser")
        #Title
        titre= soup.find('div',{'class':'col-sm-6 product_main'}).find('h1')

        #Description
        #productDescription=soup.find('div',class_='product_description').find_next().find_next().find_next()
        # paragraphs=soup.findAll('p')
        # linkp=[]
        # for paragraph in paragraphs:
        #     p=paragraph.text
        #     linkp.append(p)
        

        
        
        
        ###############################################################################

        #Upc, price tax including, price taxe excluding,Type , Tax, nb available, stock
        tds=soup.findAll('td')

        #img
        image=soup.find('div',{'class':'item active'}).find('img')
        image_url=image['src']

    

        book={}
        book['product_page_url']=URL
        book['universal_ product_code']=tds[0].text
        book['title']=titre.text
        book['price_including_tax']=tds[3].text
        book['price_excluding_tax']=tds[2].text
        book['number_available']=tds[5].text
        #book['product_description']=productDescription
        book['category']= get_category(soup)
        book['review_rating']= get_reviewRating(soup)
        book['image_url']=image_url
        book['Tax']=tds[4].text

        #print(book)

#scrapBook("http://books.toscrape.com/catalogue/security_925/index.html")
get_description("http://books.toscrape.com/catalogue/security_925/index.html")


     
    
