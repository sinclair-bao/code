import os
import numpy as np
import pydicom
from posix import listdir
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

def sample_image_generate(source_path, target_path):
    path = source_path
    path_target = target_path
    Uptakeinterval_does_not_exist_id = pd.DataFrame(columns=('Patient_ID', 'Study_date'))

    for each_id in (listdir(path)):
        #print(f'source patient image path : {each_id}')
        patient_img_path = os.path.join(source_path, each_id)
        print(f'patient img path : {patient_img_path}')
        pose001_path = os.path.join(patient_img_path, 'POST001_DS.dcm')
        dicom_img = pydicom.read_file(pose001_path)
        dicom_img_data = np.array(dicom_img.pixel_array)
        phase_2_img = np.sum(dicom_img_data, axis = 0)
        print(f'phase_2_image shape : {phase_2_img.shape}')
        new_path = os.path.join(path_target, each_id)
        # folder = os.path.exists(new_path)
        # if not folder:
        #     os.makedirs(new_path) 
        #     print('---New Folder---')
        #     print('--- ok ---')
        #     phase_2_img.save_as(new_path, 'phase_2_sum_img.dcm') 
        # check if Uptakeinterval001_DS.dcm is avarilable
        Uptakeinterval_DS_path = os.path.join(source_path, each_id, 'Uptakeinterval001_DS.dcm')
        file_exist = os.path.exists(Uptakeinterval_DS_path)
        if file_exist:
            pass
        else:
            new  = pd.DataFrame([{'Patient_ID' : each_id[0:8],'Study_date' : each_id[9:]}])
            Uptakeinterval_does_not_exist_id = Uptakeinterval_does_not_exist_id.append(new, ignore_index=True) 
    # print(Uptakeinterval_does_not_exist_id)
    Uptakeinterval_does_not_exist_id.to_excel('/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/dtpa/UptakeInterval_does_not_exist_id.xls')


        
    plt.imshow(phase_2_img)
    plt.show()



source_path = '/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/dtpa/renamed_dtpa'
target_path = '/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/dtpa/samples_for_fed_into_network'
sample_image_generate(source_path, target_path)