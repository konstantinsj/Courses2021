from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from work.locators import Inch

browser = webdriver.Chrome('chromedriver')  # path to chromedriver
wait = WebDriverWait(browser, 10)
scroll_into_view = "arguments[0].scrollIntoView();"


class InchLv(object):
    def get_data(url='https://inch.lv/browse?type=',
                 type='apartment',
                 price_to='priceTo=70000',
                 deal_type='&dealType=sale',
                 districts='&districts=R%C4%ABga',
                 subdistricts='&subdistricts=Centrs%2CVecr%C4%ABga&'):

        browser.get((url + (type + ((districts + (subdistricts)) + price_to + deal_type))));
        result = list()
        while True:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'browse-card-list__data')))
            elements = browser.find_element(*Inch.CARD_LIST)
            ads = elements.find_elements(*Inch.CARDS)
            print(f"Got {len(ads)} results on this page")
            for i in range(len(ads)):  # iterating elements on page
                result.append([ads[i].find_element(*Inch.COST_PRICE).text, ads[i].find_element(*Inch.ADDRESS).text])
                browser.execute_script(scroll_into_view, ads[i])  # need to scroll otherwise no result
            try:
                browser.find_element(*Inch.NEXT_PAGE_DISABLED).is_displayed()
                print("No next page!")
                break
            except (TimeoutException, WebDriverException):
                try:
                    browser.find_element(*Inch.NEXT_PAGE).click()
                except (TimeoutException, WebDriverException):
                    break

        print(f"Total results: {len(result)}")
        browser.quit()
        return result
