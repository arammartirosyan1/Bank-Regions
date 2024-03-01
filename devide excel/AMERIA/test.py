import pandas as pd

# Step 1: Read the Excel file into a Pandas DataFrame
excel_file = "For Aram.xlsx"
df = pd.read_excel(excel_file)

# Step 2: Identify the index of the specified row
specified_row_index = 10  # Change this to the desired row index

# Step 3: Filter the DataFrame to exclude rows above the specified index
filtered_df = df.iloc[specified_row_index:]

# Step 4: Write the filtered DataFrame back to an Excel file if needed
filtered_excel_file = "Ameria.xlsx"
filtered_df.to_excel(filtered_excel_file, index=False)