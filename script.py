import logging
import os
import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import locators 
from timekeeper import TimeKeeper
from piper import DataClassExcelFields

def set_windows_title():
	'''
	customizes the window title
	'''
	os.system('title Google Jobs Tool')

def create_driver_handler(driver_path="./chromedriver/chromedriver.exe"):
	'''
	creates a browser instance for selenium, 
	it adds some functionalities into the browser instance
	'''
	chrome_options = Options()
	chrome_options.add_argument("start-maximized")
	chrome_options.add_argument("log-level=3")
	# the following two options are used to take out the chrome browser infobar
	chrome_options.add_experimental_option("useAutomationExtension", False)
	chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
	driver_instance = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
	driver_instance.implicitly_wait(10)
	return driver_instance

def click_helper(selector):
	'''
	this is an helper function that collects a locator and 
	clicks that element with that locator 
	'''
	element = driver.find_element_by_css_selector(selector)
	element.click()

def clear_search_input_element(locator_class):
	'''
	clears the search input element
	'''
	click_helper(locator_class.clear_search_button)
	
def click_search_button_element(locator_class):
	'''
	clicks the search button
	'''
	click_helper(locator_class.search_button)

def activate_nap_mode():
	'''
	sleeps the bot for a random number of seconds
	'''
	time_to_sleep_for = random.randrange(1, 5)
	logging.info(f"Activating Nap Mode for {time_to_sleep_for} seconds")
	time.sleep(time_to_sleep_for)

def scroll_element_into_view(element):
	driver.execute_script("arguments[0].scrollIntoView();", element)

set_windows_title()

logging.basicConfig(format="[+] %(message)s", level=logging.INFO)
driver = create_driver_handler()
timekeeper = TimeKeeper()

GoogleSearchPageLocators = locators.GoogleSearchPageLocators
GoogleJobsPageLocators = locators.GoogleJobsPageLocators

# TODO: we need to fetch the keywords from a file
search_word = "singtel Tao Payoh"

search_page_url = "https://www.google.com/search?q=google+jobs"
driver.get(search_page_url)

# fish out the "/d+ more jobs" link on the g-card tag 
anchor_tag_elements = driver.find_elements_by_css_selector(GoogleSearchPageLocators.anchor_tags)
# first let's assume it's always going to be the last anchor tag
# if that changes later, we can simply work it out  
more_jobs_element = anchor_tag_elements[-1]
google_jobs_url = more_jobs_element.get_attribute('href')
activate_nap_mode()
driver.get(google_jobs_url)

# input the search word into the input element
clear_search_input_element(GoogleJobsPageLocators)
driver.find_element_by_id(GoogleJobsPageLocators.search_input_element).send_keys(search_word)
activate_nap_mode()
click_search_button_element(GoogleJobsPageLocators)

# TODO: sift through the jobs cards one after the other and fetch the needed data.
job_cards = driver.find_elements_by_tag_name(GoogleJobsPageLocators.jobs_cards)
card = job_cards[0]

scroll_element_into_view(card)

datetime_of_search = timekeeper.keep_search_datetime()
result_title = card.find_element_by_css_selector(GoogleJobsPageLocators.result_title).text
date_and_time = card.find_element_by_css_selector(GoogleJobsPageLocators.date_and_time).text
publisher = card.find_element_by_css_selector(GoogleJobsPageLocators.publisher).text

data_to_send_to_writer = DataClassExcelFields(
	datetime_of_search=datetime_of_search, 
	date_and_time=date_and_time,
	keyword=search_word,
	publisher=publisher,
	result_title=result_title,
)

print(data_to_send_to_writer)