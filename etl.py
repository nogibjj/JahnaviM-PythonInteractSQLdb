'''Use ETL to Extract, Transform and Load Data on bad drivers'''

from mylib.extract import extract
from mylib.query import query
from mylib.transform_load import trans_load 

# Extract
extract()

# Query
query()

# Transform and Load
trans_load()
