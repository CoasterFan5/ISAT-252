with open("config.txt", "w") as f:
    f.write("a\n")

with open("config.txt", "r") as f:
    content = f.read()

with open("config.txt", "a") as f:
    s = 'abc'
    for c in s:
        f.write(c)

with open("config.txt", "r") as f:
    content = f.read()
    print(content)