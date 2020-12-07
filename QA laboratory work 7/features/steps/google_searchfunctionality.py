from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from seleniumwire import webdriver 
import unittest

old_url = None

@when('Populate URL box with "{url}"')
def step_impl(context,url):
  context.driver = webdriver.Chrome('/Users/tekwill/Downloads/chromedriver')
  context.driver.get(url)

@then('Redirects to google main page')
def step_impl(context):
  context.logo = context.driver.find_element_by_css_selector("#hplogo")
  if context.logo.is_displayed():
    assert True, "Test Passed"
    context.driver.close()
  else:
    assert False, "Test Failed"
    context.driver.close() 
  

@given('The google page is loaded')
def step_impl(context):
    context.driver = webdriver.Chrome('/Users/tekwill/Downloads/chromedriver')
    context.driver.get("https://www.google.co.in")


@when('Populate search box with "{data}"')
def step_impl(context,data):
  context.search_bar = context.driver.find_element_by_css_selector("#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")
  context.search_bar.clear()
  context.search_bar.send_keys(data)


@when('search item')
def step_impl(context):
    context.search_bar = context.driver.find_element_by_css_selector("#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")
    global old_url
    old_url = context.driver.current_url
    context.search_bar.submit()

@then('Present list of 11 search result')
def step_impl(context):
    context.result_list = context.driver.find_elements_by_css_selector("#rso > div")
    number_of_results = len(context.result_list)
    if number_of_results == 11 :
      assert True, "Test Passed"
      context.driver.close()
    else:
      assert False, "Test Failed"
      context.driver.close() 

@then('Nothing happens')
def step_impl(context):
  if old_url == context.driver.current_url:
    assert True, "Test Passed"
    context.driver.close()
  else:
    assert False, "Test Failed"
    context.driver.close()

@then('The link "{message}" appears')
def step_impl(context,message):
  context.suggestion = context.driver.find_element_by_css_selector("#taw > div:nth-child(2) > div > p > span")
  text = context.suggestion.text
  if text == message:
    assert True, "Test Passed"
    context.driver.close()
  else:
    assert False, "Test Failed"
    context.driver.close()


    
