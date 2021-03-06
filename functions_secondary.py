# --------------- Section 3 --------------- #
# 1 | Fahrenheit to Celsius Conversion
#
# Fahrenheit is way we measure temperature and is commonly used in the United States, the Cayman Islands, and Liberia.
# The other unit of measurement is celsius. Celsius is commonly used throughout the rest of the world. Since they are
# different units of measurement, then the exact same temperature will have different values.
#
# For example, 68° fahrenheit is 20° celsius.
# https://www.google.com/search?client=firefox-b-1-d&q=68+degrees+fahrenheit+to+celsius
#
#
# To calculate celsius from fahrenheit, you use the following equation:
#   c = (f - 32) * (5/9)
#       where; f represents degrees fahrenheit
#              c represents degrees celsius
#
# Function
#   1 - Define a function that will convert a temperature in fahrenheit to celsius.
#   2 - Define a function that will convert a temperature in celsius to fahrenheit.
#   3 - Return the new temperature.
#
# Function Call
#   1 - Call both of these functions, and save the return value. Use any temperature.
#   2 - Print the old and converted temperature.
#
# EXAMPLE OUTPUT:
#   72° fahrenheit is 22.2222° celsius
#   10° celsius is 50° fahrenheit
#
# WRITE CODE BELOW
def fahrenheit_to_celcius(f):
    c = (f - 32) * (5/9)
    return c
print('75 degrees fahrenheit is',fahrenheit_to_celcius(75),'degrees fahrenheit')

def celsius_to_fahrenheit(cel):
    fer = (cel + 32) * (9/5)
    return fer
print('6 degrees celsius is',celsius_to_fahrenheit(6),'degrees fahrenheit')
print()

# 2 | Celsius to Kelvin
#
# There is another unit of measurement, called kelvin. It is closely related to celsius. In fact to convert an equation
# from Celsius to Kelvin is as thus:
#   k = c + 273.15
#   where; c represents degrees celsius
#
# Function
#   1 - Define a function that will convert a temperature in celsius to kelvin.
#   2 - Define a function that will convert a temperature in kelvin to celsius.
#   3 - Return the new temperature.
#
# Function Call
#   1 - Call both of these functions, and save the return value. Use any temperature.
#   2 - Print the old and converted temperature.
#
# EXAMPLE OUTPUT:
#   45° celsius is 318.15° kelvin
#   232° kelvin is -41.15° celsius
#
# WRITE CODE BELOW
def celsius_to_kelvin(c):
    k = c + 273.15
    return k
print('17 degrees in celsius is',celsius_to_kelvin(17), 'degrees kelvin')

def kelvin_to_celsius(k):
    c = k - 273.15
    return c
print('170 degrees in kelvin is',kelvin_to_celsius(170),'degrees celsius')

# Question: How could you use these functions to convert a temperature in fahrenheit to kelvin?

# You can use these functions to convert tempature in fahrenheit to kelvin by converting fahrenheit to celsius and then convert celsius to kelvin,