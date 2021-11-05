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
            '=sale');  #
next_page = "browse__pagination__next"
scroll_into_view = "arguments[0].scrollIntoView();"
card_list = 'browse-card-list__data'
cards = "browse-card-wrapper"

time.sleep(1)
elements = browser.find_element(By.CLASS_NAME, card_list)
ads = elements.find_elements(By.CLASS_NAME, cards)
price = list()
for i in range(len(ads)):   #iterating elements on page
    price.append(ads[i].find_element(By.CLASS_NAME, "browse-card__cost__price").text)
    browser.execute_script(scroll_into_view, ads[i])
if browser.find_element(By.CLASS_NAME, next_page).is_displayed():
    browser.find_element(By.CLASS_NAME, next_page).click()

print(price)
print("--- %s seconds ---" % (time.time() - start_time))

browser.quit()
