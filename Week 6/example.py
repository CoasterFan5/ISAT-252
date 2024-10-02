
def str(i):
    return ""

print(str(1) + str(2))
print(1, 2)
print("a", "b")

a = "abcabc"
b = a.upper()
print(b)

# Fact Check
print("Fact check")
print(len("asf asf asf asf".split()))

# Check if a word is a palindrome
user_input = input("Enter a string:").lower().replace(" ", "")
print("Is a palindrome" if user_input == user_input[::-1] else "Not a palindrome")