# Using departed.ptrace, a tutorial.

import numpy
import departed

def randrho (dim):
    rho = numpy.random.rand(dim, dim) + 1j * numpy.random.rand(dim, dim)
    rho = rho + numpy.conjugate(rho.T)
    rho = rho / rho.trace()
    return rho

# Consider a simple three-qubit system. 

dim = 2
rhoA = randrho(dim)
rhoB = randrho(dim)
rhoC = randrho(dim)

# The tensor product is realized with the Kronecker product. We get a matrix
# instead of a rank 6 tensor.

rhoABC = numpy.kron(numpy.kron(rhoA, rhoB), rhoC)

# Compute one-body marginals from rhoABC.

marginalA = departed.ptrace(rhoABC, [ dim, dim, dim ], [ 0, 1, 1 ])

# We can also use mask_from_component_list.

marginalB = departed.ptrace(rhoABC, [ dim, dim, dim ], 
    departed.mask_from_component_list([ 0, 2 ], 3))

marginalC = departed.ptrace(rhoABC, [ dim, dim, dim ], 
    departed.mask_from_component_list([ 2 ], 3, invert = True))

# Compare results

diff = numpy.abs(marginalA - rhoA).max()
print('max |marginalA - rhoA| = ', diff.round(14))

diff = numpy.abs(marginalB - rhoB).max()
print('max |marginalB - rhoB| = ', diff.round(14))

diff = numpy.abs(marginalC - rhoC).max()
print('max |marginalC - rhoC| = ', diff.round(14))

