import os
from numpy.core.defchararray import equal
import pandas as pd
import numpy as np
from posix import listdir
import matplotlib.pyplot as plt
import matplotlib as mpl
import pydicom
from pydicom.tag import Tag
from pylab import *
import struct
import cv2
from skimage import io
UptakeInterval_file_path = '/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/dtpa/renamed_dtpa/05213375_20201228/Uptakeinterval001_DS.dcm'
UptakeInterval_file = pydicom.read_file(UptakeInterval_file_path)
UptakeInterval_data = np.array(UptakeInterval_file.pixel_array)
print(f'Uptake Interval File shape : {UptakeInterval_data.shape}')
UptakeInterval = pydicom.dcmread(UptakeInterval_file_path)
# print(UptakeInterval)
# print('------End of Metadata------')
w = UptakeInterval[0x00571001].value
print(UptakeInterval[0x00571001].value)
print(len(w))
q = UptakeInterval[0x00571001][1][0x00571050].value
print(f'Label:{q}')
p = UptakeInterval[0x00571001][1][0x00571017].value
print(f'----binary ROI {p}--------')
print(len(p))

data1 = int(len(p)/8)
parameter1 = str(data1)+ 'd'



data_float = struct.unpack(parameter1, p)
print(f'Decode:{data_float}')
mask_matrix = np.zeros((64, 64), dtype=float)
x = []
y = []
for iter in range(0,  len(data_float), 2):
    x.append(data_float[iter])
    y.append(data_float[iter+1])
pts = np.array(data_float)
pts = pts.reshape(18, 2)        
print(pts.shape)
print(pts)
cordion = pd.DataFrame(pts)
print(cordion)
cordion.to_csv('/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/test.csv', index=False, header=False)
pts = pts.reshape((-1, 1, 2))
print(pts)










'''
# cv2.fillPoly(mask_matrix,np.int32([pts]),(255, 255, 255))
# img = cv2.polylines(img, np.int32([pts]), True, c, -1, cv2.LINE_AA)
# cv2.imshow('image',mask_matrix)
# res = cv2.fillPoly(mask_matrix, ([pts]) ,[255, 255, 255])

# plt.imshow(mask_matrix, [x,y])
plt.axis('off') 
plt.margins(0, 0)

fill(x, y, 'w')
myfig = plt.gcf() # Get the current figure. If no current figure exists, a new one is created using figure().
plt.imshow(mask_matrix, aspect='equal',cmap='gray')

# io.imshow(mask_matrix)
# io.show()
# fill(x, y,'w' )
plt.show()
myfig.savefig('/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/test.png',bbox_inches ='tight', dpi = 'figure') #save myfig
# plt.imsave('/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/test.png', a)
'''