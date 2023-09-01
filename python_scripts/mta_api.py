import pandas as pd 
import requests

filter_date = '2023-01-01'
def query_mta(fdate):
    url = "https://data.ny.gov/resource/wujg-7c2s.json?$where=date_trunc_ym(transit_timestamp)='{}'".format(fdate)

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    rjson = response.json()
    try:
        df = pd.DataFrame(rjson)
        path_str = 'C:\Users\kduba\OneDrive\Documents\MTA_DB\text_files\mta_{}.csv'.format(fdate)
        df.to_csv(path_str)
        return('success')
    except:
        return('failure')
message = query_mta(filter_date)
print(message)