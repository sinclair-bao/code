'''Data collection and generate an excel file
'''
from posix import listdir
from PIL.Image import ID
import pydicom
import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
import shutil
print(pydicom.__version__)
main_file_path = '/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/dtpa/sample-check'
all_patients = listdir(main_file_path)
folder_path = [(main_file_path + '/' + s) for s in os.listdir(main_file_path)]
#uptale_interval_path = [(p + '/' + 'Uptakeinterval001_DS.dcm') for p in folder_path]

'''
check if 2secondsframes001_DS.dcm is avariable
and get the patient id and many other clinical data if avariable
'''
two_seconds_frames_path = [(p + '/' + 'POST001_DS.dcm') for p in folder_path]
print(two_seconds_frames_path[0])
print(len(two_seconds_frames_path))
res = pd.DataFrame(columns=('Patient_ID', 'Patient_Sex', 'Patient_Weight','Patient_Size','Study_Date', 'Patient_Age'))
for every_one in two_seconds_frames_path:
    print(every_one)
    dicom_img = pydicom.read_file(every_one)
    dicom_data = np.array(dicom_img.pixel_array)
    patient_id = dicom_img.PatientID
    patient_sex = dicom_img.PatientSex
    patient_weight = dicom_img.PatientWeight
    patient_size = dicom_img.PatientSize
    study_date = dicom_img.StudyDate
    try:
        patient_age = dicom_img.PatientAge
    except:
        patient_age = 0
    new  = pd.DataFrame([{'Patient_ID' : patient_id,
                          'Patient_Sex' : patient_sex,
                          'Patient_Weight' : patient_weight,
                          'Patient_Size' : patient_size,
                          'Study_Date' : study_date,
                          'Patient_Age' : patient_age}
                          ])

    ##print(patient_id, patient_sex, patient_size, patient_weight, study_date)
    res = res.append(new, ignore_index=True) 
    # copy and rename folders
    uper_path = os.path.abspath(os.path.join(every_one, '..'))
    print(uper_path)
    target_path = '/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/dtpa/renamed_dtpa900'
    new_folder_name = patient_id + '_' + study_date
    new_target_path = os.path.join(target_path, new_folder_name)
    folder = os.path.exists(new_target_path)
    if not folder:
        os.makedirs(new_target_path) 
        print('---New Folder---')
        print('--- ok ---') 
        for root, dirs, files in os.walk(uper_path):
            for file in files:
                src_file = os.path.join(root, file)
                shutil.copy(src_file, new_target_path)
                print(src_file)
        print('-----copy finished------')
    else:
        print(f'------The folder {new_target_path} is already exist-----')

     
print(res.head())
print(len(res))
res.to_excel('/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/all_patients_data_900.xls')

