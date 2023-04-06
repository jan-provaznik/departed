# Using impartial.ptranspose, a tutorial.

import numpy
import impartial

# Peres-Horodecki criterion
#
# Bell state (|0> 0> + |1> |1>) / sqrt(2) is one of the maximally-entangled
# bipartite qubit states. According to the Peres-Horodecki criterion, its
# partial transpose is a negative matrix.

rhoAB = 0.5 * numpy.array([
    [ 1, 0, 0, 1 ], 
    [ 0, 0, 0, 0 ], 
    [ 0, 0, 0, 0 ], 
    [ 1, 0, 0, 1 ]
])

rhoABptB = impartial.ptranspose(rhoAB, [ 2, 2 ], [ 0, 1 ])
evals = numpy.linalg.eigvalsh(rhoABptB)

print('PPT', evals.min())

