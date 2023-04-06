import numpy
import itertools
import functools

from impartial import ptranspose

def kron (* matrices):
    return functools.reduce(numpy.kron, matrices, 1)

def random_complex_matrix (dim):
    rho = numpy.random.rand(dim, dim) + 1j * numpy.random.rand(dim, dim)
    return rho

def test_ptranspose ():

    test_cases_dim = [ 2, 3, 4 ]
    test_cases = itertools.product(range(1000), test_cases_dim)
    
    for test_round, test_dimension in test_cases:

        dim = test_dimension

        rhoA = random_complex_matrix(dim)
        rhoB = random_complex_matrix(dim)
        rhoC = random_complex_matrix(dim)

        rhoABC = kron(rhoA, rhoB, rhoC)

        expect_ABCptA = kron(rhoA.T, rhoB, rhoC)
        result_ABCptA = ptranspose(rhoABC, [ dim, dim, dim ], [ 1, 0, 0 ])

        expect_ABCptB = kron(rhoA, rhoB.T, rhoC)
        result_ABCptB = ptranspose(rhoABC, [ dim, dim, dim ], [ 0, 1, 0 ])

        expect_ABCptC = kron(rhoA, rhoB, rhoC.T)
        result_ABCptC = ptranspose(rhoABC, [ dim, dim, dim ], [ 0, 0, 1 ])

        assert numpy.abs(result_ABCptA - expect_ABCptA).max() < 1e-8
        assert numpy.abs(result_ABCptB - expect_ABCptB).max() < 1e-8
        assert numpy.abs(result_ABCptC - expect_ABCptC).max() < 1e-8

        expect_ABCptAB = kron(rhoA.T, rhoB.T, rhoC)
        result_ABCptAB = ptranspose(rhoABC, [ dim, dim, dim ], [ 1, 1, 0 ])

        expect_ABCptAC = kron(rhoA.T, rhoB, rhoC.T)
        result_ABCptAC = ptranspose(rhoABC, [ dim, dim, dim ], [ 1, 0, 1 ])

        expect_ABCptBC = kron(rhoA, rhoB.T, rhoC.T)
        result_ABCptBC = ptranspose(rhoABC, [ dim, dim, dim ], [ 0, 1, 1 ])

        assert numpy.abs(result_ABCptAB - expect_ABCptAB).max() < 1e-8
        assert numpy.abs(result_ABCptAC - expect_ABCptAC).max() < 1e-8
        assert numpy.abs(result_ABCptBC - expect_ABCptBC).max() < 1e-8

