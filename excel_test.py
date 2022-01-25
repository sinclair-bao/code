import os
import pandas as pd
import numpy as np

data_input = pd.read_excel('/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/dtpa/renamed_dtpa/00109452_20201027/result.xls')
print(data_input)
# print(type(data_input))
inde = data_input.index[(data_input['words']==' GFR:')].values
print(inde)
res = pd.DataFrame(columns=('Patient_ID', 'GFR_L', 'GFR_R','Area_L','Area_R'))

# print(data_input['words'])
# print((data_input['words']==' GFR:'))
print(data_input.iloc[25, 0])
L_GFR_value = data_input.iloc[inde+1, 0]
R_GFR_value = data_input.iloc[inde+2, 0]
print(f'L_GFR_value:{L_GFR_value.values[0]}')
print(f'R_GFR_value: {R_GFR_value.values[0]}')

inde_area = data_input.index[(data_input['words']==' Kidney Area():')].values
print(inde_area)
print(data_input.iloc[10, 0])

L_area_value = data_input.iloc[inde_area+1, 0]
R_area_value = data_input.iloc[inde_area+2, 0]
print(f'L_area_value:{L_area_value.values[0]}')
print(f'R_area_value: {R_area_value.values[0]}')
new  = pd.DataFrame([{'Patient_ID' : '123',
                          'GFR_L' : L_GFR_value.values[0],
                          'GFR_R' : R_GFR_value.values[0],
                          'Area_L' : L_area_value.values[0],
                          'Area_R' : R_area_value.values[0],
                          }
                          ])
res = res.append(new, ignore_index=True) 
print(res.head)
res.to_excel('/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/dtpa/renamed_dtpa/00109452_20201027/output.xls')

