# 2021 - 2023 Jan Provaznik (jan@provaznik.pro)
#
# Partial transpose operation 
# for matrices with a structure induced by the Kronecker product.
#
# See README for detailed discussion of its operating principles.

def ptranspose (matrix, component_dims, component_mask):
    '''
    Computes the partial transpose of a matrix with a Kronecker-product structure.

    Parameters
    ----------
    matrix : numpy.ndarray
        The matrix to be partially transposed
    component_dims : iterable (of integers)
        Dimensions of its components.
    component_mask : iterable (if integers)
        Specifies whether a component should be 
        transposed (1, True) or left intact (0, False).

    Returns
    -------
    numpy.ndarray
        The partially transposed matrix.
    '''

    dims = list(map(int, component_dims))
    mask = list(map(int, map(bool, component_mask)))
    nsys = len(dims)

    # Construct a look-up table for component axes.
    # Note that the tensor representation of a matrix with a Kronecker-product
    # structure has interleaved axes. 

    system_axes = [ (k, k + nsys) for k in range(nsys) ]

    # Construct a permutation vector to reorganize the tensor so that axes of
    # the components that will be transposed are exchanged.

    permutation = (
        [ system_axes[k][mask[k]]     for k in range(nsys) ] + 
        [ system_axes[k][1 - mask[k]] for k in range(nsys) ]
    )

    # (1) Reshape the matrix representation into a tensor representation. 
    #     Note that this tensor representation has grouped axes.
    # (2) Reorganize the tensor representation to perform the desired
    #     partial transposition.
    # (3) Reshape the resulting (transposed) tensor back into a matrix. 

    return (matrix
        .reshape(dims + dims)
        .transpose(permutation)
        .reshape(matrix.shape)
    )

