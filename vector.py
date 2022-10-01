import math


class Vector:

    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def get_length(self):
        length = math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
        return length


vector = Vector(x1=2, x2=6, y1=4, y2=8)
print(vector.get_length())