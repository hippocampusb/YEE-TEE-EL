
import src.utils.ETL as etl

extracted_df = etl.extract_csv("/Users/tweic/code/YEE-TEE-EL/data/bank.csv")
print(extracted_df.dtypes)