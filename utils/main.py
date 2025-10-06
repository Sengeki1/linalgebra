class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self):
        return iter((self.x, self.y, self.z))
         
         
class Matrix:
    def __init__(self, *args: Vector3) -> None:
        self.m = []
        for vector in args:
            (x, y, z) = vector
            self.m.append([x, y, z])
        print(self.m)
    
    def add_const(self, vector: Vector3) -> None:
        (x, y, z) = vector
        self.m.append([x, y, z])
        print(self.m)