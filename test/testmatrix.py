import src.matrix.pymatrix as pymatrix
import unittest


class testmatrix(unittest.TestCase):

    def test_transpose_matrix(self):
        a = [[1, 2],
             [3, 4]]
        at = [[1, 3],
              [2, 4]]

        self.assertEqual(pymatrix.transpose(a), at)

    def test_calculate_minor_of_matrix(self):
        #TODO: write this test method
        self.assertEqual(0, 1)

    def test_determinant(self):
        #TODO: write this test method
        self.assertEqual(0, 1)

    def test_inverse_of_matrix(self):
        #TODO: write this test method
        self.assertEqual(0, 1)

    def test_scalar_multiplication(self):
        #TODO: write this test method
        self.assertEqual(0, 1)

    def test_matrix_multiplication(self):
        #TODO: write this test method
        self.assertEqual(0, 1)

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
