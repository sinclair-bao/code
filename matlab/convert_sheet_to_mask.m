clc;
clear;
close all;

root_path = '/Users/sinclair/100-Learning/160-project/Works/Baoshanlei/DTPA/dtpa/renamed_dtpa3';
file_list = dir(root_path);

% iter every folder in target file path
for iter_of_patient = 4:length(file_list)
    close all;
    patient_id_and_study_date = file_list(iter_of_patient).name;
    zeros_mask = zeros(64);
    imshow(zeros_mask)
    Rt_data = strcat(root_path, '/', patient_id_and_study_date, '/', 'Rt kidney.csv');
    if exist(Rt_data, 'file')
        load_Rt_data = csvread(Rt_data);
        Rt_data_x = load_Rt_data(:,1);
        Rt_data_y = load_Rt_data(:,2);
    end
    hold on;
    plot(Rt_data_x,Rt_data_y)
    fill(Rt_data_x,Rt_data_y,'w')
    h=getframe;
    pathname = strcat(root_path, '/', patient_id_and_study_date, '/');
    new_file_name = strcat(pathname,'ROI_R.png');
    imwrite(h.cdata,new_file_name)
    %hold on;
%     figure;
%     close all
%     imshow(zeros_mask)
%     hold on;
%     Lt_data = strcat(root_path, '/', patient_id_and_study_date, '/', 'Lt kidney.csv');
%     if exist(Lt_data, 'file')
%         load_Lt_data = csvread(Lt_data);
%         Lt_data_x = load_Lt_data(:,1);
%         Lt_data_y = load_Lt_data(:,2);
%     end
%     % drew ROI 
% 
%     plot(Lt_data_x, Lt_data_y)
%     fill(Lt_data_x, Lt_data_y, 'w')
%     hold on;
%     pathname = strcat(root_path, '/', patient_id_and_study_date, '/');
%     new_file_name = strcat(pathname,'ROI_L.png');
%     imwrite(h.cdata,new_file_name)
    
    
    
end