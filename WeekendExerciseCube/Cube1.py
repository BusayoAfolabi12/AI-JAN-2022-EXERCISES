from cube import Cube

class Big_cube(Cube):
    def __init__(self, x1, y1, z1, a):
        super().__init__(a)
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1

#BigC = Big_cube(10, 10, 0, 5)

#print(BigC.cube_vol())


class Small_cube(Cube):
    def __init__(self, x2, y2, z2, a):
        super().__init__(a)
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2

#SmallC = Small_cube(5, 5, 0, 2)

#print(SmallC.cube_vol())


#To determine the positions of the two cubes on x-axis


def intersect(self):
    pos_x1l = self.x1 - (self.a/2)        # Big_cube
    pos_x1r = self.x1 + (self.a/2)

    pos_x2l = self.x2 - (self.a/2)         #Small_cube
    pos_x2r = self.x2 + (self.a/2)

#To determine the positions of the two cubes on y-axis
    pos_y1l = self.y1 - (self.a/2)        # Big_cube
    pos_y1r = self.y1 + (self.a/2)

    pos_y2l = self.y2 - (self.a/2)         # Small cube
    pos_y2r = self.y2 + (self.a/2)

# Can we append a list using np arange for the Big_cube and Small_cube on both axis

# Then try to find intersection of between the Big_cube and Small_cube on both axis


