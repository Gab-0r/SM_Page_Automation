import time

from behave import step
from pom.contact_us_page import ContactUsPage
from dotenv import load_dotenv
import os

load_dotenv()


@step("the user has accessed to contact us page")
def contact_us_page_is_displayed(context):
    context.contact_us_page = ContactUsPage(context.browser_interactions)
    assert context.contact_us_page.is_contact_us_visible(), "contact us page is not displayed"


@step("the user enter correct information to form")
def input_correct_info(context):
    context.contact_us_page = ContactUsPage(context.browser_interactions)
    assert context.contact_us_page.fill_correct_info()
    time.sleep(10)