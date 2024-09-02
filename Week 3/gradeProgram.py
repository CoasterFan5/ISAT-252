# Write a program in Python that calculates the letter grade for a student

grade = (float(input("Enter number grade: ")))

## Check for invalid data, this can be important
if not(0 <= grade <= 100):
    print("Grade is out of range")
    exit()

if 90 <= grade <= 100:
    print("A")
if 80 <= grade < 90:
    print("B")
if 70 <= grade < 80:
    print("C")
if 60 <= grade < 70:
    print("D")
if grade < 60:
    print("F")

# a second solution
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

