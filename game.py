from pyray import *
import random
from player import Player
from score import Score
from gem import Gem
from rock import Rock
from mine import Mine

class Game:
    """
    Facilitates the game of 'Greed' and maintains the game loop.
    
    Attributes:
        player: The moveable character on screen.
        falling_objects: A list that holds many instances of FallingObjects
        score: The current ammount of points the player has accumulated
        add_object_counter: Allows game to add new FallingObject to screen every 500 frames
    """

    def __init__(self):
        """
        The constructor for the game class.
        """
        self.player = Player()
        self.falling_objects = []
        self.score = Score()
        self.add_object_counter = 0

    def start_game(self):
        """
        Begins game by opening window and maintaining game loop.
        """
        # Opens a window that is 900 pixels x 600
        # pixels with the title of "Greed".
        init_window(900, 600, "Greed")
        # The gameplay loop that runs while the window has
        # not been closed by the player.
        while not window_should_close():
            # Begin drawing and set background to black color.
            begin_drawing()
            clear_background(BLACK)
            # Check if any objects need to be removed from screen.
            self.check_object_removal()
            # Generates a random FallingObject every 500 frames,
            # with a 5% chance it is a Mine, a 55% chance it is a
            # Rock, and a 40% chance it is a Gem.
            if self.add_object_counter > 500:
                picker = random.randint(1, 100)
                if picker in range(0, 6):
                    object = Mine()
                elif picker in range(6, 61):
                    object = Rock()
                elif picker in range(61, 101):
                    object = Gem()
                # Add selected object to the list of FallingObjects.
                self.falling_objects.append(object)
                self.add_object_counter = 0
            else:
                # If 500 frames have not passes, add 1 to counter.
                self.add_object_counter += 1
            # Displays current player score in the top left corner of the screen.
            self.score.display_score()
            # Moves each FallingObject down and displays them on screen each frame.
            for object in self.falling_objects:
                object.fall()
                draw_text(object.appearance, object.position.x, object.position.y, 15, RED)
            # Accepts player input each frame and adjust position accordingly, then displays player on screen.
            self.player.move()
            draw_text(self.player.appearance, self.player.position.x, self.player.position.y, 15, WHITE)
            # Ends drawing for current frame.
            end_drawing()
        close_window()

    def check_object_removal(self):
        """
        Check each frame if a FallingObject has collided with the player,
        or left the screen.
        """
        # Check every FallingObject.
        for object in self.falling_objects:
            # Check if the object has collided with the player.
            if object.position.x in range(self.player.position.x - 8, self.player.position.x + 8):
                if object.position.y in range(self.player.position.y - 8, self.player.position.y + 8):
                    # Remove FallingObject from falling_objects list.
                    self.falling_objects.remove(object)
                    # Add object point value to player score.
                    self.score.value += object.points
            # Check if the object has left the screen.
            if object.position.y == 590:
                # Remove FallingObject from falling_objects list.
                self.falling_objects.remove(object)
