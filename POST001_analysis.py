import os
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import pydicom

data_path = '/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/dtpa/renamed_dtpa/00109291_20190820/POST001_DS.dcm'
pre_path = '/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/dtpa/renamed_dtpa/00109291_20190820/PRESYR001_DS.dcm'
post_path = '/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/dtpa/renamed_dtpa/00109291_20190820/POSTSYR001_DS.dcm'

dicom_img = pydicom.read_file(data_path)
dicom_img_data = np.array(dicom_img.pixel_array)
dicom_img_shape = dicom_img_data.shape
print(f'The shape of POST001 {dicom_img_shape}')

pre_syr_img = pydicom.read_file(pre_path)
pre_syr_img_data = np.array(pre_syr_img.pixel_array)
pre_syr_img_data_shape = pre_syr_img_data.shape
print(f'PRE SYR image shape {pre_syr_img_data_shape}')

post_syr_img = pydicom.read_file(post_path)
post_syr_img_data = np.array(post_syr_img.pixel_array)
post_syr_img_data_shape = post_syr_img_data.shape
print(f'POST SYR image shape {post_syr_img_data_shape}')

fig = plt.figure(figsize=(16, 9))
'''
for i in range(0, 56):
    ax2 = fig.add_subplot(7, 8, i+1)  # 增加一个子图，三个参数分别表示：行数，列数，子图序号。i=0时，添加第一个子图
    plt.title("Slice-%d" % (i+1))  # 子图标题
    plt.xticks([])  # 不显示x轴标尺
    plt.yticks([])  # 显示y轴标尺
    cmap = mpl.cm.gray  # colormap设置，不特别设置时，为默认值
    #norm = mpl.colors.Normalize(vmin=0, vmax=1)  # colorbar标尺显示范围
    im1 = ax2.imshow(dicom_img_data[i,:,:],cmap=cmap)  # 将显示的数据放入子图
#plt.show()
'''

purfusion_phase_img = dicom_img_data[31:,:,:]
print(f'Prufusion Phase Image shape : {purfusion_phase_img.shape}')

phase_2_sum_image = np.sum(purfusion_phase_img, axis=0)
print(f'Sum Image shape : {phase_2_sum_image.shape}')
plt.imshow(phase_2_sum_image)
plt.show()

