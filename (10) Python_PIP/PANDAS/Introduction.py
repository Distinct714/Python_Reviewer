
# PANDAS MODULE

import pandas as pd 

sales = {
    "userID" : ["HD6F", "EPA9", "BAI9"],
    "order_value" : [197.75, 208.21, 134.99]
}

# Convert to a pandas Dataframe
sales_df = pd.DataFrame(sales)
print(sales_df)

# read_csv is used to read file in the current directory.
sales_df = pd.read_csv("")
print(type(sales_df))

# head() is a dataframe method to preview or display the first five row.
# It won't work with other data types.
print(sales_df.head())

# Print the mean order_value
print(sales_df["order_value"].mean())

# Print the total value of sales
print(sales_df["order_value"].sum())