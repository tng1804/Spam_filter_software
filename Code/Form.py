import tkinter as tk
from tkinter import messagebox

# Định nghĩa hàm dự đoán thư rác
def predict_spam():
    message = entry.get()  # Lấy nội dung tin nhắn từ ô nhập liệu
'''
# Thực hiện dự đoán thư rác (điều này sẽ thay thế bằng mô hình của bạn)
    is_spam = False  # Đây là giả định, bạn cần thay thế bằng quá trình dự đoán thực tế của mô hình

    # Hiển thị kết quả dự đoán
    if is_spam:
        messagebox.showinfo("Kết quả dự đoán", "Đây là thư rác!")
    else:
        messagebox.showinfo("Kết quả dự đoán", "Đây không phải là thư rác.")
'''


# Tạo cửa sổ
window = tk.Tk()
window.title("Dự đoán thư rác")

# Tạo và định vị ô nhập liệu
entry = tk.Entry(window, width=40)
entry.pack(pady=10)

# Tạo nút để thực hiện dự đoán
predict_button = tk.Button(window, text="Dự đoán", command=predict_spam)
predict_button.pack(pady=10)

# Chạy vòng lặp chính của cửa sổ
window.mainloop()