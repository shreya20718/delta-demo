dictionary={"Alice": 1, "Bob": 2, "Charlie": 3}
user=str(input("Enter a name: "))
if user in dictionary:
    print(f"{user} is {dictionary[user]} years old.")
else:
    print("student not found.")