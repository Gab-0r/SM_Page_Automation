from utilities.browser_interactions import BrowserInteractions
from pom.locators.open_position_page_locators import OpenPositionLocators as locators


class OpenPositionPage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions

    def is_open_position_page_visible(self, position):
        element = self.browser_interactions.get_element_visible(locators.POSITION_PAGE_TITLE)
        if position == element.text:
            return True
        else:
            return False