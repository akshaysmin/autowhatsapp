print('-----------status_list check------------')
print('length : ',len(status_list))
for i,status in enumerate(status_list):
	print(f'({i})')
	try:
		status_info = status.find_element_by_class_name("_2kHpK")
		status_name = status_info.find_element_by_class_name("_3dtfX").text
		print(status_name)
	except Exception as e:
		print(e.__doc__)