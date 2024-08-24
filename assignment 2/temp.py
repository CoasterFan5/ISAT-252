def fahrenheit_to_celsius(temp):
    return (5 / 9) * (temp - 32)


to_convert = float(input("Enter temperature in fahrenheit:"))
print("" + str(to_convert) + "°F is equal to " + str(fahrenheit_to_celsius(to_convert)) + "°c")
