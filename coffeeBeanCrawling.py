import time
from selenium import webdriver
from bs4 import BeautifulSoup

wd = webdriver.Chrome()
resultList = []

for i in range(1, 5): # 대리점 자바스크립트 고유 번호 1~30
    wd.get("https://www.coffeebeankorea.com/store/store.asp")
    time.sleep(1)
    try:
        wd.execute_script(f"storePop2('{i}')")
        time.sleep(3)
        coffeeHtml = wd.page_source

        coffeeSoup = BeautifulSoup(coffeeHtml, "html.parser")
        # print(coffeeSoup.prettify())
        store_p = coffeeSoup.select("div.store_txt > p")
        print(store_p)

    except:
        print(f"존재하지 않는 매장 고유 번호 : {i}")
        continue

