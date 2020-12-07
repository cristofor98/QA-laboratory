from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from seleniumwire import webdriver 
import unittest

y_position = 0

@given('I am on the product page')
def step_impl(context):
	context.driver = webdriver.Chrome('/Users/tekwill/Downloads/chromedriver')
	context.driver.get("https://adoring-pasteur-3ae17d.netlify.app/single.html") 


@when('Click on REVIEW tab')
def step_impl(context):
	context.review_tab = context.driver.find_element_by_xpath("//*[@id=\"horizontalTab\"]/ul/li[2]")

@when('Click on REPLY button')
def step_impl(context):
	global y_position
	y_position = context.driver.execute_script("return window.pageYOffset;", 1)
	context.reply_button = context.driver.find_element_by_css_selector("a")
	context.reply_button.click()

@then('A review reply form appears')
def step_impl(context):
	y_position2 = context.driver.execute_script("return window.pageYOffset;", 1)
	if y_position2 < y_position:
		assert False, "Test Failed"
		context.driver.close()
	else:
		assert True, "Test Passed"
		context.driver.close()