from behave import step
from pom.contact_us_page import ContactUsPage
from dotenv import load_dotenv
import os

load_dotenv()

@step("the user has accessed to sm website")
def go_to_sm(context):
    sm_page = ContactUsPage(context.browser_interactions)
    sm_page.to_sm_page(os.getenv("INDEX_URL"))


@step("the index page is displayed")
def index_page_is_displayed(context):
    context.index_page = ContactUsPage(context.browser_interactions)
    assert context.index_page.is_index_visible(), "index is not displayed"
