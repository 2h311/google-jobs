import logging
import os
import pprint
import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import locators 
from timekeeper import TimeKeeper
from xlsxwriter import XlsxWriter
from filereader import FileReader

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

def activate_nap_mode(secs=random.randrange(1, 5)):
	'''
	sleeps the bot for a random number of seconds
	'''
	logging.info(f"Activating Nap Mode for {secs} seconds")
	time.sleep(secs)

def scroll_element_into_view(element):
	driver.execute_script("arguments[0].scrollIntoView();", element)

set_windows_title()

logging.basicConfig(format="[+] %(message)s", level=logging.INFO)
driver = create_driver_handler()

# these are our helper classes
timekeeper = TimeKeeper()
excel_writer = XlsxWriter()

keywords = FileReader().grab_content_of_file()

GoogleSearchPageLocators = locators.GoogleSearchPageLocators
GoogleJobsPageLocators = locators.GoogleJobsPageLocators

# we need to fetch the keywords from a file
keyword = keywords[3]

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
driver.find_element_by_id(GoogleJobsPageLocators.search_input_element).send_keys(keyword)
activate_nap_mode()
click_search_button_element(GoogleJobsPageLocators)

job_cards = driver.find_elements_by_tag_name(GoogleJobsPageLocators.jobs_cards)
if not job_cards:
	print("No jobs match your search at the moment")

cnt = 1
o = 10
cap = 100

while True:

	try:
		card = job_cards[cnt-1]
		scroll_element_into_view(card)		
	except IndexError as err:
		print(f"An Error occured: {err}")
		break

	datetime_of_search = timekeeper.now
	result_title = card.find_element_by_css_selector(GoogleJobsPageLocators.result_title).text
	date_and_time = card.find_element_by_css_selector(GoogleJobsPageLocators.date_and_time).text
	publisher = card.find_element_by_css_selector(GoogleJobsPageLocators.publisher).text

	data_to_send_to_writer = {
		"Date & time of search": datetime_of_search,
		"Date/Time": date_and_time,
		"Keyword": keyword,
		"Publisher": publisher,
		"Result_Title": result_title,
	}

	pprint.pprint(data_to_send_to_writer)
	excel_writer.write_to_sheet(data_to_send_to_writer)

	print(f'{(cnt % o)}')
	if (cnt % o) == 0: # this will trigger on the 10th item 
		print('\awe got a modulo !')

		activate_nap_mode(15)
		job_cards = driver.find_elements_by_tag_name(GoogleJobsPageLocators.jobs_cards)

		if cnt == len(job_cards):
			print("New data isn't coming in . breaking")
			break

	if cnt == cap:
		break
	
	cnt += 1