# EXERCISE:
# Write a program that reads the contents of two text files and merges them together into a third one.

file_one = './Resources/03. Merge Files/FileOne.txt'
file_two = './Resources/03. Merge Files/FileTwo.txt'
output_file = 'output.txt'

with open(file_one) as firstfile:
    with open(file_two) as secondfile:
        list1 = open(file_one).read().split('\n')
        list2 = open(file_two).read().split('\n')
        list3 = list1 + list2
        list3.sort()
        finallist = '\n'.join(list3)
        open(output_file, 'w').write(str(finallist))



# EXAMPLES:
#
# input.txt:
# 1
# 3
# 5
#
# input2.txt:
# 2
# 4
# 6
#
# output.txt:
# 1
# 2
# 3
# 4
# 5
# 6
