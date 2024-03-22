from behave import given,when,then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I launch chrome browser')
def step_impl(context):
    context.driver=webdriver.Chrome()

@when('I open sauce demo homepage')
def open_homepage(context):
    context.driver.get("https://www.saucedemo.com/")


@when('Enter username "{user}" and password "{pwd}"')
def login(context,user,pwd):
    context.driver.find_element(By.ID, "user-name").send_keys(user)
    context.driver.find_element(By.ID, "password").send_keys(pwd)
    
@when('Click on login button')
def click_loginbtn(context):
    context.driver.find_element(By.ID, "login-button").click()


@then('User must successfully login to the product page')
def products(context):
    try:
        page= context.driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/span").text
    except:
        context.driver.close()
        assert False, "Test Failed"
        
    if page == "Products" :
        context.driver.close()
        assert True, "Test passed"