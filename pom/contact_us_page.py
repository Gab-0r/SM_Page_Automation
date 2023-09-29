import os

from utilities.browser_interactions import BrowserInteractions
from pom.locators.contact_us_locators import ContactUsLocators as locators
from dotenv import load_dotenv


def field_to_locator(option: str) -> tuple:
    locators_dict = {
        "name": locators.FULLNAME_FIELD,
        "email": locators.EMAIL_FIELD,
        "company": locators.COMPANY_FIELD,
        "phone": locators.PHONE_FIELD,
        "help": locators.HELP_FIELD
    }
    return locators_dict[option]


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
        return self.browser_interactions.click_element_js(locators.TERMS_CHECKBOX)

    def click_submit(self):
        return self.browser_interactions.click_element_js(locators.SUBMIT_BUTTON)

    def is_form_submitted(self):
        return self.browser_interactions.element_is_visible(locators.SUCCESSFULLY_SUBMITTED)

    def enter_info_in_field(self, value, field):
        self.browser_interactions.clear_text(field_to_locator(field))
        return self.browser_interactions.input_text(field_to_locator(field), value)




