"""
This is where the description of your program should go. It should be at most
80 characters wide and use multiple lines if needed. Change the following
author, version, and python information, as appropriate. Note that this file uses
four spaces for block indentation.

:author Siddhartha Hiremath
:version 
:python 3.12.x

"""

# ------ import section ------
import random

# ------ main section ------
def main():
    """
	This is where the description of your function goes. Use multiple lines 
	if needed. And include the following, as
	applicable:

	Args:
		None
	
	Returns:
		None
	"""

    number = random.randint(100,999)
    
    for i in range(9):
        guess = int(input("Guess a number"))
        if guess == number:
            print('good job!')
            if input('play again? y/n')=='y':
                main()
            else:
                break
        elif guess>number:
            print('Too High')
        else:
            print('Too Low')
        if i == 8:
            print('you failed')
            print('the number was ' + str(number))
            if input('play again? y/n')=='y':
                main()
            else:
                break
    # this is where your program ends.


# ------ execution section ------
if __name__ == "__main__":
    print("Starting program...")  # this is optional
    print("=================")  # this is optional
    main()
    print("=================")  # this is optional
    print("Program finished.")  # this is optional