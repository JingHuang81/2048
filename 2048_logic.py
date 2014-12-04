"""
THE FRAME OF THIS CODE IS PROVIDED BY COURSE: PRINCIPLE OF COMPUTING
            OFFERED BY RICE UNIVERSITY ON COURSERA
PLAY THE GAME HERE: http://www.codeskulptor.org/#user38_jlqzeoJR0Z_6.py

Logic part of 2048 game.
"""

import poc_2048_gui        
import simplegui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
   
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # replace with your code
    i = 0
    merged_line = line + []
    j = 0
    while j < len(line)-1:
        if merged_line[j] == 0:
             merged_line.append(merged_line.pop(j))
        if merged_line[j-1] == 0:
             merged_line.append(merged_line.pop(j-1))
        j = j + 1

    while i < len(line)-1:
        if merged_line[i] == merged_line[i+1]:
            merged_line[i] = merged_line[i] + merged_line[i+1]
            merged_line[i+1] = 0
        i = i + 1

    j = 0
    while j < len(line)-1:
        if merged_line[j] == 0:
             merged_line.append(merged_line.pop(j))
        if merged_line[j-1] == 0:
             merged_line.append(merged_line.pop(j-1))
        j = j + 1

    return merged_line


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.grid = []
        for i in range(self.grid_height):
            self.grid.append([])
            for element in range(self.grid_width):
                element = element + 0
                self.grid[i].append(0)
    
    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        self.grid = []
        for i in range(self.grid_height):
            self.grid.append([])
            for element in range(self.grid_width):
                element = element + 0
                self.grid[i].append(0)
        return self.grid
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self.grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        init_grid = str(self.grid)
        moved_grid = []
        i = 0
        row, col = 0, 0
        while i < self.grid_height or i < self.grid_width:
            if OFFSETS[direction][0] == 0:
                row = i
            if OFFSETS[direction][1] == 0:
                col = i
            if OFFSETS[direction][0] == -1:
                row = self.grid_height - 1
            if OFFSETS[direction][1] == -1:
                col = self.grid_width - 1

            while -1 < row < self.grid_height and -1 < col < self.grid_width:
                #print row,col
                moved_grid.append(self.grid[row][col])
                row = row + OFFSETS[direction][0]
                col = col + OFFSETS[direction][1]
            #print moved_grid, merge(moved_grid)
            moved_grid = merge(moved_grid)
            #print moved_grid
            while moved_grid:
                row = row - OFFSETS[direction][0]
                col = col - OFFSETS[direction][1]                
                self.grid[row][col] = moved_grid.pop()

            i = i + 1
        product = 1
        for element in self.grid:
            for i in element:
                product = product * i
        if product == 0 and str(self.grid) != init_grid:    
            self.new_tile()
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        import random
        row = random.randrange(0, self.get_grid_height())
        col = random.randrange(0, self.get_grid_width())
        while self.grid[row][col] != 0:
            row = random.randrange(0, self.get_grid_height())
            col = random.randrange(0, self.get_grid_width())
        value = random.choice([2,2,2,2,2,2,2,2,2,4])
        self.set_tile(row,col,value)
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        self.grid[row][col] = value
        #print self.grid

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        return self.grid[row][col]
 
    
poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
