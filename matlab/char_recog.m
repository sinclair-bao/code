%提取图像中的字符

clc;
clear;
close all;

root_path = '/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/dtpa/renamed_dtpa3';
file_list = dir(root_path);

for iter_of_patient = 4:length(file_list)
    iter_of_patient
    %load dicom image
    patient_id_and_study_date = file_list(iter_of_patient).name;
    report_image_name = strcat(patient_id_and_study_date(1:8), '001_SC.dcm');
    report_image_path = strcat(root_path, '/', patient_id_and_study_date,'/', report_image_name);
    
    if exist(report_image_path, 'file')
        dicom_info = dicominfo(report_image_path);
        [report_img, cmap] = dicomread(dicom_info);
        save_png_path_and_name = fullfile(root_path, patient_id_and_study_date,'report.png')
        imwrite(report_img,save_png_path_and_name,'png','Mode','lossless');
        img_png = imread(save_png_path_and_name);
        img_png = rgb2gray(img_png);


%          imshow(img_png, [])
%          figure;
%         [J, rect] = imcrop(report_img);
%         h=imrect;
%         p=ceil(getPosition(h));
        p = [1140, 56, 498, 705];
        a1=p(1):(p(1)+p(3));
        a2=(p(2)):p(2)+p(4);
        a=img_png(a2,a1);
%         imshow(a,[])
%         title('loss')
        savename = fullfile(root_path, patient_id_and_study_date, 'report_2.png');
        imwrite(a, savename)

    end
    
    

    
    
    
end