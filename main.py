# Exercice 1

# TODO: Create an integer variable named 'age' with your age

# TODO: Create a float variable named 'height' with your height in meters

# TODO: Create a string variable named 'name' with your name

# TODO: Create a boolean variable named 'is_student' and set it to True

# Print all variables and their types
# Example: print(f"Age: {age}, Type: {type(age)}")

Age = 23
Height = 1.83
Name = "Lucas"
Is_Student = "True"


print(f"Age: {Age}")
print(f"Height: {Height}")
print(f"Name: {Name}")
print(f"is_studied: {Is_Student}")

# Exercice 2

# TODO: Create two variables 'a' and 'b' with numeric values

# TODO: Perform addition, subtraction, multiplication, and division of a and b
# Print the results of each operation

# TODO: Calculate the remainder of a divided by b using the modulo operator

# TODO: Calculate a to the power of b using the exponentiation operator

a = 56
b = 94

print(f"a + b: {a + b}")
print(f"a - b: {a - b}")
print(f"a * b: {a * b}")
print(f"a / b: {a / b}")

print(f"a % b: {a % b}")

print(f"a ** b: {a ** b}")

# Exercice 3

# TODO: Create two string variables 'first_name' and 'last_name'

# TODO: Concatenate the two names to create a 'full_name' variable

# TODO: Print the full name in uppercase

# TODO: Print the length of the full name

# TODO: Create a string with multiple words and split it into a list

first_name = "Lucas"
last_name = "FOUQUET"
result = (first_name + " " + last_name).upper()
text = "Je suis étudiant chez Eugenia School"
words = text.split()

print(result)
print(len(result))
print(words)

# Exercice 4

# TODO: Convert a string containing a number to an integer

# TODO: Convert a float to an integer

# TODO: Convert an integer to a float

# TODO: Convert a number (integer or float) to a string

# Print all converted values and their new types

num_str = 93
num_int = int(num_str)

num_flt = 56.7
num_int2 = int(num_flt)

num_int3 = 49
num_flt2 = float(num_int3)

num_flt3 = 27.63
num_str2 = str(num_flt3)

# print({num_int}, type(num_int))
# print({num_int2}, type(num_int2))
# print({num_flt2}, type(num_flt2))
# print({num_str2}, type(num_str2))

# Exercice 5

# TODO: Create two boolean variables

# TODO: Perform AND, OR, and NOT operations on these variables
# Print the results

# TODO: Create two numeric variables and use comparison operators
# (>, <, >=, <=, ==, !=) to compare them
# Print the results of these comparisons

a = True
b = False

print("a AND b:", a and b)
print("a OR b:", a or b)
print("NOT a:", not a)
print("NOT b:", not b)

x = 648
y = 316

print("x > y", x > y)
print("x < y", x < y)
print("x >= y", x >= y)
print("x <= y", x <= y)
print("x == y", x == y)
print("x != y", x != y)
