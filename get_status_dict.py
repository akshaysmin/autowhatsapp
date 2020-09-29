def get_status_info_dict(status_list):
	status_info_dict = {}
	for j,status in enumerate(status_list):
		print(f'-----------------------{j}------------------------------')
		try :
			status_info = status.find_element_by_class_name("_2kHpK")
			status_name = status_info.find_element_by_class_name("_3dtfX").text
			status_time_text = status_info.find_element_by_class_name("_1582E").text
			
			try:
				#print('making points')
				points = status.find_element_by_tag_name("circle").get_attribute("stroke-dasharray")
				points = '1 2' if points==None else points
			
				status_num = len(points.strip().split(" "))/2
				print(status_num)
			except:
				print('Error in num_status')
			
			
			print('making times')
			status_time_list = status_time_text.split(" ")
			print(status_time_list)
			status_time = status_time_list[2]
			status_time = f'00:{status_time[3:]}' if status_time[0:2]=='12' else status_time #convert 12:** to 00:**
			status_day = datetime.strptime(datetime.now().strftime('%d/%m/%Y') + ' ' + status_time, '%d/%m/%Y %H:%M')
			delta_days = -1 if status_time_list[0]=="yesterday" else 0
			delta_hours= +12 if status_time_list[3]=="PM" else 0
			actual_status_time = status_day + timedelta(hours=delta_hours,days=delta_days)
			actual_status_time = actual_status_time.strftime("%d/%m/%Y %H:%M:%S")
			print("actual_status_time : ",actual_status_time)
			
			print(f"({j+1}){status_name},{status_time_text},{actual_status_time},{status_num}")
			status_info_dict[status_name] = f"{status_time_text},{actual_status_time},{status_num}"
			
		
		except Exception as e:
			print('Error in status', j)
			print(e.__doc__)
		
	return status_info_dict