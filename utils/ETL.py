# import packages
import pandas as pd
import chardet

# create extract functions
def extract_csv(file_path):
    # to do: write docstring
    """_summary_

    Args:
        file_path (_type_): _description_

    Returns:
        _type_: _description_
    """
    # detect the encoding of the file with chardet
    with open(file_path,"rb") as f:
        result = chardet.detect(f.read())

    df = pd.read_csv(file_path, encoding=result["encoding"])

    # checks for data quality
    print(df.info)
    # check duplicates
    
    return df

# create transform functions


# EDA for data quality checks
cars_df = extract_csv("/Users/tweic/code/YEE-TEE-EL/data/Large Cars Dataset.csv")
print(type(cars_df))

# address line 2, state, postalcode,and territory have null values address line is negligible look into the others
