from falling_object import FallingObject

class Gem(FallingObject):
    """
    Gem class inherits from the FallingObject class
    attributes:
        inherit super() from parent class constructor
        appearance: gives the gem the "#" look
        points: adds 1 point for every "#" caught
    """
    def __init__(self):
        #constructor for gem class
        super(Gem, self).__init__()
        self.appearance = "#"
        self.points = 1
