from behave import given,when,then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('launch chrome browser')
def launch_browser(context):
    context.driver=webdriver.Chrome()
    
@when('open sauce demo homepage')
def open_homepage(context):
    context.driver.get("https://www.saucedemo.com/")
      
@then('verify that the logo present on page')
def verify_logo(context):
    status = context.driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]").is_displayed()
    assert status is True
    
@then('close browser')   
def close_browser(context):
    context.driver.close()
