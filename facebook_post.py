
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import getpass
import sys

email = input("Facebook Email")
pswd = getpass.getpass("Facebook Password")
url = input("URL of people you want to post to, separated by comma")
message = input("What do you want to tell them?")

driver = webdriver.Chrome()

# go to the google home page
driver.get("https://www.facebook.com")
# the page is ajaxy so the title is originally this:
print(driver.title)

# find the element that's name attribute is q (the google search box)
inputElement = driver.find_element_by_name("email")

# type in the search
inputElement.send_keys(email)

inputElement = driver.find_element_by_name("pass")
inputElement.send_keys(pswd);
# submit the form (although google automatically searches now without submitting)
inputElement.submit()

for c in url.split(','):
	driver.get(c)
	inputElement = driver.find_element_by_name("xhpc_message_text")
	inputElement.send_keys(message)
	inputElement.submit()

try:
   # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    
    # You should see "cheese! - Google Search"
    	print(driver.title)

finally:
	driver.quit()
