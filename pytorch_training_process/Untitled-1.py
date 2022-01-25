import os
import numpy as np
import pandas as pd
import pydicom
import shutil
import torch
import cv2
from pydicom.pixel_data_handlers.util import apply_voi_lut
import matplotlib.pyplot as plt
from torch.autograd.grad_mode import F


print(torch.__version__)
print(pydicom.__version__)

patient_img_path = r'/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/dtpa/renamed_dtpa/00109452_20201027'
research_img_name = 'Uptakeinterval001_DS.dcm'

target_img_path = os.path.join(patient_img_path, research_img_name)

# Load research image
SIZE = 64
def load_img(path, img_size=SIZE, voi_lut=True,rotate=0):
    img = pydicom.read_file(path)
    data = img.pixel_array

    if voi_lut:
        data = apply_voi_lut(img.pixel_array, img) 
    else:
        data = img.pixel_array

    if rotate> 0:
        rotate_choice = [0, cv2.ROTATE_90_CLOCKWISE, cv2.ROTATE_90_COUNTERCLOCKWISE, cv2.ROTATE_180]
        data = cv2.rotate(data, rotate_choice[rotate])
    data = cv2.resize(data, (img_size, img_size))
    return data

a = load_img(target_img_path, 64, True, 0)
print(a.shape)
plt.imshow(a)
plt.show()
b = load_img(os.path.join(patient_img_path, 'SummedImage001_DS.dcm'), 64, True, 0)
print(b.shape)
plt.imshow(b)
plt.show()
ax1 = plt.subplot(1,2,1)
plt.imshow(a)
plt.title('UptakeInterval')
ax2 = plt.subplot(1, 2, 2)
plt.imshow(b)
plt.title('SummedImage')

plt.show()