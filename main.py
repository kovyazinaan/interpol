input_str = 'hello'
output_str = ''
for char in input_str:
    if 'a' <= char <= 'z':
        output_str += chr(ord(char) - 32)
    else:
        output_str += char
print(output_str) # 'HELLO'

# Хорошо, теперь данное решение нужно представить в виде функции.
# Его также нужно добавить отдельным файлов в репозиторий через git

# где решение в виде функции?
