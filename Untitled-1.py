def num_to_word(num):
    words = {
        0: 'ноль',        1: 'один',
        2: 'два',        3: 'три',
        4: 'четыре',        5: 'пять',
        6: 'шесть',        7: 'семь',
        8: 'восемь',        9: 'девять'
    }
    return words.get(num)

num = int(input("Введите число от 0 до 9: "))
if num in range(0, 10):
    print(num_to_word(num))
else:
    print("Некорректный ввод. Введите число от 0 до 9")














