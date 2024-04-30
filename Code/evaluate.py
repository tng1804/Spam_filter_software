from classify_test_set import classify_test_set
#B6
def evaluate_model(test_set, parameters_spam, parameters_ham, p_spam, p_ham, vocabulary):
    '''Du doan dataset'''
    #Them cot du doan
    test_set['predicted'] = test_set['Message'].apply(
        lambda message: classify_test_set(message, parameters_spam, parameters_ham, p_spam, p_ham))
    correct = 0
    total = test_set.shape[0] #So hang trong tập kiểm thử
    #Tinh toán
    for _, row in test_set.iterrows():      #Lặp qua từng hàng của tap kiem thu; - : bỏ qua index; row chua gia tri cua tung hang
        if row['Category'] == row['predicted']:
            correct += 1

    print('Độ chính xác (Correct) :', correct)
    print('Không đúng (Incorrect) :', total - correct)
    print('Độ chính xác (Accuracy) :',(correct / total * 100),"%")
    return correct, total;
