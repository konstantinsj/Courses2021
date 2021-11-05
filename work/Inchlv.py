from selenium.webdriver.common.by import By


class Inchlv:
    next_page = By.CLASS_NAME, "browse__pagination__next"
    scroll_into_view = "arguments[0].scrollIntoView();"
    card_list = By.CLASS_NAME, 'browse-card-list__data'
    cards = By.CLASS_NAME, "browse-card-wrapper"
    cost_price = By.CLASS_NAME, "browse-card__cost__price"
    next_page_disabled = By.CLASS_NAME, "browse__pagination__border.browse__pagination__border--disabled"