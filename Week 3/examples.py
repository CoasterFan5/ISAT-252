

a = 4
b = 8
c = 10

if a < b < c:
    print("b is the middle")
else:
    print("b is not the middle")

b = 3

if a < b < c:
    print("b is the middle")
else:
    print("b is not the middle")

b = 5.5
c = 4


if not (b == c or b == 5.5):
    print("test")
if not b == c or b == 5.5:
    print("test")

a = 5.5
b = 1.5
k = -3
# evaluate the following
if abs(k) > 3 or k < b - a:
    print("last check")