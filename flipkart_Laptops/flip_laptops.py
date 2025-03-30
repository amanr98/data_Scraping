from bs4 import BeautifulSoup as bs
import requests as rq

def crapData(page):
     qSqoup = bs(page,"html.parser")
     
     f_name = qSqoup.select('a.CGtC98')
     # print(f_name)
     list1 = []
     for i in f_name:

          image = i.select_one('img')
          image_url = image['src']

          name = i.select_one('div.KzDlHZ')

          rate_number = i.select_one('div.XQDdHH')
     
          ratings = i.select_one('span.Wphh3N > span > span').text.replace('\xa0', '')

          reviews = i.select('span.Wphh3N > span > span ')[2].text.replace('\xa0', '')

          confi_list=[]
          confi = i.select('ul.G4BRas > li')
          for c in confi:
               confi_list.append(
                    c.text
               )
          

          offer_price_element = i.select_one('div.Nx9bqj._4b5DiR') 
          offer_price_text = offer_price_element.text if offer_price_element else 'Offer price not available'

          actual_price_element = i.select_one('div.yRaY8j.ZYYwLA')
          actual_price_text = actual_price_element.text if actual_price_element else 'Actual price not available'


          list1.append({
               'image_url': image_url,
               'name': name.text,
               'rate_number': rate_number.text,
               'rating' : ratings,
               'reviews' : reviews,
               'configuration':confi_list,
               'offer_price':offer_price_text,
               'actual_price':actual_price_text
          })
          confi_list.clear

     print(list1)
    