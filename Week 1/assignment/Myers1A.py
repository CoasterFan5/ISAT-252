# Fahrenheit to Celsius
# Converts temperature in Fahrenheit to Celsius

def fahrenheit_to_celsius(temp):
    return round((5 / 9) * (temp - 32), 2)

if __name__ == '__main__':
    to_convert = float(input("Enter temperature in fahrenheit: "))
    print(str(to_convert), "°F is equal to", str(fahrenheit_to_celsius(to_convert)) + "°c")
