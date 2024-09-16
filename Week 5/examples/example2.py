# Example 2
# Program to print the product of a series of given numbers.

print("Please enter some numbers, and I will tell you the product")
print("When you are done, please enter a zero")
product = 1
num = float(input("Enter a number (or 0 to stop): "))
while num:
    product *= num
    num = float(input("Enter a number (or 0 to stop): "))
else:
    print(product)

# This program does not allow zeros to be multiplied which is unfortunate
