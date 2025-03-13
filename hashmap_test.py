"""
This program tests an implementation of a hashmap.

:author Siddhartha Hiremath
:version Fall 2024
:python 3.13.x

"""


# ------ import section ------

from hashmap import HashMap

# ------ main section ------

def main():
    #hashmap creation
    hashmap = HashMap(3)
    #put data
    hashmap.put('apple', 1)
    hashmap.put('banana', 14)

    print(hashmap.size())
    #add more data, forcing a resize
    hashmap.put('blueberry', 2)
    print()
    #now has size of 20
    print(hashmap.size())
    #remove data
    hashmap.remove('apple')
    #get data
    print(hashmap.get('blueberry'))

# ------ execution section ------
if __name__ == "__main__":
    print("Starting program...")  # this is optional
    print("=================")  # this is optional
    main()
    print("=================")  # this is optional
    print("Program finished.")  # this is optional