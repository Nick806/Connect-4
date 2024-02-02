
import random
import time
import os
import importlib
import configparser
import keyboard
import pygame
import sys
from dotenv import load_dotenv

################################################################################
#   Settings functions
################################################################################

HEIGHT = 10
COLUMNS = 10
bots_folder = "Bots"

def retrive_config():
    global HEIGHT, COLUMNS, bots_folder

    # Load environment variables from .env file
    load_dotenv("config.env")

    # Access variables using os.getenv
    HEIGHT = int(os.getenv("height"))
    COLUMNS = int(os.getenv("columns"))
    bots_folder = os.getenv("bots_folder")


################################################################################
#   Classes
################################################################################
    
class Board:
    def __init__(self, board):
        self.board = board
        self.height = len(board)
        self.columns = len(board[0])
    
    
    def move(self, column, player):
        if column<1 or column>self.columns: return "out of range"
        if self.board[0][column-1] != 0 : return "illegal move"
        x = self.height

        while x>0:
            x-=1
            if self.board[x][column-1] == 0:
                self.board[x][column-1] = player
                return "move done"
        return "Broo, what the heellll"
    

    def __str__(self):
        string = ""
        for row in self.board:
            for item in row:
                string+= str(item)
                string+= " "
            string+= "\n"
        
        return string



################################################################################
#   GUI functions
################################################################################

def print_start():
    name = """
Connect 4!     

beta version                                                                                        by Nick806
"""
    print(name)

def input_gamemode():
    modes = """

Select a game mode [1]:

1) Human 1Vs1 gamelpay

Gamemode n°... """
    return input(modes)

def play_gamemode(gamemode):

    gamemode = int(gamemode)

    if gamemode == 1:
        gamemode1()

def select_a_bot(bots_folder, message):

    bots = list_files(bots_folder)

    for num,bot in enumerate(bots):
        print(str(num) + " - " + bot)

    index = int(input("Insert the number that correspond to the bot " + message + "..."))
    while index<0 or index>(len(bots)-1):
        print("Input non possible... retry")
        index = int(input("Insert the number that correspond to the bot " + message + "..."))

    return bots[index]

def table_to_str(table):
    string = ""
    string += str(len(table))
    string += ";"
    string += str(len(table[0]))

    for rows in table:
        for element in rows:
            string += ";"
            string += str(element)
    
    return string

def str_to_table(string):
    list = string.split(";")
    
    rows = int(list[0])
    columns = int(list[1])

    table = create_table(rows, columns, 0)

    for r in range(rows):
        for c in range(columns):
            table[r][c] = int(list[(r)*columns + c+2])
    
    return table


################################################################################
#   Pygame
################################################################################



################################################################################
#   Section with basic functions
################################################################################

def create_table(rows, columns, elements):
    """
    Creates a 2D table (list of lists) with the specified number of rows and columns,
    filling each cell with the provided elements.

    Parameters:
    - rows (int): The number of rows in the table.
    - columns (int): The number of columns in the table.
    - elements: The value to be placed in each cell of the table.

    Returns:
    - list: A 2D table represented as a list of lists.
    """
    table = [[elements for _ in range(columns)] for _ in range(rows)]
    return table

def print_table(table):
    """
    Prints the elements of a 2D table in a readable format.

    Parameters:
    - table (list): A 2D table represented as a list of lists.

    Prints:
    - Displays the elements of the table, with each row on a new line.
    """
    for row in table:
        for item in row:
            print(item, end=" ")
        print()

def count_element_in_table(table, element):
    """
    Returns the number of times an element is contained in a table.

    Parameters:
    - table (list): The table in which to count occurrences of the element.
    - element: The element to count.

    Returns:
    - int: The count of occurrences of the specified element in the table.
    """
    count = 0

    for row in table:
        count += row.count(element)

    return count


################################################################################
#   Section with different game modes
################################################################################

def gamemode1():
    print("TODO")

################################################################################
#   File management
################################################################################

def get_function(file_path, function_name):
    """
    Dynamically imports a module from a file and retrieves the specified function.

    Parameters:
    - file_path (str): The path to the Python file containing the module.
    - function_name (str): The name of the function to retrieve.

    Returns:
    - the function of the file

    If the function or module is not found, an error message is printed, and the program exits.
    """
    try:
        module_path = os.path.splitext(file_path)[0].replace(os.path.sep, '.')
        module = importlib.import_module(module_path)
        function_to_execute = getattr(module, function_name, None)

        if callable(function_to_execute):
            return function_to_execute           
        else:
            print(f'Function {function_name}() is not present in {file_path}')
            exit()
    except Exception as e:
        print(f'Error during execution of function {function_name}() in {file_path}: {e}')
        exit()

def list_files(folder):
    """
    Lists files in the specified folder.

    Parameters:
    - folder (str): The path to the folder.

    Returns:
    - list: A list of filenames in the folder.

    Note:
    - If the folder does not exist, an appropriate message is printed, and an empty list is returned.
    - Any other errors during the operation are caught, and an empty list is returned.
    """
    try:
        files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        return files
    except FileNotFoundError:
        print(f"The folder '{folder}' does not exist.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def add_line_to_file(text, full_path):

    # Open the file in append mode or create the file if it doesn't exist
    with open(full_path, 'a+') as file:
        # Move to the beginning of the file (in case it already exists)
        file.seek(0)

        # Check if the file is empty
        is_empty = not bool(file.read(1))

        # If the file is not empty, add a new line
        if not is_empty:
            file.write('\n')

        # Add the line with the input text
        file.write(text)


################################################################################
#   MAIN
################################################################################

if __name__ == "__main__":
        
    
    retrive_config()

    b = Board(create_table(5,5,0))

    print(b)

    while True:
        print(b.move(int(input()),1))

        print(b)

    exit()

    while True:

        #pygame.init()
        
        print_start()
        
        gamemode = input_gamemode()
        
        play_gamemode(gamemode)

        #pygame.quit()

        input("Pres ENTER to continue....")

    










    #print(over_possible_combination(int(input("Rows: ")), int(input("Columns: ")), [2,2,2,2,3,3,3,4,4,5]))
    
    """print(list_files("Bots"))

    file = "Bots\\NickBot.py"

    print(execute_function(file, "take_shot", create_table(10,10,"O"), SHIPS))"""

    #print(bot_directory)

    """tabella_attacco = create_table(ROWS, COLUMNS, "O")
    tabella_difesa = create_table(ROWS, COLUMNS, 0)
    navi = SHIPS

    posiziona_navi(tabella_difesa, navi)

    print_table(tabella_difesa)
    print("")

    gioco_bot(tabella_attacco, tabella_difesa, navi)

    #game(tabella_attacco, tabella_difesa)

    print_table(tabella_attacco)"""

    #loop(bot_directory)

    #print_table(generate_net(ROWS, COLUMNS, 3))
    #input("Finito")


    """
    TEST THE IMPORT LIB

    attack_table = create_table(ROWS, COLUMNS, "O")

    remaining_ships = SHIPS

    print("risultato.... " + str(execute_function("prova.py", "modifica", attack_table, remaining_ships)))

    print(remaining_ships)
    
    """


