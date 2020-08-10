#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 22:59:21 2018

@author: devops
"""
# Importing the libraries
import time
import requests
import json

target = "http://127.0.0.1:3091"
urls = target + '/api/fight/'
ws = open('hdfight.mp4', 'rb')#.read()
files = {'file': ws}
info = {'gps':'12344333','id':'11977354',"time-stamp":'3240234049820349'}
millis = int(round(time.time() * 1000))
r = requests.post(urls, data=info, files=files)
json_data = json.loads(r.text)
millis2 = int(round(time.time() * 1000))
print("processing time in server " ,json_data['processing_time'])
print("tootal time from client and all is  " ,str(millis2-millis))
print(json_data['precentegeoffight'])
msgg = 'حدث عنف في العلاوي';
#if float(json_data['precentegeoffight']) >= 0.78:
#    reqs = requests.get('https://mamonrasool.com/mastermamon/pushmamon.php?USBBAN10388=azm00774615nEeaoknva110205678&mapaaSSS13455znb0=Azncb87268$$22mmsknnns0199556782&MSG='+msgg)
