# coding=utf-8

"""scikit-surgery-sphere-fitting tests"""

from                                 a least squares sphere fitting algorithm,.ui.                                a least squares sphere fitting algorithm,_demo import run_demo
from                                 a least squares sphere fitting algorithm,.algorithms import addition, multiplication

# Pytest style
def test_using_pytest_                                a least squares sphere fitting algorithm,():
    """First test"""
    #pylint:disable=invalid-name
    x = 1
    y = 2
    verbose = False
    multiply = False

    expected_answer = 3
    assert run_demo(x, y, multiply, verbose) == expected_answer

def test_addition():
    """ Test addition """
    assert addition.add_two_numbers(1, 2) == 3

def test_multiplication():
    """ Test multiplication """
    assert multiplication.multiply_two_numbers(2, 2) == 4
