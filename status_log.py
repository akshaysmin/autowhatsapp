from selenium import webdriver
from datetime import datetime
from datetime import timedelta
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import code

def get_status_info_dict(status_list):
	status_info_dict = {}
	for j,status in enumerate(status_list):
		#print(f'-----------------------{j}------------------------------')
		try :
			status_info = status.find_element_by_class_name("_2kHpK")
			status_name = status_info.find_element_by_class_name("_3dtfX").text
			status_time_text = status_info.find_element_by_class_name("_1582E").text
			
			try:
				#print('making points')
				points = status.find_element_by_tag_name("circle").get_attribute("stroke-dasharray")
				points = '1 2' if points==None else points
			
				status_num = len(points.strip().split(" "))/2
				#print(status_num)
			except:
				print('Error in num_status, in get_status_info_dict')
			
			
			#print('making times')
			status_time_list = status_time_text.split(" ")
			#print(status_time_list)
			status_time = status_time_list[2]
			status_time = f'00:{status_time[3:]}' if status_time[0:2]=='12' else status_time #convert 12:** to 00:**
			status_day = datetime.strptime(datetime.now().strftime('%d/%m/%Y') + ' ' + status_time, '%d/%m/%Y %H:%M')
			delta_days = -1 if status_time_list[0]=="yesterday" else 0
			delta_hours= +12 if status_time_list[3]=="PM" else 0
			actual_status_time = status_day + timedelta(hours=delta_hours,days=delta_days)
			actual_status_time = actual_status_time.strftime("%d/%m/%Y %H:%M:%S")
			#print("actual_status_time : ",actual_status_time)
			
			#print(f"({j+1}){status_name},{status_time_text},{actual_status_time},{status_num}")
			status_info_dict[status_name] = f"{status_time_text},{actual_status_time},{status_num}"
			
		
		except Exception as e:
			print('Error in status, in get_status_info_dict', j)
			print(e.__doc__)
		
	return status_info_dict

internet_slow = True if input("Is your internet slow ? (yes/no) : ").lower()=='yes' else False

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://web.whatsapp.com")

if not internet_slow:
	#click status_button
	#driver.find_element_by_xpath('//*[@title="Status"]').click()
	status_button = WebDriverWait(driver,500).until(lambda driver: driver.find_element_by_xpath('//*[@title="Status"]'))
	time.sleep(3)
	status_unread_icon = status_button.find_elements_by_xpath('//*[@data-icon="status-v3-unread"]')
	if status_unread_icon:
		status_button.click()
	else:
		print("Looks like all status are read or aren't fully loaded")
		input("Press Enter if you are ready to proceed")
		driver.find_element_by_xpath('//*[@title="Status"]').click()
	time.sleep(2)

if internet_slow: input("Press Enter after clicking show status button and status list is displayed")	

#extracting status info
status_list = driver.find_element_by_xpath('//*[@class="statusList"]').find_element_by_tag_name("span").find_elements_by_class_name("_210SC")
status_dict = get_status_info_dict(status_list)
scrollable = driver.find_element_by_class_name("_147Si")
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",scrollable)
time.sleep(2)
status_list = driver.find_element_by_xpath('//*[@class="statusList"]').find_element_by_tag_name("span").find_elements_by_class_name("_210SC")
status_dict_ = get_status_info_dict(status_list)
status_dict.update(status_dict_)

#log status info
status_log_file = "status_log.dat"
today = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
with open(status_log_file, 'a') as log:
	print('today : ',datetime.now().strftime('%d/%m/%Y'))
	print('----writing to file----')
	log.write(f"\nlog_date,{today},{len(status_dict)}\n")
	for i,status_name in enumerate(status_dict):
		log.write(f"{status_name},{status_dict[status_name]}\n")
		print(f"({i+1}) {status_name},{status_dict[status_name]}\n")

#return to homepage
if not internet_slow : driver.find_element_by_xpath('//*[@class="_19n1B"]').click()

code.interact(local=locals())
