# Example 1
# Program to print the product of 7 given numbers

# for loop version
total_sum = 1
print("Enter 7 numbers and ill give you the product!")
for number_number in range(7):
    total_sum *= float(input("Enter a number: "))
print("Total Sum:", total_sum)