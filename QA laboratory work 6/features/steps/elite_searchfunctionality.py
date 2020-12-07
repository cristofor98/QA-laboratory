from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from seleniumwire import webdriver 
import unittest

def check_error_page(text):
	if text == "Page Not Found":
		return True
	return False

@given('I am on the website homepage')
def step_impl(context):
	context.driver = webdriver.Chrome('/Users/tekwill/Downloads/chromedriver')
	context.driver.get("https://adoring-pasteur-3ae17d.netlify.app/index.html#")
   


@when('I enter search term as "{product}"')
def step_impl(context,product):
	context.search_bar = context.driver.find_element_by_name("search")
	context.search_bar.clear()
	context.search_bar.send_keys(product)
    


@then('Search results should appear')
def step_impl(context):
	context.search_bar.submit()
	try:
		text = context.driver.find_element_by_css_selector("div.header > h1").text
	except:
		assert True, "Test Passed"
		context.driver.close()
	if check_error_page(text):
		assert False, "Test Failed"
		context.driver.close()

