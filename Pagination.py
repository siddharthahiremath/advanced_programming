"""
A class that implements pagination for a list of items. Window size is the amount of items visible per page.
The current page is the page that is currently being displayed. Comments generated with AI and manually.

:author Siddhartha Hiremath
:version Spring 2025
:python 3.13.x

"""

# ------ main section ------
class Pagination:
    def __init__(self, item_list:list,  window_size:int) -> None:
        self.item_list = item_list  # Store the list of items to paginate
        try:
            self.window_size = int(window_size)  # Convert window_size to integer and store it
        except:
            print("Window size must be an integer")  # Error handling for non-integer window_size
        self.current_page = 1  # Initialize current page to first page
        self.total_pages = len(self.item_list)//self.window_size  # Calculate total number of pages
    
    def getVisibleItems(self) -> list:
        starting_splice = (self.window_size*(self.current_page-1))  # Calculate start index for current page
        ending_splice = (self.window_size*(self.current_page-1))+self.window_size  # Calculate end index for current page
        return self.item_list[starting_splice:ending_splice]  # Return items for current page
    
    def prevPage(self) -> object:
        self.current_page -=1  # Decrement current page to go to previous page
        return self  # Return self for method chaining
    
    def nextPage(self) -> object:
        self.current_page += 1  # Increment current page to go to next page
        return self  # Return self for method chaining
    
    def firstPage(self) -> object:
        self.current_page = 1  # Set current page to first page
        return self  # Return self for method chaining
    
    def lastPage(self) -> object:
        self.current_page = len(self.item_list)//self.window_size  # Set current page to last page
        return self  # Return self for method chaining
    
    def goToPage(self, page_number:int) -> object:
        try:
            self.current_page = int(page_number)  # Convert page_number to integer and set current page
            return self  # Return self for method chaining
        except:
            print("Page number must be an integer")  # Error handling for non-integer page_number
            return self  # Return self for method chaining
