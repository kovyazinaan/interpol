def count_sort(lst):
    maximum = max(lst)
    minimum = min(lst)
    count = [0] * (maximum - minimum + 1)
    for num in lst:
        count[num - minimum] += 1
    result = []
    for i in range(len(count)):
        result += [i + minimum] * count[i]
    return result
def min_max(lst):
    sorted_lst = count_sort(lst)
    return sorted_lst[0], sorted_lst[-1]
lst = [3, 14, 1, 7, 9, 8, 11, 6, 4, 2]
print(count_sort(lst))
print(min_max(lst)) 