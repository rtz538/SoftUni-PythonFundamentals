# EXERCISE
# Create a function that prints the sign of an integer number n.


def print_sign(number):
    if number > 0:
        print("The number {0} is positive.".format(number))
    elif number < 0:
        print("The number {0} is negative.".format(number))
    else:
        print("The number {0} is zero.".format(number))


print_sign(int(input()))


# EXAMPLES
# Input
# 2
#
# Output
# The number 2 is positive.
#
#
# Input
# -5
#
# Output
# The number -5 is negative.
#
#
# Input
# 0
#
# Output
# The number 0 is zero.

# HINTS
# 1. Create a function with a descriptive name which should receive one parameter.
# 2. Implement the body of the function by handling different cases:
# a. If the number is greater than zero
# b. If the number is less than zero
# c. And if the number is equal to zero
# 3. Call (invoke) the newly created function.
