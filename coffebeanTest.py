import requests
from bs4 import BeautifulSoup

coffeeHtml = requests.get("https://www.coffeebeankorea.com/store/store.asp")
coffeeSoup = BeautifulSoup(coffeeHtml.text,"html.parser")
print(coffeeSoup.prettify())
