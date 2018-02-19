# EXERCISE:
# Write a program that reads a text file and writes its every odd line in another file.
# Line numbers starts from 0.

file_path = './Resources/01. Odd Lines/Input.txt'
output_file = 'output.txt'

with open(file_path) as lines_file:
    with open(output_file, 'w') as odd_lines_file:
        line = lines_file.readline()
        while line != '':
            line = lines_file.readline()
            odd_lines_file.write(line)
            lines_file.readline()
            '''This program works by taking the first line (number 0 - not odd) outside of the while loop.
            Then, inside the while loop, every second (odd) line is written to the output file.'''
