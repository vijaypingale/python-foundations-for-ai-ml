# sum_of_n

def sum_of_n(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum

input_n = int(input("Enter number for sum: "))
result = sum_of_n(input_n)
print(f"Sum of {input_n} is {result}")