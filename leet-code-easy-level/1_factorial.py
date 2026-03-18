# factorial.py

def factorial_of_n(n):
    factorial_num = 1
    for i in range(1, n + 1):
        factorial_num = factorial_num * i
    return factorial_num

input = int(input("Enter number to calculate for factorial: "))

result = factorial_of_n(input)

print(f"The factorial of {input} is {result}")