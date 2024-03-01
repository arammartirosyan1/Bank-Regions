with open('Book1.xlsx', 'rb') as file:
    text = file.read()

binary_data = b''.join(format(byte, '08b').encode() for byte in text)

with open('binary_file.bin', 'wb') as binary_file:
    binary_file.write(binary_data)
