from typing_extensions import ParamSpecArgs
import gspread
import json
from oauth2client.client import Storage
from oauth2client.service_account import ServiceAccountCredentials
from six import string_types

#Google Spread Sheetsにアクセス
def connect_ss(jsonf,key):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonf, scope)
    gc = gspread.authorize(credentials)
    SPREADSHEET_KEY = key
    workbook = gc.open_by_key(SPREADSHEET_KEY)
    return workbook

def  spread_sheet_update(pass_info):
 
    json_file = " " #credential json file name from spreadsheet
    spread_sheet_key = " "  #credential key from spreadsheet
    wb = connect_ss(json_file,spread_sheet_key)

    ws_list = wb.worksheets()
    num_sheet_version = len(ws_list)-1
    storage_name = "ver" + f'{num_sheet_version:0=2}'
    wb.add_worksheet(title = storage_name, rows=1000, cols=10)
    ws_for_storage = wb.worksheet(storage_name)

    ws_for_reference = wb.worksheet("参照")
    ws_for_reference.clear()
    ws_for_reference.update(pass_info, value_input_option="USER_ENTERED")
    ws_for_storage.update(pass_info, value_input_option="USER_ENTERED")

if __name__=='__main__':
    import shimcham_module #module to create pass prediction as List
    import datetime
    start_time = datetime.datetime.now()
    end_time = start_time + datetime.timedelta(days = 30)
    spread_sheet_update(shimcham_module.shimcham(start_time, end_time))



