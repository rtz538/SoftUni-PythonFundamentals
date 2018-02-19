# EXERCISE:
# Write a program that reads a text file and writes its every odd line in another file.
# Line numbers starts from 0.

file_path = './Resources/01. Odd Lines/Input.txt'
output_file = 'output.txt'

lines = open(file_path).read().split('\n')

odd_lines = \
    [line for index, line in enumerate(lines) if index % 2 == 1]

print(*odd_lines, file=open(output_file, 'w'), sep='\n')
