import time

from behave import step
from pom.index_page import IndexPage
from dotenv import load_dotenv
import os

load_dotenv()


@step("the user has accessed to sm website")
def go_to_sm(context):
    sm_page = IndexPage(context.browser_interactions)
    sm_page.to_sm_page(os.getenv("INDEX_URL"))


@step("the index page is displayed")
def index_page_is_displayed(context):
    time.sleep(3)
    context.index_page = IndexPage(context.browser_interactions)
    assert context.index_page.is_index_visible(), "index is not displayed"


@step("click {element}")
def click_element(context, element):
    context.index_page = IndexPage(context.browser_interactions)
    assert context.index_page.click_element(element), "element not found"
