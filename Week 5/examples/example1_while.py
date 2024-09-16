# Example 1
# Program to print the product of 7 given numbers

# While loop version
product = 1
count = 0
print("Input 7 numbers and I will give you the product")
while count < 7:
    num = float(input("Enter a number: "))
    product *= num
    count += 1
else: #this is neat
    print(product)