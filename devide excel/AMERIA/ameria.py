import pandas as pd


df = pd.read_excel("For Aram.xlsx")
for x in range(len(df.values)):
    data = [df.values[x][0]]
    if "Պայմանագրի Համար" in str(data).title():
        specified_row_index = x + 1

excel_file = "For Aram.xlsx"
df = pd.read_excel(excel_file)

filtered_df = df.iloc[specified_row_index:]

filtered_excel_file = "Ameria.xlsx"
filtered_df.to_excel(filtered_excel_file, index=False)

df = pd.read_excel("Ameria.xlsx")
x = (df.loc[4].values, df.loc[9].values, df.loc[14].values, [df.values[5][8]])
print(x)