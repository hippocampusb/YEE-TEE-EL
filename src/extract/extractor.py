# import nexessary packages
import pandas as pd

# extractor code
def extractor(file_path):
    df = pd.read_csv(file_path)
    return df

