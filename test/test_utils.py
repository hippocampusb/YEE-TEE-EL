# import libraries
import pytest
import logging
import utils.ETLETL as etl
import pandas as pd

# test extract functions
def test_extract(file_path):
    df = etl.extract_csv(file_path)
    assert isinstance(df,pd.DataFrame)

test_extract("/Users/tweic/code/YEE-TEE-EL/data/Large Cars Dataset.csv")