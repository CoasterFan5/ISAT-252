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

# I do not know where this is going
my = "lumberjack"
print(my[-1]) # this is allowed
print(my[0:-5]) # this is also allowed
print(my[0:100]) #this is fine
# print(my[5:3]) # this just does nothing???
# print(my[33]) # This is too far, python errors

for align, text in zip('<^>', ['left', 'center', 'right']):
    print(align, text)
    print('{0:{fill}{align}16}'.format(text, fill=align, align=align))
