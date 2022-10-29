import pyray
from point import Point

class Player:
    """
    Keeps track of the player in the game and keeps track of 
    their movement and of their current position on the screen

    attributes:
        appearance: sets the player as the "#"
        position: sets player at the center of the screen
        move_counter: allows player to move every 20 frames

    """
    def __init__(self):
        #constructor for the player class

        self.appearance = "#"
        self.position = Point(450, 300)
        self.move_counter = 0

    def move(self):
        """
        it keeps track of the player movement
        sets barrier to screen so player cannot 
        leave the confines
        
        """
        #keeps player from exiting left side of the screen
        if self.position.x == 2:
            self.position.x += 1
            return
        
        #keeps player from exiting right side of the screen
        if self.position.x == 890:
            self.position.x -= 1
            return
        
        #keeps player from exiting top side of the screen
        if self.position.y == 2:
            self.position.y += 1
            return
        
        #keeps player from exiting bottom side of the screen
        if self.position.y == 590:
            self.position.y -= 1
            return

        #if player is holding left and right it prevent movements
        if pyray.is_key_down(pyray.KEY_LEFT) and pyray.is_key_down(pyray.KEY_RIGHT):
            return

        #if player is holding left and up moves it diagonally
        if pyray.is_key_down(pyray.KEY_LEFT) and pyray.is_key_down(pyray.KEY_UP):
            if self. move_counter < 20:
                self.move_counter += 1
            else:
                self.position.x -= 1
                self.position.y -= 1
                self.move_counter = 0
            return
        
        #if player is holding left and down moves it diagonally
        if pyray.is_key_down(pyray.KEY_LEFT) and pyray.is_key_down(pyray.KEY_DOWN):
            if self. move_counter < 20:
                self.move_counter += 1
            else:
                self.position.x -= 1
                self.position.y += 1
                self.move_counter = 0
            return

        #if player is holding right and up moves it diagonally
        if pyray.is_key_down(pyray.KEY_RIGHT) and pyray.is_key_down(pyray.KEY_UP):
            if self. move_counter < 20:
                self.move_counter += 1
            else:
                self.position.x += 1
                self.position.y -= 1
                self.move_counter = 0
            return
        
        #if player is holding right and down moves it diagonally
        if pyray.is_key_down(pyray.KEY_RIGHT) and pyray.is_key_down(pyray.KEY_DOWN):
            if self. move_counter < 20:
                self.move_counter += 1
            else:
                self.position.x += 1
                self.position.y += 1
                self.move_counter = 0
            return
        
        #if player is holding up and down it prevent movements
        if pyray.is_key_down(pyray.KEY_UP) and pyray.is_key_down(pyray.KEY_DOWN):
            return

        #move left
        if pyray.is_key_down(pyray.KEY_LEFT):
            if self. move_counter < 20:
                self.move_counter += 1
            else:
                self.position.x -= 1
                self.move_counter = 0
            return
        
        #move right
        if pyray.is_key_down(pyray.KEY_RIGHT):
            if self. move_counter < 20:
                self.move_counter += 1
            else:
                self.position.x += 1
                self.move_counter = 0
            return
        
        #move up
        if pyray.is_key_down(pyray.KEY_UP):
            if self. move_counter < 20:
                self.move_counter += 1
            else:
                self.position.y -= 1
                self.move_counter = 0
            return
        
        #move down
        if pyray.is_key_down(pyray.KEY_DOWN):
            if self. move_counter < 20:
                self.move_counter += 1
            else:
                self.position.y += 1
                self.move_counter = 0
            return