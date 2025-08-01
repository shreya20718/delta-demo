a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

c=a+b
print("addition is",c)
c=a-b
print("substraction is",c)
c=a*b
print("multiplication is ",c)
if b != 0:
    c = a / b
    print("Division:", c)
else:
    print("Division by zero is not allowed.")
    