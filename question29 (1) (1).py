import pandas as pd

df = pd.read_csv("data.csv")

filtered = df[df['age'] > 25]
grouped = df.groupby('age').mean()

print(filtered)
print(grouped)