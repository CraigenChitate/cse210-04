from pyray import *

class Score:
    """
    displays score in the top left of the screen and sets
    the text as white

    attributes:
        self.value: sets initial score at 0

    """
    def __init__(self):
        self.value = 0

    def display_score(self):
        #displays the current score
        draw_text(f"Score: {self.value}", 20, 20, 25, WHITE)

    def update_score(self, points):
        #updates the score according to objects caught
        self.value += points