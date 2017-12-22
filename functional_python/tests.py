import unittest
from functional_python.currying import quadratic_formula
from functional_python.currying import curried_quadratic_formula


class QuadraticTest(unittest.TestCase):
    def test_2_answers(self):
        self.assertEqual(quadratic_formula(1, 5, 6), (-3.0, -2.0))

    def test_1_solution(self):
        self.assertEqual(quadratic_formula(1, 2, 1), -1.0)

    def test_no_solution(self):
        self.assertIsNone(quadratic_formula(1, 0, 16))

    def test_string_fails(self):
        with self.assertRaises(TypeError):
            quadratic_formula("jan","piet","klaas")


class CurriedQuadraticTest(unittest.TestCase):
    def test_2_answers(self):
        self.assertEqual(curried_quadratic_formula(1)(5)(6), (-3.0, -2.0))

    def test_1_solution(self):
        self.assertEqual(curried_quadratic_formula(1)(2)(1), -1.0)

    def test_no_solution(self):
        self.assertIsNone(curried_quadratic_formula(1)(0)(16))

    def test_string_fails(self):
        with self.assertRaises(TypeError):
            quadratic_formula("jan","piet","klaas")