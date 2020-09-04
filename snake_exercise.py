import curses # this is the library that talks to/from the screen, specifically a terminal.
import logging # logging is like leaving print(), for debugging purposes. but it goes to a file and not the screen.
import time
import sys
from random import randint

"""

Game Requirements:
Usual snake requirements
- # represents a part of the body
- @ represents the head of the snake.
- . represents a point on the screen.
- * represents a food item that the snake should eat.

if the snake touches itself, the game is over
the map/field is circular: leaving the field from the right
c
to end the game, hit ctrl+c

ncurses is a library that talks to the terminal window for you.
- screen.refresh() is like telling the terminal to display what was just called.
- it also captures keys pressed and can understand the
"""
# go to this file to see logs. see the logging call for how to add your own logging.
logging.basicConfig(filename='/tmp/snake_logs.txt')

"""
this class represents the field or map. part of what this class has to do is manage the snake.
As you can see, we're representing the field with arrays of integers. where integers from 0-4
mean something and the others don't. see icons for that.
"""
class Field:
    def __init__(self, size):
        self.size = size
        self.icons = {
            0: ' . ',
            1: ' * ',
            2: ' # ',
            3: ' & ',
        }
        self.snake_coords = []
        self._create_field()
        self.add_food()

    def add_food(self):
        """
            Add food to a random position on the field.
        """
        pass

    def food_eaten(self):
        """
            Returns True if the snake just ate the food, false otherwise.
        """
        pass
    def _clear_field(self):
        """
            clears the field from all food and snake.
        """
        pass
    def get_food_pos(self):
        """
            returns an array of len 2 representing the 2d position of the food.
        """
        pass
    def _create_field():
        """
            just set up the array for the whole
        """
        pass
"""
Snake class, this holds all the information needed to render, move, grow, and potentially kill
the snake. as you can see in the __init__ (constructor), we represent the position as a list of arrays (each
of these arrays are of length 2 to represent the position of the snake in the 2d field.
Question: how long is the snake to start and where in the screen does the snake begin?
"""
class Snake:

    def __init__(self, field):
        self.field = field
        self.direction = curses.KEY_RIGHT
        self.coords = [[0, 0], [0, 1], [0,2], [0,3]]


    def is_alive(self):
        """
            returns True if the snake is alive and False otherwise.
        """
        pass

    def set_direction(self, desired_direction):
        """
            set the direction of the snake based on the desired_direction argument.
        """
        pass

    def move():
        """
            recalculate the position of the snake based on 1 "tick" of movement.
        """
        pass

    def grow():
        """
            this function is responsible for growing the snake by 1.
        """

    def _within_bounds(self):
        """
            returns True if the snake is within the field bounds.
            return False if not.
        """
        pass

def main(screen):
    # Configure screen
    screen.timeout(0)
    # you'll want to set up the objects required for the game, maybe a snake and a field.
    while(True):
        ch = screen.getch()
        if ch != -1:
            logging.debug("the keycode that was pressed was: {}".format(ch))
            # you're doing to want more things here...
        snake.move()
        # Render field
        field.render(screen)
        screen.refresh()

if __name__ == "__main__":
    curses.wrapper(main)

