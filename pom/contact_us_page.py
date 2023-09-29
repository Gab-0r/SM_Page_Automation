import os

from utilities.browser_interactions import BrowserInteractions
from pom.locators.contact_us_locators import ContactUsLocators as locators
from dotenv import load_dotenv


def element_to_locator(option: str) -> tuple:
    locatorsDict = {
    }
    return locatorsDict[option]


class ContactUsPage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions

    def is_contact_us_visible(self):
        return self.browser_interactions.element_is_visible(locators.FORM)

    def fill_correct_info(self):
        load_dotenv()
        info_to_submit = [
            (os.getenv("NAME_OK"), locators.FULLNAME_FIELD),
            (os.getenv("EMAIL_OK"), locators.EMAIL_FIELD),
            (os.getenv("COMPANY_OK"), locators.COMPANY_FIELD),
            (os.getenv("PHONE_OK"), locators.PHONE_FIELD),
            (os.getenv("HELP_OK"), locators.HELP_FIELD)
        ]

        for element in info_to_submit:
            (info, field) = element
            self.browser_interactions.input_text(field, info)

        return True

    def mark_checkbox(self):
        return self.browser_interactions.click_checkbox(locators.TERMS_CHECKBOX)



