from utilities.browser_interactions import BrowserInteractions
from pom.locators.contact_us_locators import ContactUsLocators as locators


class ContactUsPage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions

    def to_sm_page(self, url: str):
        print(url)
        self.browser_interactions.open_page(url)

    def is_index_visible(self):
        return self.browser_interactions.element_is_visible(locators.NAV_BUTTON)

