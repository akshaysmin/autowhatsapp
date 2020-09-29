status_date = status_list[3].find_element_by_class_name("_2kHpK").find_element_by_class_name("_1582E").text.split(" ")
print(status_date)
status_day = datetime.strptime(datetime.now().strftime('%d/%m/%Y') + ' ' + status_date[2], '%d/%m/%Y %H:%M')
print("today : ",status_day.strftime("%d/%m/%Y %H:%M:%S"))
delta_days = -1 if status_date[0]=="yesterday" else 0
delta_hours= +12 if status_date[3]=="PM" else 0
actual_status_date = status_day + timedelta(hours=delta_hours,days=delta_days)
actual_status_date = actual_status_date.strftime("%d/%m/%Y %H:%M:%S")
print("actual_status_date : ",actual_status_date)

