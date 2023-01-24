# -*- coding: utf-8 -*-
"""selTest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1to7IFWTnbLG1IpfOgJ-tWrGM1FD8DatC
"""

import pymongo
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pyvirtualdisplay import Display
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import codecs
from selenium.webdriver.common.by import By
from ping3 import ping
from threading import Thread
import urllib3
from http.client import responses
import subprocess
import urllib.request
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import threading
import os
import multiprocessing
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import time
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from urllib3.exceptions import MaxRetryError, NewConnectionError
from selenium.common.exceptions import TimeoutException,InvalidArgumentException
from selenium.common import exceptions

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

CONNECTION_STRING = "mongodb://ens492admin:ens492@143.198.147.247:27017/?directConnection=true&serverSelectionTimeoutMS=2000&authSource=admin&appName=mongosh+1.6.1"
# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
client = MongoClient(CONNECTION_STRING)

dbname = client['urlContents']
collection_name = dbname["whoisds"]
import datetime
today = datetime.date.today()
from datetime import date, timedelta, datetime
today = datetime.today()
date_today = today.strftime("%d/%m/%Y")
time2 = time.asctime()
splittedtime = time2.split(" ")
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
try:
    import queue
except ImportError:
    import Queue as queue
import re

num_threads = 50
ips_q = queue.Queue()

server_list_file = open('/home/output.txt', 'r')
hosts = server_list_file.read()
ips = hosts.split('\n') 
ips.pop()

chrome_options = Options()
chrome_options.page_load_strategy = "eager"
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('ignore-certificate-errors')
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument('--ignore-ssl-errors=yes')
chrome_options.add_argument('--ignore-certificate-errors')
 
capabilities = DesiredCapabilities.CHROME
capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
prefs = {"download.default_directory" : "/home"}
chrome_options.add_experimental_option("prefs",prefs)
start = time.perf_counter()

def my_content(new_u):
  try:
    d = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options,desired_capabilities=capabilities)
    d.set_page_load_timeout(10)
    d.get(new_u)
    html = d.page_source
    soup = BeautifulSoup(html, features="html.parser")
    d.quit()
  except TimeoutException as e:
    #print("EEK! TimeoutException", e)
    soup = "EEK! TimeoutException"
  except (ConnectionRefusedError, MaxRetryError, NewConnectionError) as e:
    #print("EEK! Connection error", e)
    soup = "EEK! Connection error"
  except InvalidArgumentException as e:
    soup = "EEK! Invalid Argument Exception"
  except Exception as e:
    #print("EEK! Unexpected exception in webdriver.get: " + str(e))
    soup = "EEK! Unexpected exception in webdriver.get: "
  return soup

def thread_pinger(q): 
  line = q.split()
  if(line[1][0] == '3'):
    url = line[2]
    content = my_content(url)
  else:
    url = line[0]
    content = my_content(url)
  item = {
  "date": date_today,
  "time": splittedtime[4],
  "url" : url,
  "status_code" : line[1],
  "content" : str(content)
  }
  if(line[1][0] != '0'):
    collection_name.insert_one(item)
  return url

with concurrent.futures.ThreadPoolExecutor(num_threads) as executor:
  future_to_url = {executor.submit(thread_pinger, url): url for url in ips}
  for future in concurrent.futures.as_completed(future_to_url,timeout=30):
    url = future_to_url[future]
    try:
      data = future.result()
      print(data)
    except future.TimeoutError:
      print("Timeout: "+url)
      
finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')