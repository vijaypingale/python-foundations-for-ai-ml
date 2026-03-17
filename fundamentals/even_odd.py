
number = int(input("Enter the nunber to find even or odd: "))

def findEvenOrOdd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = findEvenOrOdd(number)

print(f"Entered number {number} is : {result}")
