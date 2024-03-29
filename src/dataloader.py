import seaborn
import pandas


df = seaborn.load_dataset('dowjones')

df.head()

df.info()

df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day

df.info()

year_avg = df.groupby(df['year'])['Price'].mean()
print(year_avg)

print("A new line")