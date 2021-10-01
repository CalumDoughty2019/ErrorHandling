
try:
    user_input = input('Type a number: ')
    user_input_as_number = float(user_input)
    oops = user_input_as_number/0
except ValueError:
    print('You did not enter a number.')
except ZeroDivisionError:
    print('You are not allowed to divide by zero.')