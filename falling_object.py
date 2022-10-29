import random
from point import Point

class FallingObject:
    """
        FallingObject class is parent class for gem, rock, and mine class
        sets how the ojects "fall" down the screen

        attributes:
        appearance: place holder that allows child classes to set their own appearances
        
        position: randomly populates objects into random location at top of screen
        has random x position and y position set at 0 so its top of screen
        
        points: place holder that allows child classes to set their own point values for scoring  
    
        move_counter: allows for smooth movement of player and falling objects

    """
    def __init__(self):
        #constructor for FallingObject class
        self.appearance = "0"
        self.position = Point(random.randint(2, 890), 0)
        self.points = 1
        self.move_counter = 0

    def fall(self):
        #moves the falling object down every 30 frames
        
        if self. move_counter < 30:
            self.move_counter += 1
        else:
            self.position.y += 1
            self.move_counter = 0
