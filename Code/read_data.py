import pandas as pd
def read_mail_data(file_path):
    raw_mail_data = pd.read_csv(file_path)
    return raw_mail_data                    #trả về 1 dataFrame
