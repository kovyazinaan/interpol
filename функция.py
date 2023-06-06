def capitalize(input_str):
    output_str = ''
    for char in input_str:
        if 'a' <= char <= 'z':
            output_str += chr(ord(char) - 32)
        else:
            output_str += char
    return output_str
input_str = 'hello'
output_str = capitalize(input_str)
print(output_str) # 'HELLO'
