# User inputs their first name and last name
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()

# Strip() method to remove any leading or trailing whitespace

# last name and first name combined in reverse order with a space in between
# title() method to capitalize the first letter of each name
reversed_name = f"{last_name.title()} {first_name.title()}"

# Print the reversed name
print(reversed_name)


# user input
user_input = input("Enter a number: ")

# input to integer
# input to float first, then to integer to handle cases like '3.14'
int_value = int(float(user_input))

# input to float
# The float() function converts a number or a string that represents a number to a floating-point number
float_value = float(user_input)

# input to complex
# The complex() function can take a float value and convert it to a complex number with zero imaginary part
complex_value = complex(float(user_input))

# Display the converted values
print(f"Integer value: {int_value}")
print(f"Float value: {float_value}")
print(f"Complex value: {complex_value}")

# Explanation:
# - Integer (int): Represents whole numbers without a decimal point.
# - Float (float): Represents numbers with decimal points or fractions.
# - Complex (complex): Represents numbers with a real and an imaginary part (e.g., 1 + 2j).


length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is: {area}")


length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is: {area:.2f}")



# Prompt the user to enter three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Calculate the average of the three numbers
average = (num1 + num2 + num3) / 3

# Print the average using the % method for string formatting
print("The average of the three numbers is: %.2f" % average)



while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    number = float(user_input)
    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")



num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even.")
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Both numbers are odd.")
else:
    print("One number is even and the other is odd.")


num = int(input("Enter an integer: "))

binarystr = ""
octalstr = ""
hexstr = ""

for i in range(31, -1, -1):
    if num & (1 << i):
        binarystr += "1"
    else:
        binarystr += "0"

for i in range(0, 11):
    octalstr = str((num >> (3 * i)) & 7) + octalstr

hexdigits = "0123456789ABCDEF"
for i in range(7, -1, -1):
    hexdigit = (num >> (4 * i)) & 15
    hexstr += hexdigits[hexdigit]

print(f"Binary: {binarystr.lstrip('0') or '0'}")
print(f"Octal: {octalstr.lstrip('0') or '0'}")
print(f"Hexadecimal: {hexstr.lstrip('0') or '0'}")
