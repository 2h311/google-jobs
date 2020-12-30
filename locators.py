'''
separation of selectors and locators from the main logic
'''

class GoogleSearchPageLocators:
	anchor_tags = 'g-card a'

class GoogleJobsPageLocators:
	clear_search_button = 'button[aria-label="Clear search"]'
	search_button = 'button[aria-label="Search"]'
	search_input_element = "hs-qsb"
	jobs_cards = 'li'
	result_title = '[role="heading"]'
	date_and_time = '[class*=KKh3md] span'
	publisher = '[class*=vNEEBe]'
