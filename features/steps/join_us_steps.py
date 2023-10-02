import time
from behave import step
from pom.join_us_page import JoinUsPage
from dotenv import load_dotenv
import os

load_dotenv()


@step("the user has accessed to join us page")
def join_us_visible(context):
    context.join_us_page = JoinUsPage(context.browser_interactions)
    assert context.join_us_page.is_join_us_visible(), "join us page is not displayed"


@step("the user search the {position} open position")
def search_position(context, position):
    context.join_us_page = JoinUsPage(context.browser_interactions)
    assert context.join_us_page.search_position(position), "search result was not expected"
