import math

# Ask the user for a number
number = float(input("Enter a number: "))

# Calculations using math module
sqrt_value = math.sqrt(number)
log_value = math.log(number)
sine_value = math.sin(number)

# Display the results
print(f"Square root of {number} is: {sqrt_value}")
print(f"Natural logarithm of {number} is: {log_value}")
print(f"Sine of {number} (in radians) is: {sine_value}")
