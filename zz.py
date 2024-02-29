"""
text_file_path = 'text_file.txt'
binary_file_path = 'binary_file.bin'

# Open the text file in read mode ('r')
with open(text_file_path, 'r') as text_file:
    # Read the content of the text file
    text_content = text_file.read()

# Open the binary file in binary write mode ('wb')
with open(binary_file_path, 'wb') as binary_file:
    # Convert the text content to bytes and write it to the binary file
    binary_file.write(text_content.encode('utf-8'))
"""
"""

def text_to_binary(file_path, output_path):
    try:
        # Read text from the file
        with open(file_path, 'r') as text_file:
            text_data = text_file.read()

        # Convert text to binary data
        binary_data = bytes(text_data, 'utf-8')

        # Write binary data to a new file
        with open(output_path, 'wb') as binary_file:
            binary_file.write(binary_data)

        print("Conversion successful. Binary file saved at:", output_path)

    except FileNotFoundError:
        print("File not found.")


# Example usage
text_file_path = 'input.txt'  # Provide your text file path here
binary_file_path = 'output.bin'  # Provide the desired output binary file path here

text_to_binary("text_file.txt", "binary_file.bin")
"""



import pandas as pd


def excel_to_binary(excel_file_path, output_path):
    try:
        # Read Excel file into a DataFrame
        df = pd.read_excel(excel_file_path)

        # Serialize DataFrame to binary format
        df.to_pickle(output_path)  # Example using pickle, you can also use other formats like parquet

        print("Conversion successful. Binary file saved at:", output_path)

    except FileNotFoundError:
        print("File not found.")


# Example usage
excel_file_path = 'input.xlsx'  # Provide your Excel file path here
binary_file_path = 'output.pkl'  # Provide the desired output binary file path here

excel_to_binary("Book1.xlsx", "binary_file.bin")
