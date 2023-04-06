# 2021 - 2023 Jan Provaznik (jan@provaznik.pro)
#
# Partial trace operation 
# for matrices with a structure induced by the Kronecker product.
#
# See README for detailed discussion of its operating principles.

import operator
import functools

def ptrace (matrix, component_dims, component_mask):
    '''
    Computes the partial trace of a matrix with a Kronecker-product structure.
    
    Parameters
    ----------
    matrix : numpy.ndarray
        The matrix to be partially traced.
    component_dims : iterable (of integers)
        Dimensions of its components.
    component_mask : iterable (of integers)
        Specifies whether a component should be 
        traced out (1, True) or left intact (0, False).
    
    Returns
    -------
    numpy.ndarray
        The marginal matrix.
    '''
    
    dims = list(map(int, component_dims))
    mask = list(map(int, map(bool, component_mask)))
    nsys = len(dims)

    # Compute indices of components that should be either 
    # traced out or carried over.
    
    index_trace = [ m for m in range(nsys) if     mask[m] ]
    index_carry = [ m for m in range(nsys) if not mask[m] ]

    # Compute bulk dimensions of the components to be either 
    # traced out or carried over.
    
    width_trace = functools.reduce(operator.mul, 
        [ dims[m] for m in index_trace ], 1)
    width_carry = functools.reduce(operator.mul, 
        [ dims[m] for m in index_carry ], 1)

    # Construct a look-up table for component axes.
    # Note that the tensor representation of a matrix with a Kronecker-product
    # structure has interleaved axes. 
    
    system_axes = [ (m, m + nsys) for m in range(nsys) ]

    # Construct a permutation vector to reorganize the tensor so that axes of
    # the components that will be traced out are placed before the components
    # to be carried over. Their original order is otherwise retained.

    permutation = (
        [ system_axes[m][0] for m in index_trace ] + 
        [ system_axes[m][1] for m in index_trace ] + 
        [ system_axes[m][0] for m in index_carry ] + 
        [ system_axes[m][1] for m in index_carry ]
    )

    # (1) Reshape the matrix representation into a tensor representation. 
    #     Note that this tensor representation has grouped axes.
    # (2) Reorganize the tensor representation so that the components to be
    #     traced out are located before the ones to be carried over.
    # (3) Reshape the tensor representation into a rank four tensor. 
    #     The first two axes are occupied by the components to be traced out.
    # (4) Compute the partial trace with numpy.trace function which uses the
    #     first two axes.
    # (5) Reshape the result into a matrix. 
    
    return (matrix
        .reshape(dims + dims)
        .transpose(permutation)
        .reshape(width_trace, width_trace, width_carry, width_carry)
        .trace()
        .reshape(width_carry, width_carry)
    )

