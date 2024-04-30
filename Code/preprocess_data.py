import pandas as pd
import re
#B2
''' Lam sach du lieu '''
def clean_data(raw_data):
    cleaned_data = raw_data.copy()
    cleaned_data['Message'] = cleaned_data['Message'].apply(lambda x: re.sub(r'[^\w\s]', ' ', x))
    cleaned_data['Message'] = cleaned_data['Message'].str.lower()
    return cleaned_data

''' Chia dữ liệu tập huấn: Tập huấn luyện va tap kiem thu'''
def split_data(data):
    data_randomized = data.sample(frac=1, random_state=1)   #
    training_test_index = round(len(data_randomized) * 0.8) #Tra ve chi muc cua so tap kiem thu (Tong so hang cua tap kiem thu 4458) (80 % cua data)
    training_set = data_randomized[:training_test_index].reset_index(drop=True)  #Tạo tập dữ liệu huấn luyện
    test_set = data_randomized[training_test_index:].reset_index(drop=True) #Tạo tập dữ liệu kiểm thử còn lại của DataFrame
    return training_set, test_set