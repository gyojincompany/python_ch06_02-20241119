from selenium import webdriver
import time

wd = webdriver.Chrome()
wd.get("http://www.naver.com")

time.sleep(10)
