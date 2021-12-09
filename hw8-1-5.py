# Author: ATN 12/9/21

def to_celsius(fahrenheit):
    celsius = round((((fahrenheit) - 32) * 5/9), 2)
    return celsius

print(to_celsius(40) == 4.44)
print(to_celsius(94) == 34.44)
print(to_celsius(37) == 2.78)
