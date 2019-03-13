#Parse HTML content on the page and use this info
#Course: https://www.udemy.com/the-complete-python-web-course-learn-by-building-8-apps/
import requests
from bs4 import BeautifulSoup

#  <p class="price price--large">£89.00</p>

request=requests.get("https://www.johnlewis.com/house-by-john-lewis-whistler-dining-chair/p3901192")
content=request.content  #request content of html page
soup = BeautifulSoup(content, "html.parser") # parse the page with BS
element = soup.find("p", {"class":"price--large"}) #find a tag <p> with class price
string_price=element.text.strip() #get text price from the tag £89.00
price_without_symbol=string_price[1:] #delete £ 89.00
price=float(price_without_symbol) #convert into number

if price<100:
    print ("Buy a chair!")
    print ("The current price is: £{}.". format(price))
else:
    print ("You don't have enough money, loser")
