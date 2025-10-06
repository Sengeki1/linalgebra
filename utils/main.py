class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self):
        return iter((self.x, self.y, self.z))
         
         
class Matrix3:
    def __init__(self, *args: Vector3) -> None:
        self.m = []
        self.c = []
        for vector in args:
            (x, y, z) = vector
            self.m.append([x, y, z])
    
    def add_const(self, vector: Vector3) -> None:
        (x, y, z) = vector
        self.c.append([x, y, z])