import pprint
import time

import json
import requests
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
start_time = time.time()
browser = webdriver.Chrome('chromedriver')  # path to chromedriver

browser.get('https://inch.lv/browse?type=apartment&districts=R%C4%ABga&subdistricts=Centrs%2CVecr%C4%ABga&dealType'
            '=sale&page=1');  #

time.sleep(1)
elements = browser.find_element(By.CLASS_NAME, 'browse-card-list__data')
ads = elements.find_elements(By.CLASS_NAME, "browse-card-wrapper")
price = list()
for i in range(len(ads)):   #iterating elements on page
    price.append(ads[i].find_element(By.CLASS_NAME, "browse-card__cost__price").text)
    browser.execute_script("arguments[0].scrollIntoView();", ads[i])
if browser.find_element(By.CLASS_NAME, "browse__pagination__next").is_displayed():
    browser.find_element(By.CLASS_NAME, "browse__pagination__next").click()
print(price)
print("--- %s seconds ---" % (time.time() - start_time))

browser.quit()
