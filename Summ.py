"""Написать функцию, принимающую сколько угодно параметров (в том числе и 0) и возвращающую их сумму."""

def summa(args):
"""Function summ

Accepts any number of parameters - int args
Returns their amount - int k

"""
    k = 0
    for num in args:
        k += num
    return k
sum_list = []
sum_list = input("Input the numbers that you want to add up separated by a space. To exit, press Enter. ").split()
for i in range (len(sum_list)):
    try:
        sum_list[i] = int(sum_list[i])
    except ValueError:
        print("Invalid data format, the data will be deleted")
        sum_list[i] = 0
a = summa(sum_list)
print("Your summary: ", a)
