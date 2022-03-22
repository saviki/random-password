import random
import string


def generator(length=10, have_upper=True, have_lower=True, have_numbers=True, have_symbols=True):

    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    numbers = string.digits
    symbols = "!@#$%^&*"

    password = set()
    count = 1

    while count <= length:
        
        if have_upper and count <= length:
            password.add(random.choice(upper_letters))
            count += 1

        if have_lower and count <= length:
            password.add(random.choice(lower_letters))
            count += 1

        if have_numbers and count <= length:
            password.add(random.choice(numbers))
            count += 1

        if have_symbols and count <= length:
            password.add(random.choice(symbols))
            count += 1

    return "".join(password)


