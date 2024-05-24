import numpy as np

def fibonacci_func(number):
    number = int(number)
    left = (1+np.sqrt(5)) / 2
    right = (1-np.sqrt(5)) / 2
    fib_num = round( (1/np.sqrt(5)) * ( ( np.power((left), number) ) - ( np.power((right), number) ) ), 0)
    return fib_num


num = input("The fibonacci number for : \n")
print(f"is {fibonacci_func(num)}")


