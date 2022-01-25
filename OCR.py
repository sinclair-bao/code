# encoding:utf-8
import pandas as pd
import numpy as np
import os
import requests
import base64

'''
通用文字识别（高精度版）
'''

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# 二进制方式打开图片文件
#f = open('[本地文件]', 'rb')
f = open('/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/dtpa/renamed_dtpa/00109452_20201027/report_2.png', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
#access_token = '[调用鉴权接口获取的token]'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=eL5Tl7Ifyhgmeo0oaByQ1GlF&client_secret=LjY6NdXG0wBT6FGXG9O60aG6HXx01uMe'
response = requests.get(host)
if response:
    #print(response.json())
    response = response.json()
access_token = response['access_token']
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
output = []
if response:
    # print (response.json()['words_result'])
    result = response.json()['words_result']
    result = pd.DataFrame(result)

print(result)
result.to_excel('/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/dtpa/renamed_dtpa/00109452_20201027/result.xls')

