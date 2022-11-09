#Функция принимает положительное integer число.
#Необходимо возвести в квадрат все цифры переданного числа, объединить их и вернуть int число.
def square_digits(num):
    num = str(num)
    result = str()
    for i in num:
        result = result + str(int(i) ** 2)
    return int(result)

print(square_digits(9119))