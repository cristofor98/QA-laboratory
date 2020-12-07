from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from seleniumwire import webdriver 
import unittest,time

def check_error_page(text):
    if text == "Page Not Found":
        return True
    return False

@when('Populate review form with username "{username}" and email "{email}" and message {message}')
def step_impl(context,username,email,message):
    context.username_field = context.driver.find_element_by_css_selector("input[type=text]:nth-child(1)")
    context.username_field.send_keys(username)
    time.sleep(10)
    context.email_field = context.driver.find_element_by_css_selector("input[type=\"email\"]:nth-child(2)")
    context.email_field.send_keys(email)
    time.sleep(10)
    context.message_field = context.driver.find_element_by_css_selector("div.add-review textarea")
    context.message_field.send_keys(message)
    time.sleep(10)

@when('Click on SEND button')
def step_impl(context):
    context.send_button = context.driver.find_element_by_css_selector("input[type=submit]:nth-child(4)")
    context.send_button.click()

@then('A warning message "{string}" appears')
def step_impl(context):
    context.username_field = context.driver.find_element_by_css_selector("input[type=text]:nth-child(1)")
    context.email_field = context.driver.find_element_by_css_selector("input[type=email]:nth-child(2)")
    context.message_field = context.driver.find_element_by_css_selector("textarea")
    actual_username_field = context.username_field.get_attribute("validationMessage")
    actual_email_field = context.email_field.get_attribute("validationMessage")
    actual_message_field = context.message_field.get_attribute("validationMessage")
    if actual_username_field != None and actual_email_field != None and actual_message_field != None:
        assert True, "Test Passed"
        context.driver.close()
    else:
        assert False, "Test Failed"
        context.driver.close()


@when('Populate review form with "<username>" "<email>" "<message>"')
def step_impl(context,username,email,message):
    context.username_field = context.driver.find_element_by_css_selector("input[type=text]:nth-child(1)")
    context.username_field.send_keys(username)
    context.email_field = context.driver.find_element_by_css_selector("input[type=email]:nth-child(2)")
    context.email_field.send_keys(email)
    context.message_field = context.driver.find_element_by_css_selector("textarea")
    context.message_field.send_keys(message)
      
    
@then('The review is posted')
def step_impl(context):
    try:
        text = context.driver.find_element_by_css_selector("div.header > h1").text
    except:
        assert True, "Test Passed"
        context.driver.close()
    if check_error_page(text):
        assert False, "Test Failed"
        context.driver.close()
    