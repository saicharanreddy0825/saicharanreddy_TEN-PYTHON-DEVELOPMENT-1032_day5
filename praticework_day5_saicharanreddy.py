# 1. List of 5 fruits

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print("Fruits:")
for i in fruits:
    print(i)


# 2. Tuple of 3 colors

colors = ("Red", "Blue", "Green")

print("\nFirst Color:")
print(colors[0])


# 3. Dictionary with student names and marks

students = {
    "Ravi": 90,
    "Sunny": 95,
    "Kiran": 88
}

print("\nStudent Marks:")
print(students)


# 4. Set of 5 numbers

numbers = {10, 20, 30, 40, 50}

print("\nUnique Numbers:")

for i in numbers:
    print(i)


# 5. Dictionary of products and quantities

products = {
    "Laptop": 10,
    "Mouse": 20,
    "Keyboard": 15
}

print("\nStock Details:")

for i in products:
    print(i, "-", products[i])
