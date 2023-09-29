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
    assert context.contact_us_page.fill_correct_info(),"fields were not filled"


@step("mark the checkbox to aceppt terms and conditions")
def check_terms_and_conditions(context):
    context.contact_us_page = ContactUsPage(context.browser_interactions)
    assert context.contact_us_page.mark_checkbox(), "checkbox not found"


@step("click submit button")
def contact_us_click_submit(context):
    context.contact_us_page = ContactUsPage(context.browser_interactions)
    assert context.contact_us_page.click_submit(), "button not found"


@step("the form is submit correctly")
def form_correctly_submit(context):
    context.contact_us_page = ContactUsPage(context.browser_interactions)
    assert context.contact_us_page.is_form_submitted(), "form wwas not submitted"
    time.sleep(2)