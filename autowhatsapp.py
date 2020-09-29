'''
opens whatsapp web, after login with phone, sends given msg to specified contact
'''

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

driver_path = "geckodriver.exe" #replace it with path to chromedriver
contact = input("Enter contact name (Exactly) : ")		
message = input("Enter message to send : ")		

driver = webdriver.Firefox(executable_path=driver_path) #change to webdriver.Chrome
driver.get("https://web.whatsapp.com")

#search
input("Press Enter if webpage is ready")
xpath_search = "/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]" #this is directly copied from browser inspect element
search_box = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(xpath_search))
print(f"searching {contact}")
search_box.click()
search_box.send_keys(contact)
time.sleep(2)

#select
print(f"selecting {contact}")
driver.find_element_by_xpath(f'//*[@title="{contact}"]').click()
time.sleep(2)

#message
msg_clickable = driver.find_element_by_xpath("//div[contains(@class, '_3uMse')]")
msg_clickable.click()
msg_typable = msg_clickable.find_element_by_tag_name("div").find_element_by_class_name("_3FRCZ")
msg_typable.send_keys(message,Keys.ENTER)