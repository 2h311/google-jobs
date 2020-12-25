from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_driver_instance(driver_path = "./chromedriver/chromedriver.exe"):
	chrome_options = Options()
	chrome_options.add_argument("start-maximized")
	chrome_options.add_argument("log-level=3")
	chrome_options.add_experimental_option("useAutomationExtension", False)
	chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
	return webdriver.Chrome(executable_path=driver_path, options=chrome_options)

driver = create_driver_instance()
# i'm using this for testoting purposes only
driver.get('https://google.com')