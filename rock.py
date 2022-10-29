from falling_object import FallingObject

class Rock(FallingObject):
    """
    Rock class inherits from FallingObject
    attributes:
        super() inherits from parent class constructor
        appearance: gives this class "o" appearance
        points: deducts 1 point when collides
    """
    def __init__(self):
        #constructor for Rock class
        super(Rock, self).__init__()
        self.appearance = "O"
        self.points = -1