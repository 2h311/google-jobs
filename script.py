import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_driver_handler(driver_path="./chromedriver/chromedriver.exe"):
	'''
	this function creates a browser instance for selenium 
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

def clear_search_input_element():
	'''
	this function simply clears the search input element
	'''
	click_helper('button[aria-label="Clear search"]')
	
def click_search_button_element():
	'''
	this function clicks the search button
	'''
	click_helper('button[aria-label="Search"]')

driver = create_driver_handler()
search_word = "singtel"
search_page_url = "https://www.google.com/search?q=google+jobs"
driver.get(search_page_url)

# fish out the "/d+ more jobs" link on the g-card tag 
anchor_tag_elements = driver.find_elements_by_css_selector('g-card a')
# first let's assume it's always going to be the last anchor tag
# if that changes later, we can simply work it out  
more_jobs_element = anchor_tag_elements[-1]
google_jobs_url = more_jobs_element.get_attribute('href')
driver.get(google_jobs_url)

# search form element
# google_jobs_search_form_element = driver.find_element_by_css_selector('form[role="search"]')
# input_element = google_jobs_search_form_element.find_element_by_css_selector("input")
# input the search word into the input element
driver.find_element_by_id("hs-qsb").send_keys(search_word)

