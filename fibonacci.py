"""Написать функцию, которая возвращает заданное число Фибоначчи. Обязательно через рекурсию"""

def fibonacci(n):
    if (n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
try:
    n = int(input("Enter the number of members of the sequence:"))
except:
    print('You did not enter an integer')
else:
    print("The Fibonacci sequence:")
    for i in range(n):
        print(fibonacci(i))

