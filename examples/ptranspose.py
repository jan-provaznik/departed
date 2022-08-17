import numpy
import impartial
import functools

#
#                         Using impartial.ptranspose,
#                                 a tutorial.
#

# We start by defining some useful functions.

def dag (mat):
    return numpy.conjugate(mat.T)

def kron (* matrices):
    return functools.reduce(numpy.kron, matrices, 1)

def randrho (dim):
    rho = numpy.random.rand(dim, dim) + 1j * numpy.random.rand(dim, dim)
    rho = rho + dag(rho)
    rho = rho / rho.trace()
    return rho

# Consider a simple tri-partite qubit system. 

dim = 2
rhoA = randrho(dim)
rhoB = randrho(dim)
rhoC = randrho(dim)

# The tensor product of individual density matrices is represented using 
# Kronecker product. The result is a matrix, NOT a tensor of higher order.

rhoABC = kron(rhoA, rhoB, rhoC)

# Suppose we were using actual tensor representation. We would start with
#
# rhoABC = sum(i, j, k, l, m, n) 
#          rhoABC(i, j, k, l, m, n) |i>A<|j| |k>B<l| |m>C<n|
#
# and to partially transpose with respect to some of the parts we would just
# swap the relevant indices. For example to partially transpose with respect to
# the second system, B, we would swap (k, l) indices in the coefficient,
#
# rhoABCptB = sum(i, j, k, l, m, n) 
#             rhoABC(i, j, l, k, m, n) |i>A<|j| |k>B<l| |m>C<n|.
#
# But alas we are using Kronecker representation.
#
# We can use the function, impartial.ptranspose, to achieve our goal. 
# The function expects three arguments,
# (1) the density matrix (in Kronecker form) to be partially transposed
# (2) list of dimensions of individual parts,
# (3) the mask specifying whether given parts will be transposed.

# We use 0 to mark parts that will remain unchanged, while 
# we use 1 to indicate the part will be transposed.

rhoABCptB = impartial.ptranspose(rhoABC, [ dim, dim, dim ], [ 0, 1, 0 ])

# Peres-Horodecki criterion
#
# Bell state (|0> 0> + |1> |1>) / sqrt(2) is one of the maximally entangled 
# bipartite qubit states. According to Peres-Horodecki criterion its partial
# transpose must be negative.

rhoAB = 0.5 * numpy.array([
    [ 1, 0, 0, 1 ], 
    [ 0, 0, 0, 0 ], 
    [ 0, 0, 0, 0 ], 
    [ 1, 0, 0, 1 ]
])

rhoABptB = impartial.ptranspose(rhoAB, [ 2, 2 ], [ 0, 1 ])
evals = numpy.linalg.eigvalsh(rhoABCptB)

print('PPT', evals.min())

