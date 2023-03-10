from PyPDF2 import PdfReader
import pandas as pd


# Read excel orders
def read_excel(file_path):
    df = pd.read_excel(file_path)
    return df


def get_file_paths(relative_path):
    file_names = os.listdir(relative_path)
    files_path = []

    for item in file_names:
        files_path.append(relative_path + item)

    return files_path


# Read Nuinvest brokerage notes
def extract_nuinvest_orders():
    pass


# Read Rico brokerage notes
def extract_rico_orders():
    pass
