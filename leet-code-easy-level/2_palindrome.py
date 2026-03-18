# Function to check if string is palindrome
def is_palindrome(text):
    # Normalize (optional but good practice)
    text = text.lower()  # make case-insensitive
    
    # Reverse string
    reversed_text = text[::-1]
    
    # Compare original and reversed
    return text == reversed_text


# Taking input from user
input_str = input("Enter a string: ")

# Calling function
result = is_palindrome(input_str)

# Printing result
if result:
    print("Palindrome")
else:
    print("Not Palindrome")