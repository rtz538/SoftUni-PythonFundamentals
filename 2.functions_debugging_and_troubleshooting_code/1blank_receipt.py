def print_header():
    print('CASH RECEIPT\n' + 30 * '-')


def print_body():
    print('Charged to' + 20 * '_')
    print('Received by' + 19 * '_')


def print_footer():
    print(30 * '-' + f'\n\u00A9 SoftUni')


def print_receipt():
    print_header()
    print_body()
    print_footer()


print(print_receipt())
