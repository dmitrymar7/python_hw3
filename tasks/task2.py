# 2 Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def prod_pars(lst:list):
    len_lst = len(lst) 
    if len_lst == 0:
        return list()
    lst_res = [lst[i] * lst[len_lst - 1 - i] for i in range(int(len_lst / 2 + 0.5))]
    return lst_res

def task2():
    lst = [2, 3, 4, 5, 6]
    res = prod_pars(lst)
    print(f"{lst} => {res}")

    lst = [2, 3, 5, 6]
    res = prod_pars(lst)
    print(f"{lst} => {res}")


task2()
