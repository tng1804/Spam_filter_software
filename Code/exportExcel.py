from evaluate import evaluate_model
#B7
def exprotExcel(test_set):
    filtered_df = test_set[test_set['Category'] != test_set['predicted']]
    # Xuất ra file chỉ chứa ham mail
    filtered_df.to_csv('email_du_doan_sai.csv', index=True)
    print('Đã xuất file chứa các thư dự đoán sai của tập kiểm thử thành công');
