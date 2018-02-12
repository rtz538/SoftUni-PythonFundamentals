# EXERCISE
# Create a function that prints a blank cash receipt. \
# The function should invoke three other functions: one for printing the header, one for the body and one for the footer


def print_header():
    print(f"CASH RECEIPT\n{30 * '-'}")


def print_body():
    print(f"Charged to{20 * '_'}\nReceived by{19 * '_'}")


def print_footer():
    print(f"{30 * '-'}\n\u00A9 SoftUni")


def print_receipt():
    print_header()
    print_body()
    print_footer()


print_receipt()


# EXAMPLES:
#
# CASH RECEIPT
# ------------------------------
# Charged to____________________
# Received by___________________
# ------------------------------
# © SoftUni

# HINTS:
# 1. First create a function with no parameters for printing the header. \
# Give it a meaningful name and write the code that it will execute.
# 2. Do the same for printing the receipt body and footer.
# 3. Create a function that will call all three functions in the necessary order. \
# Again, give it a meaningful and descriptive name and write the code.
# 4. For printing "©" use Unicode "\u00A9"
# 5. Call (invoke) the first function
