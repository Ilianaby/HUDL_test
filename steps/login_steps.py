# login_steps.py
from behave import given, when, then
from pages.login_page import LoginPage
from utils.common_utils import read_config


# Step Definitions

@given(u'I navigate to the login page')
def step_given_navigate_to_login_page(context):
    context.login_page = LoginPage()
    assert context.login_page.navigate_to_login_page(), "Login link not found"
    context.login_page.click(context.login_page.login_link)


@when(u'I submit valid credentials')
def step_when_submit_valid_credentials(context):
    email, password = read_config("email", "password")
    context.login_page.submit_creds(email, password)


@then(u'I should be logged in successfully')
def step_then_see_successful_login_indicator(context):
    assert context.login_page.is_login_successful(), "Login failed"


@when(u'I submit invalid credentials')
def step_when_submit_invalid_credentials(context):
    email, password = read_config("email", "wrong_password")
    context.login_page.submit_creds(email, password)


@when(u'I submit empty/missing credentials')
def step_when_submit_invalid_credentials(context):
    email, password = "", ""
    context.login_page.submit_creds(email, password)


@then(u'I should see the error message')
def step_then_see_error_message(context):
    assert context.login_page.get_error_message(), "Error message not found by XPATH"


@then(u'I should be able to logout')
def step_then_be_able_to_logout(context):
    context.login_page.find_logout()


@when(u'I click "Log Out"')
def step_then_be_able_to_logout(context):
    assert context.login_page.click_logout(), "Logout failed"


@then(u'I should not be logged in')
def step_then_not_logged_in(context):
    context.login_page.check_not_logged_in()


@then(u'I should stay on the login page')
def step_then_stay_on_login_page(context):
    assert context.login_page.check_element_by_id("logIn"), "Mandatory element not found"

@then(u'I should be redirected to the Home page')
def step_then_redirected_to_home_page(context):
    assert context.login_page.check_element_by_id("homepage_hero-button"), "Mandatory element not found"


@then(u'I should close the session')
def step_then_close_session(context):
    context.login_page.close_session()
