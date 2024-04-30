from read_data import read_mail_data
from preprocess_data import clean_data, split_data
from build_vocab import build_vocabulary
from naive_bayes import train_naive_bayes
from evaluate import evaluate_model
from classify_test_set import classify_test_set
from exportExcel import exprotExcel

import tkinter as tk
from tkinter import messagebox

# Read data
file_path = r'C:\Python\DuDoanThuRac_Nhom1\Dataset\mail_data.csv'
raw_mail_data = read_mail_data(file_path)

# Preprocess data
cleaned_data = clean_data(raw_mail_data)
print(cleaned_data)
training_set, test_set = split_data(cleaned_data)

# Build vocabulary
vocabulary, word_counts_per_sms, training_set_clean,x = build_vocabulary(training_set)
print('Số lượng từ: ',x)

# Train Naive Bayes
parameters_spam, parameters_ham, p_spam, p_ham = train_naive_bayes(training_set_clean, vocabulary)

# Evaluate the model
print('\nĐo lường độ chính xac cua mo hình:\n')
accuracy = evaluate_model(test_set, parameters_spam, parameters_ham, p_spam, p_ham, vocabulary)
#print('Model Accuracy:', accuracy)
exprotExcel(test_set)
'''
# Example usage of classify_test_set
while True:
    # Nhập vào thư để kiểm tra từ bàn phím
    message_to_test = input("\nNhập vào thư để kiểm tra (để dừng, nhập 'exit'): ")

    # Kiểm tra điều kiện dừng
    if message_to_test.lower() == 'exit':
        print('Dừng kiểm tra.')
        break

    # Thực hiện kiểm tra
    test_result = classify_test_set(message_to_test, parameters_spam, parameters_ham, p_spam, p_ham)
    print('Test Result:', test_result)

    '''
def predict_spam():
    message = entry.get()  # Lấy nội dung tin nhắn từ ô nhập liệu
    test_result = classify_test_set(message, parameters_spam, parameters_ham, p_spam, p_ham)
    #print('Test Result:', test_result)
    # Hiển thị kết quả dự đoán
    if test_result == "spam":
        messagebox.showinfo("Kết quả dự đoán", "Đây là thư rác!")
    else:
        messagebox.showinfo("Kết quả dự đoán", "Đây không phải là thư rác.")

'''
# Thực hiện dự đoán thư rác (điều này sẽ thay thế bằng mô hình của bạn)
    is_spam = False  # Đây là giả định, bạn cần thay thế bằng quá trình dự đoán thực tế của mô hình

    # Hiển thị kết quả dự đoán
    if is_spam:
        messagebox.showinfo("Kết quả dự đoán", "Đây là thư rác!")
    else:
        messagebox.showinfo("Kết quả dự đoán", "Đây không phải là thư rác.")
'''

def update_label_text():
    correct,total = evaluate_model(test_set, parameters_spam, parameters_ham, p_spam, p_ham, vocabulary)
    correct_label.config(text="Số thư dự đoán đúng: {}".format(correct))
    incorrect = total - correct
    incorrect_label.config(text="Số thư dự đoán sai: {}".format(incorrect))
    accuracy = (correct / total * 100)
    accuracy_label.config(text="Độ chính xác: {}".format(accuracy))
# Tạo cửa sổ
window = tk.Tk()
window.title("Dự đoán thư rác")
# Tạo một biến font với kích thước chữ là 18
my_font = ("Helvetica", 18)

# Tạo label để hiển thị đánh giá mô hình
danhgia = tk.Label(window,text="ĐÁNH GIÁ MO HÌNH ", font=my_font) #
danhgia.pack()

# Tạo label để hiển thị số thư đúng
correct_label = tk.Label(window,text="Số thư dự đoán đúng: ", font=my_font) #
correct_label.pack()

# Tạo label để hiển thị số thư sai
incorrect_label = tk.Label(window, text="Số thư du đoán sai: ", font=my_font)
incorrect_label.pack()

# Tạo label để hiển thị độ chính xác
accuracy_label = tk.Label(window, text="Độ chính xác: ", font=my_font)
accuracy_label.pack()



# Đặt kích thước và vị trí của cửa sổ
window_width = 600
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


# Tạo label để
lb2 = tk.Label(window, text="Nhập thư bất kỳ để dự đoán", font=my_font)
lb2.pack()
# Tạo và định vị ô nhập liệu
entry = tk.Entry(window, width=60)
entry.pack(pady=10)

# Tạo nút để thực hiện dự đoán
predict_button = tk.Button(window, text="Dự đoán", command=predict_spam, font=my_font)
predict_button.pack(pady=10)

# Tạo một nút để cập nhật nhãn
update_button = tk.Button(window, text="Hiển thị độ chính xác của mô hình", command=update_label_text, font=my_font)
update_button.pack()

# Chạy vòng lặp chính của cửa sổ
window.mainloop()



