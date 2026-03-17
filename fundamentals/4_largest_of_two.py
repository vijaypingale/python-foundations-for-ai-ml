# Program to find largest number from given twon numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def find_largest_number(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
    
result = find_largest_number(num1, num2)

print(f"The largest number between {num1} and {num2} is {result}")
