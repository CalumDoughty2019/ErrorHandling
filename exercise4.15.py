def readposint():
    try:
        user_input = input('Type a positive number: ')
        user_input_as_number = int(user_input)
        #oops = user_input_as_number / 0
    except FloatingPointError:
        print('This is not a whole number')
    except ValueError:
        print('You did not enter a number.')
    except ZeroDivisionError:
        print('You are not allowed to divide by zero.')
    except RuntimeError:
        print('Another issue')
    #print(user_input)


readposint()