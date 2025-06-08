# import packages
import pandas as pd

# create extract functions
def extract_csv(file_path):
    df = pd.read_csv(file_path, sep=";")
    return df
