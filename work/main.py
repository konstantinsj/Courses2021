import time
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

start_time = time.time()
browser = webdriver.Chrome('chromedriver')  # path to chromedriver
wait = WebDriverWait(browser, 10)
next_page = By.CLASS_NAME, "browse__pagination__next"
scroll_into_view = "arguments[0].scrollIntoView();"

card_list = By.CLASS_NAME, 'browse-card-list__data'
cards = By.CLASS_NAME, "browse-card-wrapper"
cost_price = By.CLASS_NAME, "browse-card__cost__price"
next_page_disabled = By.CLASS_NAME, "browse__pagination__border.browse__pagination__border--disabled"

url = 'https://inch.lv/browse?type='
type = 'apartment'
price_to = 'priceTo=70000'
deal_type = '&dealType=sale'
districts = '&districts=R%C4%ABga'
subdistricts = '&subdistricts=Centrs%2CVecr%C4%ABga&'

browser.get((url + (type + ((districts + (subdistricts)) + price_to + deal_type))));
result = list()

while True:
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'browse-card-list__data')))
    elements = browser.find_element(*card_list)
    ads = elements.find_elements(*cards)
    print(f"Got {len(ads)} results on this page")
    for i in range(len(ads)):  # iterating elements on page
        result.append(ads[i].find_element(*cost_price).text)
        browser.execute_script(scroll_into_view, ads[i])
    try:
        browser.find_element(*next_page_disabled).is_displayed()
        print("No next page!")
        break
    except (TimeoutException, WebDriverException):
        try:
            browser.find_element(*next_page).click()
        except (TimeoutException, WebDriverException):
            break

print(f"Total results: {len(result)}")
print(result)
print("--- %s seconds ---" % (time.time() - start_time))

browser.quit()
