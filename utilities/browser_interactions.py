import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_locator(raw_locator: tuple) -> tuple:
    strategy, selector = raw_locator
    strategies = {"ID": By.ID, "XPATH": By.XPATH, "CSS": By.CSS_SELECTOR}
    return strategies[strategy], selector


class BrowserInteractions:
    def __init__(self, driver: Chrome, time_out: int):
        self._driver = driver
        self.time_out = time_out

    def open_page(self, url: str):
        self._driver.get(url)

    def click_element(self, raw_locator: tuple):

        element = WebDriverWait(self._driver, self.time_out).until(
            EC.element_to_be_clickable(get_locator(raw_locator))
        )
        element.click()


    def click_element_js(self, raw_locator: tuple) -> bool:
        try:
            element = WebDriverWait(self._driver, self.time_out).until(
                EC.presence_of_element_located(get_locator(raw_locator))
            )
        except:
            return False
        else:
            self._driver.execute_script("arguments[0].click()", element)
            return True

    def input_text(self, raw_locator: tuple, text: str) -> bool:
        try:
            element = WebDriverWait(self._driver, self.time_out).until(EC.visibility_of_element_located(
                get_locator(raw_locator)
            ))
        except:
            return False
        else:
            element.send_keys(text)
            return True

    def element_is_visible(self, raw_locator: tuple) -> bool:
        try:
            WebDriverWait(self._driver, self.time_out).until(
                EC.visibility_of_element_located(get_locator(raw_locator))
            )
        except:
            return False
        else:
            return True

    def get_elements(self, raw_locator: tuple) -> list[WebElement]:
        try:
            WebDriverWait(self._driver, self.time_out).until(
                EC.presence_of_all_elements_located(get_locator(raw_locator))
            )
        except:
            return []
        else:
            return self._driver.find_elements(*get_locator(raw_locator))

    def get_element(self, raw_locator: tuple) -> WebElement:
        try:
            WebDriverWait(self._driver, self.time_out).until(
                EC.presence_of_element_located(get_locator(raw_locator))
            )
        except:
            return None
        else:
            return self._driver.find_element(*get_locator(raw_locator))

    def clear_text(self, raw_locator: tuple):
        try:
            WebDriverWait(self._driver, self.time_out).until(
                EC.presence_of_element_located(get_locator(raw_locator))
            )
        except:
            return False
        else:
            return self._driver.find_element(*get_locator(raw_locator)).clear()
            return True

    def get_element_visible(self, raw_locator: tuple) -> WebElement:
        try:
            WebDriverWait(self._driver, self.time_out).until(
                EC.visibility_of_element_located(get_locator(raw_locator))
            )
        except:
            return None
        else:
            return self._driver.find_element(*get_locator(raw_locator))