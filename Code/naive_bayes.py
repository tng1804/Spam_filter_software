import pandas as pd
#B4
'''Thuật toán Naive Bayes'''
def train_naive_bayes(training_set_clean, vocabulary):
    '''Tinh toan hang so dau tien'''
    # Isolating spam and ham messages first: tách dữ liệu
    spam_messages = training_set_clean[training_set_clean['Category'] == 'spam']    #chi chua cac hang co Category = spam
    ham_messages = training_set_clean[training_set_clean['Category'] == 'ham']      #chi chua cac hang co Category = ham

    # P(Spam) and P(Ham)
    p_spam = len(spam_messages) / len(training_set_clean)   # ti le SL tin nhắn spam trong tổng số tin nhắn cua training_set_clean
    p_ham = len(ham_messages) / len(training_set_clean)

    # N_Spam
    n_words_per_spam_message = spam_messages['Message'].apply(len)  #Tính toán tổng số từ trong mỗi tin nhắn của spam_messages
    n_spam = n_words_per_spam_message.sum()     #Tổng số từ trong tất cả các tin nhắn spam.
    # N_Ham
    n_words_per_ham_message = ham_messages['Message'].apply(len)    #Tính toán tổng số từ trong moi tin nhắn ham
    n_ham = n_words_per_ham_message.sum()   #Tổng số từ trong tất cả các tin nhắn ham.
    # N_Vocabulary
    n_vocabulary = len(vocabulary)  #Lay so luong tu duy nhat trong tu vung
    # Laplace smoothing
    alpha = 1   #Tham so làm mịn = 1

    '''Tính toán các tham số'''
    # Initiate parameters: Bắt đầu tham số
    parameters_spam = {unique_word: 0 for unique_word in vocabulary} #Khoi tao 1 tu dien: với các tu duy nhat trong tu vung lam key (khoa), gia tri ban dau = 0
    parameters_ham = {unique_word: 0 for unique_word in vocabulary}  #Khoi tao 1 tu dien: với các tu duy nhat trong tu vung lam khoa, gia tri ban dau = 0

    # Calculate parameters: Tính toán
    # tính toán các tham số cho mỗi từ trong từ vựng cho cả tin nhắn spam và tin nhắn ham
    for word in vocabulary:
        #N(wi|spam)
        n_word_given_spam = spam_messages[word].sum()   #Tính tổng số lần xuất hiện của từ(wi) trong tất cả các tin nhắn spam.

        # spam_messages already defined: đã đc xđ
        #P(wi|spam)
        p_word_given_spam = (n_word_given_spam + alpha) / (n_spam + alpha * n_vocabulary)   #Tính xác suất của từ khi biết tin nhắn là spam, sử dụng kỹ thuật làm mịn Laplace.
        # 'word' là một từ cụ thể và 'p_word_given_spam' là xác suất tương ứng của nó trong tin nhắn
        parameters_spam[word] = p_word_given_spam       #Lưu trữ xác suất đã tính trong từ điển parameters_spam.

        # N(wi|ham)
        n_word_given_ham = ham_messages[word].sum()     #Tính tổng số lần xuất hiện của từ(wi) trong tất cả các tin nhắn ham.
        # ham_messages already defined
        # P(wi|spam)
        p_word_given_ham = (n_word_given_ham + alpha) / (n_ham + alpha * n_vocabulary)      #Tính xác suất của từ khi biết tin nhắn là ham, sử dụng kỹ thuật làm mịn Laplace.
        parameters_ham[word] = p_word_given_ham         #Lưu trữ xác suất đã tính trong từ điển parameters_ham,

    return parameters_spam, parameters_ham, p_spam, p_ham
