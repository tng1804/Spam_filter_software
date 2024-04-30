import pandas as pd
#B3
'''Tao tu vung'''
def build_vocabulary(training_set):
    training_set['Message'] = training_set['Message'].str.split() #Tách thành danh sách các từ
    vocabulary = list(set(word for sms in training_set['Message'] for word in sms))
    '''
    # Khởi tạo một danh sách rỗng để chứa từ vựng
    vocabulary = []
    for sms in training_set['Message']:
        for word in sms:
            # Thêm từng từ vào danh sách từ vựng nếu chưa có trong danh sách
            vocabulary.append(word)
    #chuyển đổi thành một tập hợp để loại bỏ các từ trùng lặp, sau đó chuyển tập hợp trở lại thành danh sách.
    vocabulary = list(set(vocabulary))
    '''
    x=len(vocabulary)

    '''Tạo tu dien can cho bo huan luyen cua minh'''
    # Add the word count logic
    word_counts_per_sms = {unique_word: [0] * len(training_set['Message']) for unique_word in vocabulary}
    #print(word_counts_per_sms)
    for index, sms in enumerate(training_set['Message']): # duyet tung tin nhan, lấy cả chỉ số index
        for word in sms: # duyet tung tu trong tin nhan
            word_counts_per_sms[word][index] +=  1 #Tang gia tri tuong ung cua tung tu trong tu dien
    '''
    for word in vocabulary:
        counts = word_counts_per_sms[word]
        total_count = sum(counts)
        print(f"Từ '{word} xuất hiện {total_count} lần trong các tin nhan'")
    #    print(word_counts_per_sms[word])
    '''
    word_counts = pd.DataFrame(word_counts_per_sms) #Tạo ra một dataframe từ từ điển
    #print(word_counts)

    '''Noi DataFrame vua tao voi DataFrame chua tap huan luyen theo chieu ngang axis = 1'''
    training_set_clean = pd.concat([training_set, word_counts], axis=1)
    #print(training_set_clean)
    return vocabulary, word_counts_per_sms, training_set_clean,x



'''
word_counts_per_sms: Từ điển lưu số lần xuất hiện của tùng từ(wi thuộc vacobulary) trong mỗi tin nhan
word_counts_per_sms[word]: Truy cập danh sách (list) liên kết với từng từ word trong từ điển. Độ dài = sl tin nhăn HL (len())
[index]: Chọn phần tử tại vị trí index trong danh sách liên kết với từ word
+= 1: Tăng giá trị của phần tử đó lên 1.

'''