import pandas as pd 
import requests

url = "https://data.ny.gov/resource/wujg-7c2s.json?$where=date_trunc_ym(transit_timestamp)='2023-08-01'"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
df = pd.read_json(response.json)

df.head()