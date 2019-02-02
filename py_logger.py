#pip install gspread
#pip install --upgrade oauth2client
#pip install PyOpenSSL


import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

#############!!!!!!!!!!!Input needed, path to your json credentials file!!!!!!!!!!!#############
credentials = ServiceAccountCredentials.from_json_keyfile_name('path to your json file', scope)

gc = gspread.authorize(credentials)


####if you are creating a new spreadsheet using code####
sh = gc.create("button_log")
#############!!!!!!!!!!!Input needed, your email id!!!!!!!!!!!#############
sh.share('arjunsg@uw.edu', perm_type='user', role='writer') #share it with your gmail id to view it in drive
worksheet = sh.sheet1


####if using a pre-existing spreadsheet or creating a new one from the web interface####
#worksheet = gc.open("rpi_logs").sheet1 #name of the spreadsheet
#list_of_lists = worksheet.get_all_values()



#######log values######
list_of_lists = worksheet.get_all_values()
line = len(list_of_lists)+1
worksheet.add_rows(line+2)
worksheet.update_cell(line, 1, str(datetime.datetime.now()))
worksheet.update_cell(line, 2, 'Bingo!')