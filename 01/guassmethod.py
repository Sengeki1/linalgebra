from ..utils.main import Matrix3, Vector3     

matrix = Matrix3(
    Vector3(0,  1,  3), 
    Vector3(0,  0,   2),
    Vector3(3,  1,   2),
)
const = Vector3(1, 10, 6)
matrix.add_const(const)

class GausMethod:
    def __init__(self, matrix: Matrix3):
        m_length = len(matrix.m)
        self.m = matrix.m
        self.c = matrix.c

        # swap if zeros found given the size of the matrix
        if m_length < 3:
            if self.m[0][0] < 1:
                self.swap(0, self.m[0][0])
            elif self.m[0][1] < 1:
                self.swap(1, self.m[0][1])
        else:
            for _ in range(m_length):
                for i, expr in enumerate(self.m):
                    for j, _ in enumerate(expr):
                        if self.m[i][j] == 0:
                            self.swap(i)
            
        print(f"[Matrix] - {self.m}")
        print(f"[Constants] - {self.c}")

    def swap(self, pos) -> None:
        prev_v = self.m[(pos + 1) % len(self.m)]
        prev_c = self.c[0][(pos + 1) % len(self.m)]

        if (self.m[pos] != self.m[-1]):
            self.m[(pos + 1) % len(self.m)] = self.m[pos]
            self.m[pos] = prev_v
        print(f"[{pos}] - {self.m}")
        print(f"[{pos}] - {self.c}")

        self.c[0][(pos + 1) % len(self.m)] = self.c[0][pos]
        self.c[0][pos] = prev_c

GausMethod(matrix)


