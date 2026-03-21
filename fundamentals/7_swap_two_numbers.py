# Write a program to swap a two numbers

import random

def swap_two_numbers(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp
    print(f"After swap of two variable: num1 {num1} and num2 {num2}")
    return num1, num2

print(swap_two_numbers(8,2))
text = "Test string Good afternoon"
print(text.split()[1])

print(f"Random number using ramdon functino: {random.randint(1,50)}")