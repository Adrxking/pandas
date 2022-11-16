import pandas as pd

df = pd.read_csv('pandas/telco.csv')

# print(len(df))
# print(df.head())
# print(df.head().T)
# print(df.dtypes)
"""
Convert the column 'TotalCharges' to a numeric format, coercing errors if necessary.
"""
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'] = df['TotalCharges'].fillna(0)


"""
Change all column names to lowercase.
"""
df.columns = df.columns.str.lower()

"""
Delete the column 'customerid' from the dataset.
"""
df = df.drop(['customerid'], axis = 1)

"""
For string values change spaces to an underscore symbol.
"""
df = df.replace(regex='\\s+', value='_')

"""
Convert the column 'churn' to integer format (no - 0, yes - 1).
"""
df['churn'] = df['churn'].replace(['No', 'Yes'], [0, 1])

"""
Check for categorical columns how many different values they have.
"""
categorical = ["paymentmethod", "gender", "contract", "multiplelines", "partner", "dependents", "internetservice", "onlinesecurity", "onlinebackup", "deviceprotection", "techsupport", "streamingtv", "streamingmovies", "paperlessbilling"]
print(df[categorical].nunique()) 
