import pandas as pd

df = pd.read_csv("dirtydata.csv")

print(df.to_string())

"""
df.dropna(inplace = True)

print(df.to_string())

"""
"""
df.fillna(130, inplace = True)

print(df.to_string())
"""
"""
df["Calories"].fillna(130, inplace = True)
print(df.to_string())
"""
"""
x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)

print(df.to_string())
"""
"""
x = df["Calories"].median()

df["Calories"].fillna(x, inplace = True)

print(df.to_string())
"""

x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)

print(df.to_string())