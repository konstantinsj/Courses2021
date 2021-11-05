import pprint
import time

import json
import requests
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

start_time = time.time()
browser = webdriver.Chrome('chromedriver')  # path to chromedriver
next_page = "browse__pagination__next"
scroll_into_view = "arguments[0].scrollIntoView();"
card_list = 'browse-card-list__data'
cards = "browse-card-wrapper"
next_page_disabled = "browse__pagination__border.browse__pagination__border--disabled"

browser.get('https://inch.lv/browse?type=apartment&districts=R%C4%ABga&subdistricts=Centrs%2CVecr%C4%ABga&page=1&priceTo=70000&dealType=sale');  #
time.sleep(1)
price = list()

while True:
    time.sleep(1)
    elements = browser.find_element(By.CLASS_NAME, card_list)
    ads = elements.find_elements(By.CLASS_NAME, cards)
    print(f"Got {len(ads)} results on this page")
    for i in range(len(ads)):  # iterating elements on page
        price.append(ads[i].find_element(By.CLASS_NAME, "browse-card__cost__price").text)
        browser.execute_script(scroll_into_view, ads[i])
    try:
        browser.find_element(By.CLASS_NAME, next_page_disabled).is_displayed()
        print("No next page!")
        break
    except (TimeoutException, WebDriverException):
        try:
            browser.find_element(By.CLASS_NAME, next_page).click()
        except (TimeoutException, WebDriverException):
            break
    time.sleep(3)

print(f"Total results: {len(price)}")
print(price)
print("--- %s seconds ---" % (time.time() - start_time))

browser.quit()
