import re
#B5
'''Do luong do chinh xac cua thu rac'''
def classify_test_set(message, parameters_spam, parameters_ham, p_spam, p_ham):
    #message = re.sub('\W', ' ', message)
    message = re.sub(r'[^\w\s]', ' ', message)
    message = message.lower().split()    #Chuyen ve chu thuong, sau do tach thanh danh sach cac tu
    p_spam_given_message = p_spam        #Ti le SL tin nhăn spam trong tong so tin nhăn traning_set
    p_ham_given_message = p_ham
    for word in message:
        if word in parameters_spam:
            #parameters_spam :Tu điển luu các Xác xuất của từ(wi) biết tin nhắn spam
            p_spam_given_message *= parameters_spam[word]
        if word in parameters_ham:
            p_ham_given_message *= parameters_ham[word]

    if p_ham_given_message > p_spam_given_message:
        return 'ham'
    elif p_spam_given_message > p_ham_given_message:
        return 'spam'
    else:
        return 'needs human classification'




    ''''
    P(spam|w1...wn) = P(spam)*P(w1|spam)*P(w2|spam)*...*P(wn|spam)
    P(ham|w1...wn) = P(ham)*P(w1|ham)*P(w2|ham)*...*P(wn|ham)
    Nếu P(spam|w1...wn) > P(ham|w1...wn) => Thư rác và ngược lại
    '''
