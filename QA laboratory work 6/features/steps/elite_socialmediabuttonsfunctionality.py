from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from seleniumwire import webdriver 
import unittest

old_url = None

@when('Click social media button for linked')
def step_impl(context):
	global old_url
	old_url = context.driver.current_url
	context.socialmedia_button = context.driver.find_element_by_css_selector("i")
	context.socialmedia_button.click()


@then('the social media page appear')
def step_impl(context):
	if old_url != context.driver.current_url:
		assert True, "Test Passed"
		context.driver.close()
	else:
		assert False, "Test Failed"
		context.driver.close()
     