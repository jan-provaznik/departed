import numpy
import impartial
import functools

#
#                           Using impartial.ptrace,
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

# (A) To retrieve the rhoA marginal from rhoABC, we would do 
#
#                       marginalA = ptrace[BC](rhoABC). 
#
# The partial trace function, impartial.ptrace, expects three arguments,
#
# (1) the density matrix (in Kronecker form) to be (partially) traced out,
# (2) list of dimensions of individual parts,
# (3) the mask specifying whether given parts will be traced out. 
#
# We use 0 to mark parts that will be kept, while 
# we use 1 to indicate the part will be traced out.

marginalA = impartial.ptrace(rhoABC, [ dim, dim, dim ], [ 0, 1, 1 ])

# Compare the marginal with the original.

diff = numpy.abs(marginalA - rhoA).max()
print('max |marginalA - rhoA| = ', diff.round(14))

# (B) Similarly, to retrieve rhoB marginal from rhoABC, we would do 
#
#                       marginalB = ptrace[AC](rhoABC). 
#
# Please note that the mask has changed in impartial.ptrace invocation.

marginalB = impartial.ptrace(rhoABC, [ dim, dim, dim ], [ 1, 0, 1 ])

# Compare the marginal with the original.

diff = numpy.abs(marginalB - rhoB).max()
print('max |marginalB - rhoB| = ', diff.round(14))

# (C) Alternatively one can use the impartial.mask_from_carry utility which,
# given a list of parts to be kept and the number of parts comprising the
# system, constructs the mask.
#
# Please note that arrays starts at zero. This means that 0 refers to the first
# system and (N - 1) to the Nth system.

marginalC = impartial.ptrace(rhoABC, [ dim, dim, dim ], 
    impartial.mask_from_carry([ 2 ], 3))

# Compare the marginal with the original.

diff = numpy.abs(marginalC - rhoC).max()
print('max |marginalC - rhoC| = ', diff.round(14))

