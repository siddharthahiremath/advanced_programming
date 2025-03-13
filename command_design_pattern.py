
"""
This module implements the Command design pattern to handle text editing operations
in a document, allowing for undo/redo functionality.

The Command pattern encapsulates text operations as objects, making it possible to:
- Execute text commands (insert, delete)
- Undo previous operations
- Redo previously undone operations

The pattern consists of:
- Command (abstract base class defining the command interface)
- Concrete Commands (InsertCommand, DeleteCommand implementing specific operations) 
- Receiver (TextDocument class that performs the actual text modifications)
- Invoker (TextEditor class that maintains command history and executes commands)

AI was used to comment code.


:author Siddhartha Hiremath
:version Spring 2025
:python 3.12.x

"""
# ------ import section ------
from abc import ABC, abstractmethod

# ------ main section ------

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    def undo(self):
        pass
    @abstractmethod
    def redo(self):
        pass

class TextDocument():
    """
    A class representing a text document that can be modified through various
    text operations like insertion and deletion. The document maintains the text
    content and provides methods to manipulate it.

    Args:
        text: str - The initial text content of the document.

    Returns:
        None
    """

    def __init__(self, text:str):
        self.text = text
    def delete_text(self, start_char, end_char):
        strlist =  list(self.text)
        for i in range(end_char-start_char):
            strlist.pop(start_char)
        self.text = ''.join(strlist)
    def insert_text(self, insert_position, insert_text):
        strlist =  list(self.text)
        strlist.insert(insert_position, insert_text)
        self.text = ''.join(strlist)
    def display_text(self):
        print(self.text)
    def clear_terminal(self):
        print("\n"*100)

class DeleteText(Command):
    """
    A class representing a command to delete text from a document.

    Args:
        text_document: TextDocument - The document to perform the deletion on.
        start_char: int - The starting character index of the deletion.
        end_char: int - The ending character index of the deletion.
    Returns:
        None
    """
    def __init__(self, text_document, start_char, end_char):
        self.start_char = start_char
        self.end_char = end_char
        self.text_document = text_document
        self.previous_text = ""
    def execute(self):
        self.deleted_text = self.text_document.text[self.start_char:self.end_char]
        self.text_document.delete_text(self.start_char, self.end_char)
    def undo(self):
        self.text_document.insert_text(self.start_char, self.deleted_text)
    def redo(self):
        self.text_document.delete_text(self.start_char, self.end_char)

class InsertText(Command):
    """
    A class representing a command to insert text into a document.

    Args:
        text_document: TextDocument - The document to perform the insertion on.
        insert_position: int - The position in the document to insert the text.
        insert_text: str - The text to insert into the document.
    Returns:
        None
    """
    def __init__(self, text_document, insert_position, insert_text):
        self.insert_position = insert_position
        self.insert_text = insert_text
        self.text_document = text_document
    def execute(self):
        self.text_document.insert_text(self.insert_position, self.insert_text)
    def undo(self):
        self.text_document.delete_text(self.insert_position, self.insert_position+len(self.insert_text))
    def redo(self):
        self.text_document.insert_text(self.insert_position, self.insert_text)

class DisplayText(Command):
    def __init__(self, text_document):
        self.text_document = text_document
    def execute(self):
        self.text_document.display_text()
    def undo(self):
        self.text_document.clear_terminal()
    def redo(self):
        self.text_document.display_text()


        
class Invoker:
    """
    A class representing an invoker that manages a stack of commands.

    Args:
        None
    Returns:
        None
    """
    def __init__(self) -> None:
        self.undostack = []
        self.redostack = []
    def execute(self, command):
        command.execute()
        self.redostack.clear()
        self.undostack.append(command)
    def undo(self):
        if len(self.undostack)>0:
            last_command = self.undostack.pop()
            last_command.undo()
            self.redostack.append(last_command)
    def redo(self):
        if len(self.redochange)>0:
            last_command = self.redostack.pop()
            last_command.redo()
            self.undostack.append(last_command)

class TextEditor:
    """
    A class representing a text editor that allows users to perform text operations
    like deletion, insertion, and display. The editor maintains a text document and
    an invoker to manage command history.

    Args:
        None
    Returns:
        None
    """

    def __init__(self):
        self.textdocument = TextDocument(input("What should be your initial text? "))
        self.invoker = Invoker()
        self.hasquit = False

    def actionstep(self):
        commandnum = input("What command would you like to run? 0 for Delete, 1 for Insert, 2 for Display Text, 3 for Undo, 4 for Redo, 5 for Quit. ")
        try:
            match int(commandnum):
                case 0:
                    startint = int(input("What character number would you like to start delete from? This is noninclusive. "))
                    endint = int(input("What character number would you like to end delete at? This is inclusive. "))
                    self.invoker.execute(DeleteText(self.textdocument, startint, endint))
                case 1:
                    startint = int(input("What character number would you like to start insert from? "))
                    inserttext = input("What text would you like to insert? ")
                    self.invoker.execute(InsertText(self.textdocument, startint, inserttext))
                case 2:
                    self.invoker.execute(DisplayText(self.textdocument))
                case 3:
                    self.invoker.undo()
                case 4:
                    self.invoker.redo()
                case 5:
                    self.hasquit = True
                case default:
                    print("Invalid input, please chose a number 0-5")
        except Exception:
            print("Invalid input, please try again. ")

        if not self.hasquit:
            self.actionstep()
# ------ execution section ------

if __name__ == "__main__":
    print("Starting program...")
    print("=================")
    TextEditor().actionstep()
    print("=================")
    print("Program finished.")



        


