import time
import json
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('chromedriver')      #path to chromedriver

browser.get('https://www.ss.com/lv/transport/cars/bmw/');   #
car_list = browser.find_elements(By.CLASS_NAME, "d1")
car = list()
for i in range(len(car_list)):
    car.append(car_list[i].text)

with open("cars.json", mode="w", encoding="utf-8") as write_file:  # saving data to json
    json.dump(car, write_file, indent=4, ensure_ascii=False)

browser.quit()
