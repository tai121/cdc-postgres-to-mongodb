import base64

# Base64-encoded string
encoded_string = "Cg=="

# Decode the Base64 string
decoded_bytes = base64.b64decode(encoded_string)

# Convert each character to its ASCII representation and concatenate
ascii_concatenated = ''.join(str(ord(char)) for char in decoded_bytes.decode("utf-8"))

# Print the concatenated ASCII values as a string
print(type(ascii_concatenated))
