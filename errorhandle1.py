import sys

#print(55/0) #will get error(division by zero)
#list2 = [1, 2, 3] #list index is out of range
#slice_list = list2[6] #
#sys.exit(0)

try:
    print("reach this")
    print(55/0)
except ZeroDivisionError:
    print("Ah cannae dae that!!")
#sys.exit(0)

user_input = input('Type a number: ')
try:
    #Try to do something that could fail.
    user_input_as_number = float(user_input)
except ValueError:
    #this will be executed if a ''ValueError'' is raised
    print('You did not enter a number')
else:
    #This will be executed if no exception got raised in the ''try'' statement.
    print('The square of your number is ', user_input_as_number**2)
finally:
    #This will be executed whether or not an exception is raised.
    print('Thank you')