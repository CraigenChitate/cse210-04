from falling_object import FallingObject

class Mine(FallingObject):
    """
    Mine class inherits from FallingObject class
    attributes:
        inherits super() from parent class constructor
        appearance: gives mine "x" appearance
        points: deducts 20 points when collides
    """
    def __init__(self):
        #constructor for Mine class
        super(Mine, self).__init__()
        self.appearance = "x"
        self.points = -20
