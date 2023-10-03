from behave import step
from pom.open_position_page import OpenPositionPage
import time


@step("the user has accessed to {position} position page")
def position_page_visible(context, position):
    context.open_position_page = OpenPositionPage(context.browser_interactions)
    assert context.open_position_page.is_open_position_page_visible(position)


@step("the user enter correct information to apply")
def complete_apply_form(context):
    context.open_position_page = OpenPositionPage(context.browser_interactions)
    assert context.open_position_page.fill_apply_form()
    time.sleep(10)