from ..utils.main import Matrix, Vector3     

matrix = Matrix(
    Vector3(10, 1, -1), 
    Vector3(2, -1, 3)
)
const = Vector3(3, 4, 1)
matrix.add_const(const)



