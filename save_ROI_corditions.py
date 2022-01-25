import os
from posix import listdir
import struct
import pydicom
import pandas as pd
import numpy as np
import shutil
root_path = '/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/dtpa/renamed_dtpa3'
file_list = listdir(root_path)
# print(file_list)

def Generate_ROI_csv(root_path, folder_name):
    # print(folder_name)
    file_path = os.path.join(root_path, folder_name)
    uptake_inter_val_path = os.path.join(file_path, 'Uptakeinterval001_DS.dcm')
    if os.path.exists(uptake_inter_val_path):
        # if UptakeInterval files exists, the start to load file and get useful data
        UptakeInterval_file = pydicom.read_file(uptake_inter_val_path)
        UptakeInterval_data = np.array(UptakeInterval_file.pixel_array)
        # print(f'Uptake Interval File shape : {UptakeInterval_data.shape}')
        UptakeInterval = pydicom.dcmread(uptake_inter_val_path)
        # print(folder_name)

        for roi_iter in range(0, len(UptakeInterval[0x00571001].value)):
            ROI_label = UptakeInterval[0x00571001][roi_iter][0x00571050].value
            # print(ROI_label)
            if ROI_label in ['Lt Kidney', 'Rt kidney']:
                # print(ROI_label)
                ROI_encoder_data = UptakeInterval[0x00571001][roi_iter][0x00571017].value
                # print(f'Encode:{ROI_encoder_data}')
                # check if ROI data is missing
                if ROI_encoder_data == None:
                    # if ROI encoder data is missing then print patient ID and move the patient's folder to 
                    # a new folder named by the patient ID 
                    print(f'Error: No ROI info - ID = {folder_name}, Label = {ROI_label}')
                    No_ROI_data_folder = os.path.join('/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/dtpa/no_roi_data', folder_name )
                    os.mkdir(No_ROI_data_folder)
                    shutil.move(file_path, No_ROI_data_folder)
                    break
                else:
                    lenth_of_roi_data = int(len(ROI_encoder_data)/8)
                    parameter1 = str(lenth_of_roi_data)+ 'd'
                    ROI_decoder_data = struct.unpack(parameter1, ROI_encoder_data)
                    # print(f'Patient ID {folder_name}, Label: {ROI_label}')
                    # print(f'Decoded ROI Data: {ROI_decoder_data}')
                    pts = np.array(ROI_decoder_data)
                    pts = pts.reshape(int(len(ROI_decoder_data)/2), 2)        
                    print(pts.shape)
                    print(pts)
                    cordion = pd.DataFrame(pts)
                    print(cordion)
                    save_csv_name = ROI_label + '.csv'
                    save_csv_path = os.path.join(file_path, save_csv_name)
                    cordion.to_csv(save_csv_path, index=False, header=False)
          
    else:
        print(f'File does NOT exists: Patient ID is {folder_name}')
        # if UptakeInterval file does not exists then move folder to another folder
        another_folder_path = '/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/dtpa/noUptakeIntervalfile'
        new_folder_path = os.path.join(another_folder_path, folder_name)
        os.mkdir(new_folder_path)
        shutil.move(file_path, new_folder_path)

        


for folder_name in file_list:
    Generate_ROI_csv(root_path, folder_name)

    