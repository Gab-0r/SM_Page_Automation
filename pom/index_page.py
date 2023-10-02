import time

from utilities.browser_interactions import BrowserInteractions
from pom.locators.index_page_locators import IndexLocators as locators

def element_to_locator(option: str) -> tuple:
    locatorsDict ={
        'contact us': locators.CONTACT_US_OPTION,
        'menu button': locators.NAV_BUTTON
    }
    return locatorsDict[option]

class IndexPage():
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions

    def to_sm_page(self, url: str):
        self.browser_interactions.open_page(url)

    def is_index_visible(self):
        time.sleep(1)
        return self.browser_interactions.element_is_visible(locators.NAV_BUTTON)

    def click_element(self, element):
        time.sleep(1)
        return self.browser_interactions.click_element(element_to_locator(element))

