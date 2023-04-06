import numpy
import itertools
import functools

from departed import ptrace

def kron (* matrices):
    return functools.reduce(numpy.kron, matrices, 1)

def random_complex_matrix (dim):
    rho = numpy.random.rand(dim, dim) + 1j * numpy.random.rand(dim, dim)
    return rho

def test_ptrace ():

    test_cases_dim = [ 2, 3, 4 ]
    test_cases = itertools.product(range(1000), test_cases_dim)
    
    for test_round, test_dimension in test_cases:

        dim = test_dimension

        rhoA = random_complex_matrix(dim)
        rhoB = random_complex_matrix(dim)
        rhoC = random_complex_matrix(dim)

        rhoAB = kron(rhoA, rhoB)
        rhoAC = kron(rhoA, rhoC)
        rhoBC = kron(rhoB, rhoC)

        rhoABC = kron(rhoA, rhoB, rhoC)

        marginalA = ptrace(rhoABC, [ dim, dim, dim ], [ 0, 1, 1 ])
        marginalB = ptrace(rhoABC, [ dim, dim, dim ], [ 1, 0, 1 ])
        marginalC = ptrace(rhoABC, [ dim, dim, dim ], [ 1, 1, 0 ])

        assert numpy.abs(marginalA - rhoA * rhoB.trace() * rhoC.trace()).max() < 1e-8
        assert numpy.abs(marginalB - rhoB * rhoA.trace() * rhoC.trace()).max() < 1e-8
        assert numpy.abs(marginalC - rhoC * rhoA.trace() * rhoB.trace()).max() < 1e-8

        marginalAB = ptrace(rhoABC, [ dim, dim, dim ], [ 0, 0, 1 ])
        marginalAC = ptrace(rhoABC, [ dim, dim, dim ], [ 0, 1, 0 ])
        marginalBC = ptrace(rhoABC, [ dim, dim, dim ], [ 1, 0, 0 ])

        assert numpy.abs(marginalAB - rhoAB * rhoC.trace()).max() < 1e-8
        assert numpy.abs(marginalAC - rhoAC * rhoB.trace()).max() < 1e-8
        assert numpy.abs(marginalBC - rhoBC * rhoA.trace()).max() < 1e-8

