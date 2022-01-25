from heapq import merge
import numpy as np
import pandas as pd
import os
import xlrd
data_set1_path = r'/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/all_output_data69.xls'
data_set2_path = r'/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/all_patients_data_2022.xls'

data_set1 = pd.read_excel(data_set1_path, dtype={'Patient_ID': str, 'Study_date': str, 'Area_L': float, 'Area_R':float, 'GFR_L':float, 'GFR_R':float}, )
data_set2 = pd.read_excel(data_set2_path, dtype={'Patient_ID':str, 'Patient_Sex':str, 'Study_Date':str, 'Patient_Age':str})

data_set1['other'] = data_set1['Patient_ID'] + data_set1['Study_date']
# print(data_set1['other'])
# print(data_set1.head)
data_set2['other'] = data_set2['Patient_ID'] + data_set2['Study_Date']
# print(data_set2.head)
data_set1_target_data = data_set1[['Area_L', 'Area_R', 'GFR_L', 'GFR_R', 'Study_date', 'Patient_ID', 'other']]
data_set2_target_data = data_set2[['Patient_Sex', 'Patient_Weight', 'Patient_Size', 'Patient_Age', 'other']]
print(data_set1_target_data.head)
print(data_set2_target_data.head)

all_data = pd.merge(data_set1_target_data, data_set2_target_data, left_on='other', right_on='other')
print(all_data.head)

all_data['Total_GFR'] = all_data['GFR_L'] + all_data['GFR_R']
print(all_data.head)
all_data.to_csv('/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/all_data_90.csv')
all_data.to_excel('/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/all_data_90.xls')