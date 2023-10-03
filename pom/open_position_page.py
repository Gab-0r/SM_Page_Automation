from utilities.browser_interactions import BrowserInteractions
from pom.locators.open_position_page_locators import OpenPositionLocators as locators
import os
from dotenv import load_dotenv

class OpenPositionPage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions

    def is_open_position_page_visible(self, position):
        element = self.browser_interactions.get_element_visible(locators.POSITION_PAGE_TITLE)
        if position == element.text:
            return True
        else:
            return False

    def fill_apply_form(self):
        load_dotenv()
        info_to_submit = [
            (os.getenv("NAME_OK"), locators.FULL_NAME_FIELD),
            (os.getenv("EMAIL_OK"), locators.EMAIL_FIELD),
            (os.getenv("PHONE_OK"), locators.PHONE_FIELD),
            (os.getenv("CITY_COUNTRY"), locators.CITY_COUNTRY_FIELD),
            (os.getenv("LINKED_IN"), locators.LINKEDIN_FIELD),
            (os.getenv("ABOUT_YOU"), locators.ABOUT_YOU_FIELD)
        ]

        for element in info_to_submit:
            info, field = element
            self.browser_interactions.input_text(field, info)
        return True

    def attach_file(self):
        file = os.getcwd() + os.getenv("CV_FILE")
        print(file)
        return self.browser_interactions.attach_file(
            file, locators.FILE_TO_ATTACH_FIELD
        )