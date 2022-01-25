import os
import pandas as pd
import numpy as np

root_path = r'/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/dtpa/finished_folders2/'
excel_path = [(root_path + s + '/result.xls') for s in os.listdir(root_path)]
# print(excel_path)

res = pd.DataFrame(columns=('Patient_ID', 'GFR_L', 'GFR_R','Area_L','Area_R', 'Study_date'))

for each_patient in os.listdir(root_path):
    patient_id = each_patient[0:8]
    print(patient_id)
    study_date = each_patient[9:]
    print(study_date)
    each_excel_path = os.path.join(root_path, each_patient, 'result.xls')
    data_in = pd.read_excel(each_excel_path)
    inde = data_in.index[(data_in['words']=='GFR:')].values
    print(inde)
    L_GFR_value = data_in.iloc[inde+1, 1]
    R_GFR_value = data_in.iloc[inde+2, 1]
    print(f'L_GFR_value:{L_GFR_value.values[0]}')
    print(f'R_GFR_value: {R_GFR_value.values[0]}')

    inde_area = data_in.index[(data_in['words']=='Kidney Area():')].values
    if len(inde_area) == 0:
        inde_area = data_in.index[(data_in['words']== 'Kidney Area (cm^2):')]
    if len(inde_area) == 0:
        inde_area = data_in.index[(data_in['words']== 'Kidney Area(cm^2):')]
    if len(inde_area) == 0:
        inde_area = data_in.index[(data_in['words']== 'Kidney Area(cm2):')]
    if len(inde_area) == 0:
        inde_area = data_in.index[(data_in['words']== 'Kidney Area (cm2):')]
    if len(inde_area) == 0:
        inde_area = data_in.index[(data_in['words']== 'Kidney Area(cm^):')]
    if len(inde_area) == 0:
        inde_area = data_in.index[(data_in['words']== 'Kidney Area (cmA2):')]

    print(inde_area)
    print(data_in.iloc[10, :])

    L_area_value = data_in.iloc[inde_area+1, 1]
    R_area_value = data_in.iloc[inde_area+2, 1]
    print(f'L_area_value:{L_area_value.values[0]}')
    print(f'R_area_value: {R_area_value.values[0]}')
    new  = pd.DataFrame([{'Patient_ID' : patient_id,
                          'GFR_L' : L_GFR_value.values[0],
                          'GFR_R' : R_GFR_value.values[0],
                          'Area_L' : L_area_value.values[0],
                          'Area_R' : R_area_value.values[0],
                          'Study_date' : study_date
                          }
                          ])
    res = res.append(new, ignore_index=True) 
    # print(res.head)
res.to_excel('/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/dtpa/renamed_dtpa/all_output_data69.xls')
print('Done !!!')

