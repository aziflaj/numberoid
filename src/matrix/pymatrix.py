import math

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


# transpose matrix
def transpose(matrix):
    cols = len(matrix[0])
    trans = []

    for i in range(cols):
        temp = []
        for row in matrix:
            temp.append(row[i])
        trans.append(temp)

    return trans


# minor matrix of a matrix
def minor_matrix(matrix, row_index, col_index):
    mnr = []
    xdim = len(matrix[0])
    ydim = len(matrix)
    if xdim != ydim:
        print("You should pass a square matrix")
        return

    dim = xdim

    if row_index >= dim or col_index >= dim or row_index < 0 or col_index < 0:
        print("Invalid row or column")
        return

    for i in range(dim):
        row = []
        for j in range(dim):
            if i == col_index or j == row_index:
                continue

            row.append(matrix[i][j])

        if len(row) != 0:
            mnr.append(row)

    return mnr


def determinant(matrix):
    xdim = len(matrix)
    ydim = len(matrix[0])

    if xdim != ydim:
        print("Please enter a square matrix")
        return

    dim = xdim
    det = 0

    if dim == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    for j in range(dim):
        d = determinant(minor_matrix(matrix, 0, j))
        det += matrix[j][0] * d * math.pow(-1, j)

    return det


# inverse of matrix
def inverse(matrix):
    xdim = len(matrix)
    ydim = len(matrix[0])

    if xdim != ydim:
        print("Please enter a square matrix")
        return

    dim = xdim
    denom = determinant(matrix)

    if denom == 0:
        print("No inverse matrix")
        return

    cofactors = []  # the matrix of cofactors
    for i in range(dim):
        cofactor_row = []
        for j in range(dim):
            minor_det = determinant(minor_matrix(matrix, j, i)) * math.pow(-1, i + j)
            cofactor_row.append(minor_det)

        cofactors.append(cofactor_row)

    ct = transpose(cofactors)

    # multiply every ct item with 1/denom
    scalar_multiply(ct, 1 / denom)

    return ct


# scalar multiplication
def scalar_multiply(matrix, const):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] *= const

    return matrix


# multiplication

def multiply(A, B):
    Aj = len(A[0])
    Bi = len(B)

    if Aj != Bi:
        print("Cant multiply these matrices")
        return

    length = len(A)
    width = len(B[0])

    C = []  # product matrix

    for i in range(length):
        cRow = []  # one row of C
        for j in range(width):
            val = 0

            for a in range(Bi):
                val += A[i][a] * B[a][j]

            cRow.append(val)

        C.append(cRow)

    return C


# linear system solver
#
# This method solves a system of linear equations of the standard form Ax = b, where:
# A is the matrix of the coefficients
# x is the column vector of the variables
# b is the column vector of the results
# This method returns the x column vector's values
#

def linear_solver(A, b):
    if len(A) == 2:
        y = (b[0][0] * A[1][0] - A[0][0] * b[1][0]) / (-A[0][0] * A[1][1] + A[1][0] * A[0][1])
        x = (b[1][0] - A[1][1] * y) / A[1][0]

        return [x, y]

    return multiply(inverse(A), b)

