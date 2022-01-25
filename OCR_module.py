# encoding:utf-8
import pandas as pd
import numpy as np
import os
import requests
import base64
import shutil

'''
通用文字识别（高精度版）
'''
root_path = r'/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/dtpa/renamed_dtpa3/'
report_path = [(root_path + s + '/report_2.png') for s in os.listdir(root_path)]
# print(png_path)

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
i = 0
for each_report_path in report_path:
    print(each_report_path)
    i = i +1
    print(i)
    f = open(each_report_path, 'rb')
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
    print(response)
    output = []
    if response:
        print (response.json()['words_result'])
        result = response.json()['words_result']
        result = pd.DataFrame(result)
        print(result)

    print('Convert Done')
    uper_path = os.path.abspath(os.path.join(each_report_path, '..'))
    print(uper_path)
    excel_write_path = os.path.join(uper_path, 'result.xls')
    # print(excel_write_path)
    result.to_excel(excel_write_path)
    target_path = '/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/dtpa/finished_folders2'
    shutil.move(uper_path, target_path)
    print('Finished !')

