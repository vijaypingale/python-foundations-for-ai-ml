# reverse_string.py 

# Function to reverse a string
def reverse_string(text):
    reversed_text = ""  # empty string to store result
    
    # Loop through string in reverse order
    for ch in text:
        reversed_text = ch + reversed_text
    
    return reversed_text  # return reversed string


# Taking input from user
input_str = input("Enter a string: ")

# Calling function
result = reverse_string(input_str)

# Printing result
print(f"Reversed string is: {result}")

def reverse_string1(text):
    return text[::-1]   # slicing trick
# Taking input from user
input_str = input("Enter a string: ")

# Calling function
result = reverse_string1(input_str)
print(f"Reversed string is using ::abc {result}")