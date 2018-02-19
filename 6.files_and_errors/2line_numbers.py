# Write a program that reads a text file and inserts line numbers in front of each of its lines. \
# The result should be written to another text file.

file_path = './Resources/01. Odd Lines/Input.txt'
output_file = 'output.txt'

lines = open(file_path).read().split('\n')

lines_with_numbers = \
    [f'{index+1}. {line}' for index, line in enumerate(lines) if line != '']

joined_lines_with_numbers = '\n'.join(lines_with_numbers)

open(output_file, 'w').write(joined_lines_with_numbers)


# EXAMPLES:
#
# Input:
# line one
# line two
# line three
#
# Output:
# 1. line one
# 2. line two
# 3. line three
