var1 = "Hello World!"
var2 = "Python Programming"
print("var1[0]:", var1[0])
print("var2[7]:", var2[7])
print("var2[1:5]:", var2[1:5])
print("Var1[1:]:", var1[1:])
print("Var2[:5]:", var2[:5])

line_of_text = input("enter a line of text: ")
# Solution 1
if "a" in line_of_text:
    print("s1 found @", line_of_text.find("a"))
else:
    print("Not Found")

# Solution 2
if "a" in line_of_text:
    for i in range(len(line_of_text)):
        if line_of_text[i] == "a":
            print("s2 found @", i)
else:
    print("Not Found")

# Solution 3
if "a" in line_of_text:
    for i in range(len(line_of_text)):
        if line_of_text[i] == "a":
            print("s3 found @", i)
            break
else:
    print("Not Found")