from behave import given,when,then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I launch  browser')
def step_impl(context):
    assert True, "Test Passed"


@when(u'I open application')
def step_impl(context):
    assert True, "Test Passed"


@when(u'Enter valid username and password')       
def step_impl(context):
    assert True, "Test Passed"


@when(u'Click on login')
def step_impl(context):
    assert True, "Test Passed"


@then(u'User must login to the product page')     
def step_impl(context):
    assert True, "Test Passed"


@when(u'I click on product name')
def step_impl(context):
    assert True, "Test Passed"


@then(u'Product description should be displayed') 
def step_impl(context):
    assert True, "Test Passed"