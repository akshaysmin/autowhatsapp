from selenium import webdriver
from datetime import datetime
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

'''
driver = webdriver.Firefox(executable_path="geckodriver.exe")

#goto https://web.whatsapp.com and login
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
input()
print("Logged In")

def send_message(contact,message):
	#inp_xpath_search = "//input[@title='Search or start new chat']"
	inp_xpath_search = "//span[.='Search or start new chat']"
	input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
	input_box_search.click()
	time.sleep(2)
	input_box_search.send_keys(contact)
	time.sleep(2)

send_messsage("Tom","Automated by python!")

time.sleep(2)
driver.quit()
'''