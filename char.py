
# Sample Python Practice Program

# 1. Variables
name = "Anand"
age = 30

print("Name:", name)
print("Age:", age)


# 2. Function
def greet_user(name):
    return f"Hello, {name}! Welcome to Python."

print(greet_user(name))


# 3. Conditional Statements
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# 4. For Loop
print("\nNumbers from 1 to 10:")
for i in range(1, 11):
    print(i)


# 5. List
fruits = ["Apple", "Banana", "Mango"]

print("\nFruits:")
for fruit in fruits:
    print(fruit)


# 6. Dictionary
employee = {
    "id": 101,
    "name": "Anand",
    "department": "IT",
    "salary": 30000
}

print("\nEmployee Details:")
for key, value in employee.items():
    print(key, ":", value)


# 7. Exception Handling
try:
    num1 = int(input("\nEnter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Division Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Please enter valid numbers!")


# 8. Final Message
print("\nPython practice completed successfully!")
