import src.matrix.pymatrix as pymatrix
import unittest


class TestMatrix(unittest.TestCase):
    def test_transpose_matrix(self):
        matrix = [[1, 2],
                  [3, 4]]

        transposed = [[1, 3],
                      [2, 4]]

        self.assertEqual(pymatrix.transpose(matrix), transposed)

    def test_calculate_minor_of_3x3_matrix(self):
        matrix = [[1, 2, 3],
                  [2, 4, 6],
                  [19, 3, 21]]

        minor_1x2 = [[1, 2],
                     [19, 3]]

        self.assertEqual(pymatrix.minor_matrix(matrix, 1, 2), minor_1x2)

    def test_minor_throws_value_error(self):
        matrix = [[2, 3],
                  [3, 4],
                  [4, 5]]

        self.assertRaises(ValueError, pymatrix.minor_matrix, matrix, 0, 0)

    def test_determinant_equals_0(self):
        matrix = [[1, 2, 3],
                  [2, 4, 6],
                  [19, 3, 21]]

        self.assertEqual(pymatrix.determinant(matrix), 0)

    def test_nonzero_determinant(self):
        matrix = [[1, 2, 3],
                  [2, 8, 6],
                  [19, 3, 21]]

        self.assertEqual(pymatrix.determinant(matrix), -144)

    def test_determinant_of_non_square(self):
        matrix = [[1, 2, 3],
                  [2, 4, 6],
                  [19, 3, 21],
                  [7, 7, 7]]

        self.assertRaises(ValueError, pymatrix.determinant, matrix)

    def test_inverse_of_unit_matrix(self):
        matrix = [[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]]

        self.assertEqual(pymatrix.inverse(matrix), matrix)

    def test_inverse_of_matrix(self):
        matrix = [[4, 3],
                  [3, 2]]

        inverse = [[-2, 3],
                   [3, -4]]

        self.assertEqual(pymatrix.inverse(matrix), inverse)

    def test_inverse_of_nonsquare_matrix(self):
        matrix = [[1, 2, 3],
                  [2, 4, 6],
                  [19, 3, 21],
                  [7, 7, 7]]

        self.assertRaises(ValueError, pymatrix.inverse, matrix)

    def test_inverse_of_matrix_with_zero_determinant(self):
        matrix = [[1, 2, 3],
                  [2, 4, 6],
                  [19, 3, 21]]

        self.assertRaises(ValueError, pymatrix.inverse, matrix)

    def test_scalar_multiplication(self):
        matrix = [[1, 3, 0],
                  [0, 0, 0]]

        matrix_times_9 = [[9, 27, 0],
                          [0, 0, 0]]
        self.assertEqual(pymatrix.scalar_multiply(matrix, 9), matrix_times_9)

    def test_2x2_2x2_matrix_multiplication(self):
        m1 = [[3, 5],
              [7, 8]]

        m2 = [[5, 9],
              [8, 4]]

        result = [[55, 47],
                  [99, 95]]

        self.assertEqual(pymatrix.multiply(m1, m2), result)

    def test_2x2_2x1_matrix_multiplication(self):
        m1 = [[3, 5],
              [7, 8]]

        m2 = [[5],
              [8]]

        result = [[55],
                  [99]]

        self.assertEqual(pymatrix.multiply(m1, m2), result)

    def test_2x1_2x2_matrix_multiplication(self):
        m1 = [[3, 5],
              [7, 8]]

        m2 = [[5],
              [8]]

        self.assertRaises(ValueError, pymatrix.multiply, m2, m1)

    def test_solve_system_of_linear_equations(self):
        coef = [[4, 1, -1],
                [3, 3, 0],
                [-1, 0, 3]]

        const = [[16],
                 [5],
                 [-1]]

        real_solution = [[5.25],
                         [-3.5833333333333335],
                         [1.4166666666666667]]

        solution = pymatrix.linear_solver(coef, const)
        self.assertEqual(solution, real_solution)
