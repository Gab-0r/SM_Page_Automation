from utilities.browser_interactions import BrowserInteractions
from pom.locators.contact_us_locators import ContactUsLocators as locators

def element_to_locator(option: str) -> tuple:
    locatorsDict = {
    }
    return locatorsDict[option]

class ContactUsPage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions

    def is_contact_us_visible(self):
        return self.browser_interactions.element_is_visible(locators.FORM)


