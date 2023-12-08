class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return(f"({self.x}, {self.y})")
    def __add__(self, other):
        result_x = self.x + other.x
        result_y = self.y + other.y
        return(Vector2D(result_x, result_y))
    def __sub__(self, other):
        result_x = self.x - other.x
        result_y = self.y - other.y
        return(Vector2D(result_x, result_y))
    def __mul__(self, scalar):
        result_x = self.x * scalar
        result_y = self.y * scalar
        return(Vector2D(result_x, result_y))