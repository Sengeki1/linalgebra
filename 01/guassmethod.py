from ..utils.main import Matrix3, Vector3     

class GausMethod:
    def __init__(self, matrix: Matrix3):
        m_length = len(matrix.m)
        self.m = matrix.m
        self.c = matrix.c

        # swap if zeros found given the size of the matrix
        for _ in range(m_length):
            for i, row in enumerate(self.m):
                for j, _ in enumerate(row):
                    if self.m[i][j] == 0:
                        self.swap(i)

        # transform to echalon form
        col_index = 0
        for _ in range(m_length):
            if m_length < 3:
                r_c = [
                        self.m[0][col_index], 
                        self.m[1][col_index]
                      ]
            else:
                r_c = [
                        self.m[0][col_index], 
                        self.m[1][col_index], 
                        self.m[2][col_index]
                      ]
            
            for i, c in enumerate(r_c):
                if col_index == 0:
                
                    if c != 0 and (i == 1 or i == 2):
                        k = c / self.m[0][0]
                        f_m = [float(i) * k for i in self.m[0]]
                        self.m[i] = [x - y for x, y in zip(self.m[i], f_m)]
                        self.c[0][i] -= k * self.c[0][0]
                                            
                elif col_index == 1:
                    if c != 0 and (i == 2):
                        k = c / self.m[1][1]
                        f_m = [float(i) * k for i in self.m[1]]
                        self.m[i] = [x - y for x, y in zip(self.m[i], f_m)]
                        self.c[0][i] -= k * self.c[0][1]

            col_index += 1

        if self.m[1][1] != 1.0:
            k_ = (1.0 / self.m[1][1])
            self.m[1] = [k_ * i for i in self.m[1]]
            self.c[0][1] *= k_
        
        if m_length == 3:
            if self.m[2][2] != 1.0:
                k_ = (1.0 / self.m[2][2])
                self.m[2] = [k_ * i for i in self.m[2]]
                self.c[0][2] *= k_

        print(f"[Matrix] - {self.m}")
        print(f"[Constants] - {self.c}")

    def swap(self, pos) -> None:
        prev_v = self.m[(pos + 1) % len(self.m)]
        prev_c = self.c[0][(pos + 1) % len(self.m)]

        if (self.m[pos] != self.m[-1]):
            self.m[(pos + 1) % len(self.m)] = self.m[pos]
            self.m[pos] = prev_v

        self.c[0][(pos + 1) % len(self.m)] = self.c[0][pos]
        self.c[0][pos] = prev_c

matrix = Matrix3(
    Vector3(1,  1,  -1), 
    Vector3(2,  -1,   1)
)
const = Vector3(-2, 5, 0)
matrix.add_const(const)

GausMethod(matrix)



