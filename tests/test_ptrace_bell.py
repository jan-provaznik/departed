import numpy

from impartial import (
    ptrace
)

# A simple predictable example with Bell state. The marginal should be a
# completely mixed state.

def test_ptrace_bell ():
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

