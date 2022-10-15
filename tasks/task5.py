# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

def fibonacci(n):
    
    lst = list()

    for i in range(n):
        if i == 0 or i == 1:
            lst.append(1)
            continue
        lst.append(lst[i - 1] + lst[i - 2]) 

    return lst

def nega_fibonacci(n):
    
    lst = list()

    for i in range(n):
        if i == 0:
            lst.append(1)
            continue
        elif i == 1:
            lst.append(-1)
            continue
        
        lst.append(lst[i - 2] - lst[i - 1])
        
    return lst

def result_fibonacci(n):
    lst_nega_fibonacci = nega_fibonacci(n)
    lst_fibonacci = fibonacci(n)
    lst = lst_nega_fibonacci
    lst.reverse()
    lst.append(0)
    lst.extend(lst_fibonacci)
    return lst


def task5():
    k = 8
    lst = result_fibonacci(k)
    print(f"k = {k} => {lst}")


task5()
