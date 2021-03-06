import math
import copy


def print_matrix(matrix):
    """
    This function prettyprints a matrix
    :param matrix: The matrix to prettyprint
    """
    for i in range(len(matrix)):
        print(matrix[i])


def transpose(matrix):
    """
    This function transposes a matrix
    :param matrix: The matrix to transpose
    :return: The transposed matrix
    """
    num_cols = len(matrix[0])
    trans = []

    for i in range(num_cols):
        temp = []
        for row in matrix:
            temp.append(row[i])
        trans.append(temp)

    return trans


def minor_matrix(matrix, row_index, col_index):
    """
    This function calculates the minor of a matrix for a given row and column
    index. The matrix should be a square matrix, and the row and column
    should be positive and smaller than the width and height of the matrix.
    :param matrix: The matrix to calculate the minor
    :param row_index: The row index of the minor to calculate
    :param col_index: The column index of the minor to calculate
    :return: The minor for the given row and column
    """
    minor = matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    if num_cols != num_rows:
        raise ValueError("You should pass a square matrix")

    if row_index > num_rows or col_index > num_cols or row_index < 1 or col_index < 1:
        raise ValueError("Invalid row or column")

    # remove the specified row
    minor.pop(row_index - 1)

    # remove the specified column
    for row in minor:
        row.pop(col_index - 1)

    return minor


def determinant(matrix):
    """
    This function calculates the determinant of a square matrix.
    :param m_copy: The matrix to find the determinant
    :return: The determinant of the matrix
    """
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    if num_cols != num_rows:
        raise ValueError("You should pass a square matrix")

    dim = num_cols
    det = 0

    if dim == 1:
        return matrix[0][0]

    if dim == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return det

    for j in range(dim):
        m_copy = copy.deepcopy(matrix)
        minor = minor_matrix(m_copy, 1, j+1)
        d = determinant(minor)
        det += matrix[0][j] * d * math.pow(-1, j)

    return det


def inverse(matrix):
    """
    This function inverts a square matrix. If the matrix is not square,
    it returns nothing
    :param matrix: The matrix to invert
    :return: The inverse of the matrix passed as parameter
    """
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    if num_rows != num_cols:
        raise ValueError("You should pass a square matrix")

    dim = num_rows
    denom = determinant(matrix)

    if denom == 0:
        raise ValueError("The determinant is 0. Can't invert matrix")

    cofactors = []  # the matrix of cofactors, transposed
    for i in range(dim):
        cofactor_row = []
        for j in range(dim):
            m_copy = copy.deepcopy(matrix)
            minor = minor_matrix(m_copy, j+1, i+1)
            minor_det = determinant(minor) * math.pow(-1, i + j)
            cofactor_row.append(minor_det)

        cofactors.append(cofactor_row)

    # multiply every cofactor with 1/denom
    scalar_multiply(cofactors, 1 / denom)

    return cofactors


def scalar_multiply(matrix, const):
    """
    This function makes the scalar multiplication between a matrix and a number.
    :param matrix: The matrix to multiply
    :param const: The constant number which will multiply the matrix
    :return: The result of the multiplication
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] *= const

    return matrix


def multiply(matrix1, matrix2):
    """
    This function multiplies two matrices. In order to multiply, it makes sure
    the width of matrix1 is the same as the height of matrix2
    :param matrix1: Left matrix
    :param matrix2: Right matrix
    :return: The product matrix of the multiplication
    """

    width1 = len(matrix1[0])
    height2 = len(matrix2)

    if width1 != height2:
        raise ValueError("Can't multiply these matrices")

    length = len(matrix1)
    width = len(matrix2[0])

    product_matrix = []  # product_matrix = matrix_A * matrix_B

    for i in range(length):
        product_row = []  # one row of product_matrix
        for j in range(width):
            val = 0

            for a in range(height2):
                val += matrix1[i][a] * matrix2[a][j]

            product_row.append(val)

        product_matrix.append(product_row)

    return product_matrix


def linear_solver(coef, const):
    """
    This function solves a system of linear equations of the standard form Ax = B
    :param coef: The matrix of coefficients, A
    :param const: The matrix of constant terms, B
    :returns: A list of the solutions
    """
    if len(coef) == 2:
        y = (const[0][0] * coef[1][0] - coef[0][0] * const[1][0]) / (-coef[0][0] * coef[1][1] + coef[1][0] * coef[0][1])
        x = (const[1][0] - coef[1][1] * y) / coef[1][0]

        return [x, y]

    return multiply(inverse(coef), const)
