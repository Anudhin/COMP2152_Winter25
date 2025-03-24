# Sample Coding Questions 01 Week 01
# Name: Anudhin Thomas

array_variable = [1, 4, 7, 9]


a, b, c, d = 1, 2, 3, 4
e = (a * c) - (b / d)

e = (a - ((b ** c) // d) + (a % c))


temperature = 32.6
print(f"The temperature today is: {temperature:.3f} degrees Celsius")

user_age = input("Please enter your age: ")
try:
    user_age = int(user_age)
    user_age += 22
    print(f"Now showing the shop items filtered by age: {user_age}")
except ValueError:
    print("Error: Please enter a valid integer for your age.")
