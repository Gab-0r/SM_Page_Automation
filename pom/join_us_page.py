import time

from utilities.browser_interactions import BrowserInteractions
from pom.locators.join_us_locators_locators import JoinUsLocators as locators

def open_position_at(position: str):
    op_position_dict = {
    }
    return op_position_dict[position]



class JoinUsPage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions

    def is_join_us_visible(self):
        return self.browser_interactions.element_is_visible(locators.JOIN_US_DIV)

    def search_position(self, position: str):
        self.browser_interactions.input_text(locators.SEARCH_FIELD, position)
        self.browser_interactions.click_element_js(locators.SEARCH_FIELD_BUTTON)
        time.sleep(2)
        search_result = self.browser_interactions.get_element_visible(locators.SEARCH_RESULTS)
        if position in search_result.text:
            return self.browser_interactions.click_element_js(locators.SEARCH_RESULTS)
        else:
            return False