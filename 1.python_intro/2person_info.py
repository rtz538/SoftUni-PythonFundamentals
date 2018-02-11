'''Write a Python program, which reads a person’s name, age, town and salary, and prints it back to the console \
with the following format:
“{name} is {age} years old, is from {town} and makes ${salary}”
Note: Leave floating point numbers unformatted.

Hints
To format a string, you can either use the .format() function, or a template string (f'format')'''


name = input()
age = int(input())
town = input()
salary = float(input())

print(f"{name} is {age} years old, is from {town} and makes ${salary}")

'''Examples

Input
Gosho
20
Sofia
530

Output
Gosho is 20 years old, is from Sofia and makes $530.0

Input
Pesho
22
Plovdiv
450

Output
Pesho is 22 years old, is from Plovdiv and makes $450.0
'''