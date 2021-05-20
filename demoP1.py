import requests
from bs4 import BeautifulSoup
from pathlib import Path 


'''links=[]

for i in range(1,3):
    URL="http://books.toscrape.com/catalogue/category/books/childrens_11/page-"+str(i)+".html"
    r= requests.get(URL)
    if r.ok:
        print ('page :'+str(i))
        soup= BeautifulSoup(r.text,"html.parser")
        articles= soup.findAll('article')
        for article in articles:
            a= article.find('a')
            link= a['href']
            links.append("http://books.toscrape.com/"+ link)

print(len(links)) 

with open ('url.txt','w') as file:
    for link in links:
        file.write(link+'\n')
  
URL="http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
livre= requests.get(URL)
if livre.ok: 
    soup= BeautifulSoup(livre.text,"html.parser")
    titre= soup.find('div',{'class':'col-sm-6 product_main'}).find('h1')
    print('Titre : '+ titre.text)
    #priceIncludingTax= soup.find('div',{'class':'col-sm-6 product_main'}).find('p',{'class':'price_color'})
    link=[]
    ths=soup.findAll('th')
    tds=soup.findAll('td')
    for i,j in zip(ths,tds):
        print(i.text,': ',j.text)'''

#def book(url):
    
#     URL=url
#     livre= requests.get(URL)
#     if livre.ok: 
#         soup= BeautifulSoup(livre.text,"html.parser")
#         #Titre du livre
#         titre= soup.find('div',{'class':'col-sm-6 product_main'}).find('h1')

#         #Déscription du livre
#         #productDescription=soup.find('div',{'class':'sub-header'}).find_next_siblings("p")

#         #Upc, prix taxe incluse, prix taxe excluse,Type du produit, Taxe, nombre d'avis, stock
#         tds=soup.findAll('td')

#         #image
#         image=soup.find('div',{'class':'item active'}).find('img')
#         image_url=image['src']

#         #catégorie
#         categorys=soup.findAll('li')
#         category=categorys[2].text
#         categoryReplace=category.replace('\n','')
    
#         dicoBook={'product_page_url':URL,'title':titre.text,'universal_ product_code':tds[0].text,'Product Type':tds[1].text,'price_excluding_tax':tds[2].text,'price_including_tax':tds[3].text,'product_description':'productDescription','Tax':tds[4].text,'number_available':tds[5].text,'category':categoryReplace,'Number of reviews':tds[6].text,'image_url':image_url}    
#         print (dicoBook)
    
# book('http://books.toscrape.com/catalogue/security_925/index.html')
       
mypath=Path('./data/Christian') 
print(mypath.exists())






    