import gspread
from datetime import date

new_sales = [
{'employee_name': 'Bob',
'current_sales': '12690'},
{'employee_name': 'Fred',
'current_sales': '14448'},
{'employee_name': 'Jan',
'current_sales': '2373'},
{'employee_name': 'Elidia',
'current_sales': '9250'},
# notice that I'm skipping Jill - her sales should remain the same w/ no updated_date.
# This could be an example where my api didn't successfully complete the update value for Jill.
{'employee_name': 'George',
'current_sales': '6265'},
{'employee_name': 'Sally',
'current_sales': '6311'},
{'employee_name': 'Joe',
'current_sales': '11963'},
{'employee_name': 'Nadim',
'current_sales': '5900'},
{'employee_name': 'Jared',
'current_sales': '11813'},
{'employee_name': 'Megan',
'current_sales': '9151'},
{'employee_name': 'Amber',
'current_sales': '6930'},
{'employee_name': 'Fred',
'current_sales': '2830'},
{'employee_name': 'Linda',
'current_sales': '7966'}, # Linda's sales were found, but didn't change. We would still want to write the value
# and the new updated_date
{'employee_name': 'Dave',
'current_sales': '3894'},
{'employee_name': 'Carlos',
'current_sales': '1564'}
]

new_dict = {item['employee_name']:item['current_sales']  for item in new_sales }
today = date.today().strftime("%m/%d/%Y")
range_value_data_list = []

gc = gspread.service_account("service_account.json")
sh = gc.open_by_key('1UEYC_VeF3vi90WXXN8xBuIMt9ZzGz5FovMyGAVCVyy8')
worksheet = sh.get_worksheet(0)
for i in range(2, 19):
    em_name = worksheet.cell(i, 1).value
    
    if em_name in new_dict:
        range_value_item_str = { 'range': "B{}:C{}".format(i, i), 'values': ([[new_dict[em_name], today]]) }
        range_value_data_list.append(range_value_item_str)
        
worksheet.batch_update(range_value_data_list)