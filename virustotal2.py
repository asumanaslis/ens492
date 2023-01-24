# -*- coding: utf-8 -*-
"""Virustotal2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19XvJLnR1c1MngpY3APTJWwIPnKkISaRX
"""

from google.colab import drive
drive.mount('/content/drive', force_remount=True)

import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/ENS 491 Phishing detection/domains.csv')

df.drop(columns=df.columns[0], axis=1,  inplace=True)

df

n = int(len(df.index)/4 ) + 1

df2 = df.iloc[n:(2*n)]

pip install virustotal_python

import requests
import time
import json
import pandas
import os

whoisdsVirusTotalDF = pd.DataFrame().assign(URL=df2['domain'])

url_list = whoisdsVirusTotalDF.values.tolist()

cols = ['URL', 'Status','Total Detect','Total Engine']
dat = pd.DataFrame(columns = cols)


API_key = 'ad0e459b16e2de4d5f489dfa4067b45855e82ec62f09dc5e71b8a48d2e50294a'
url = 'https://www.virustotal.com/vtapi/v2/url/report'


#parameters = {'apikey': API_key, 'resource': url_list}

for i in url_list:
  i = i[0]
  parameters = {'apikey': API_key, 'resource': i}

  response= requests.get(url=url, params=parameters)
  if response.status_code == 403:
    print("Error from server: " + str(response.content))
    a = "Not Found"
    b = "-"
    c = "-"
  else:
    json_response= json.loads(response.text)
  
    if json_response['response_code'] <= 0:
      a = "Not Found"
      b = "-"
      c = "-"
    elif json_response['response_code'] >= 1:
      if json_response['positives'] <= 0:
        a = "Clean"
        b = "0"
        c = "90"
      else:
        a = "Malicious"
        b = str(json_response['positives'])
        c = "90"
  dat = dat.append({'URL': i, 'Status':a,'Total Detect':b, 'Total Engine':c,},ignore_index=True)


  time.sleep(15)

dat

dat.to_csv('/content/drive/MyDrive/ENS 491 Phishing detection/virustotal2v3.csv')