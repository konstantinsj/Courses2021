import pprint
import time
import json
import requests
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('chromedriver')  # path to chromedriver
browser.get('https://inch.lv/browse?type=apartment&districts=R%C4%ABga&subdistricts=Centrs%2CVecr%C4%ABga&dealType'
            '=sale&page=1');  #

elements = browser.find_element(By.CLASS_NAME, 'browse-card-list__data')
ads = elements.find_elements(By.CLASS_NAME, "browse-card-wrapper")
price = list()
# price = browser.find_element(By.CSS_SELECTOR, f'#cell0Browse').find_element(find_price).text

for i in range(len(ads)):
    price.append(ads[i].find_element(By.CLASS_NAME, "browse-card__cost__price").text)
    actions = ActionChains(browser)
    actions.move_to_element(ads[i]).perform()
# pprint.pprint(price,)
print(price)

browser.quit()
