import numpy

from impartial import (
    ptrace,
    ptranspose
)

# A simple and predictable example with Bell states.
# The marginal should be a completely mixed state.

def test_bell_ptrace ():
    matrix_target = 0.5 * numpy.array([
        [ 1, 0 ],
        [ 0, 1 ]
    ])
    matrix_source = 0.5 * numpy.array([
        [ 1, 0, 0, 1 ],
        [ 0, 0, 0, 0 ],
        [ 0, 0, 0, 0 ],
        [ 1, 0, 0, 1 ],
    ])
    matrix_result = ptrace(matrix_source, [ 2, 2 ], [ 0, 1 ])

    assert numpy.abs(matrix_result - matrix_target).max() < 1e-6

# A simple and predictable example with Bell states.
# The partial transpose should be a negative matrix.

def test_bell_ptranspose ():
    matrix_source = 0.5 * numpy.array([
        [ 1, 0, 0, 1 ],
        [ 0, 0, 0, 0 ],
        [ 0, 0, 0, 0 ],
        [ 1, 0, 0, 1 ],
    ])
    matrix_result = ptranspose(matrix_source, [ 2, 2 ], [ 0, 1 ])
    matrix_mineig = numpy.linalg.eigvalsh(matrix_result).min()

    assert matrix_mineig < 0
