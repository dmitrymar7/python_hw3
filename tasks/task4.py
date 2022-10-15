# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def decimal_to_bin(num:int):
    if num == 0:
        return "0"
    result = ""
    while num > 0:
        result = str(num % 2) + result
        num //= 2
    return result

def task4():
    num = 45
    bin = decimal_to_bin(num)
    print(f"{num} => {bin}")

    num = 3
    bin = decimal_to_bin(num)
    print(f"{num} => {bin}")

    num = 2
    bin = decimal_to_bin(num)
    print(f"{num} => {bin}")

task4()