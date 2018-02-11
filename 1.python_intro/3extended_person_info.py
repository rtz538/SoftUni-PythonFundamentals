'''Write a Python program, which reads information about a person in the same format as the previous problem, /
 and prints it back to the console with the following format:

Name: {name}
Age: {age}
Town: {town}
Salary: ${salary}
Age range: {ageRange}
Salary range: {salaryRange}

Format the salary to the 2nd decimal point.

The age range is as follows:
If the person is less than 18 years old, they are a “teen”
If the person is less than 70 years old, they are an “adult”
Otherwise, the person is an “elder”

The salary range is as follows:
If the salary is less than $500, it is “low”
If the salary is less than $2000, it is “medium”
Otherwise, the salary is “high”'''


name = input()
age = input()
town = input()
salary = float(input())

if int(age) < 18:
    agerange = "teen"
elif int(age) < 70:
    agerange = "adult"
else:
    agerange = "elder"

if salary < 500:
    salaryrange = "low"
elif salary < 2000:
    salaryrange = "medium"
else:
    salaryrange = "high"

print(f'Name: {name}\nAge: {age}\nTown: {town}\nSalary: ${salary:.2f}'
      f'\nAge range: {agerange}\nSalary range: {salaryrange}')


'''Examples:

Input
Gosho
20
Sofia
530

Output
Name: Gosho
Age: 20
Town: Sofia
Salary: $530.00
Age range: adult
Salary range: medium


Input
Pesho
17
Plovdiv
4500

Output
Name: Pesho
Age: 17
Town: Plovdiv
Salary: $4500.00
Age range: teen
Salary range: high

Input
Ivan
77
Montana
250

Output 
Name: Ivan
Age: 77
Town: Montana
Salary: $250.00
Age range: elder
Salary range: low'''