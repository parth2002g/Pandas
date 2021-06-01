import pandas as pd

df = pd.read_json("data.js")

print(df.to_string())