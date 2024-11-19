import time
from selenium import webdriver
from bs4 import BeautifulSoup

wd = webdriver.Chrome()
resultList = []

wd.get("https://www.coffeebeankorea.com/store/store.asp")
time.sleep(1)
i = 1

try:
    wd.execute_script(f"storePop2('{261}')")
    time.sleep(3)
    coffeeHtml = wd.page_source

    coffeeSoup = BeautifulSoup(coffeeHtml, "html.parser")
    # print(coffeeSoup.prettify())
    store_name = coffeeSoup.select("div.store_txt > h2")
    print(store_name[0].text.strip())  # 대리점 명
    store_address = coffeeSoup.select("table.store_table > tbody > tr > td")
    print(store_address[2].text.strip())
    print(store_address[3].text.strip())

except:
    print(f"존재하지 않는 매장 고유 번호 : {i}")


