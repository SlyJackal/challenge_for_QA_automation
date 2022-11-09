#Написать функцию которая принимает список int чисел и
#возращает список уникальных чисел, без повторяющихся элементов.

def unique_nums(num_list):
    return list(set(num_list))

lst = [1, 2, 2, 2, 3, 3, 1]

print(unique_nums(lst))