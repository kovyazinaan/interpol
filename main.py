input_str = 'hello'
output_str = ''
for char in input_str:
    if 'a' <= char <= 'z':
        output_str += chr(ord(char) - 32)
    else:
        output_str += char
print(output_str) # 'HELLO'