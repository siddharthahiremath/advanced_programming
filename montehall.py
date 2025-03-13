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
import matplotlib.pyplot as plt

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
    successfulswitch = 0
    successfulstay = 0

    for i in range(1000):
        doors = ['big reward', 'small reward', 'no reward']
        random.shuffle(doors)
        selection = random.randint(0,2)
        monteshows = 3-(doors.index('big reward'))-selection
        if random.randint(0,1)==1:
            if doors[selection]== 'big reward':
                successfulstay += 1
        else:
            if doors[3-monteshows-selection]=='big reward':
                successfulswitch += 1
    print(successfulswitch)
    print(successfulstay)

    fig = plt.figure(figsize = (10, 5))
    options = ['switch','stay']
    values = [successfulswitch, successfulstay]

    plt.bar(options, values, color ='maroon', 
            width = 0.4)

    plt.xlabel("Options")
    plt.ylabel("Success rates")
    plt.title("Switch v Stay in the Monte Hall Problem")
    plt.show()

            
    # this is where your program ends.


# ------ execution section ------
if __name__ == "__main__":
    print("Starting program...")  # this is optional
    print("=================")  # this is optional
    main()
    print("=================")  # this is optional
    print("Program finished.")  # this is optional