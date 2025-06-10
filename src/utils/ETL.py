# import packages
import pandas as pd

# create extract functions
def extract_csv(file_path):
    df = pd.read_csv(file_path, encoding="latin1")

    # checks for data quality
    print(df.info)
    # check duplicates

    return df

# create transform functions


# EDA for data quality checks
sales_df = extract_csv("/Users/tweic/code/YEE-TEE-EL/data/Large Cars Dataset.csv")

# address line 2, state, postalcode,and territory have null values address line is negligible look into the others
