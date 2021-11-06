from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from work.locators import Locators


class InchLv(object):
    def __init__(self):
        self.browser = webdriver.Chrome('chromedriver')  # path to chromedriver
        self.wait = WebDriverWait(self.browser, 10)
        self.scroll_into_view = "arguments[0].scrollIntoView();"

    def get_data(self, url='https://inch.lv/browse?type=',
                 type='apartment',
                 price_to='priceTo=70000',
                 deal_type='&dealType=sale',
                 districts='&districts=R%C4%ABga',
                 subdistricts='&subdistricts=Centrs%2CVecr%C4%ABga&'):

        self.browser.get((url + (type + ((districts + (subdistricts)) + price_to + deal_type))));
        result = list()
        while True:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'browse-card-list__data')))
            elements = self.browser.find_element(*Locators.CARD_LIST)
            ads = elements.find_elements(*Locators.CARDS)
            print(f"Got {len(ads)} results on this page")
            for i in range(len(ads)):  # iterating elements on page
                result.append([ads[i].find_element(*Locators.COST_PRICE).text, ads[i].find_element(*Locators.ADDRESS).text])
                self.browser.execute_script(self.scroll_into_view, ads[i])  # need to scroll otherwise no result
            try:
                self.browser.find_element(*Locators.NEXT_PAGE_DISABLED).is_displayed()
                print("No next page!")
                break
            except (TimeoutException, WebDriverException):
                try:
                    self.browser.find_element(*Locators.NEXT_PAGE).click()
                except (TimeoutException, WebDriverException):
                    break

        print(f"Total results: {len(result)}")
        self.browser.quit()
        return result
