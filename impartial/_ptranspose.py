#!/usr/bin/env python3
#
# 2021 - 2022 Jan Provaznik (jan@provaznik.pro)
#
# Partial transposition for Kronecker representation of
# multi-partite discrete variable quantum systems.
#
# See README for discussion of its operating principles.

def ptranspose (matrix, component_dims, component_mask):
    '''
    Compute the partial transpose of a kronecker-product structured matrix.

    Parameters
    ----------
    matrix : numpy.ndarray
        Matrix to be partially transposed
    component_dims : iterable (of integers)
        Dimensions of individual components.
    component_mask : iterable (if integers)
        Specifies whether a component should be 
        transposed (1) or left unaltered (0).

    Returns
    -------
    numpy.ndarray
        Partially transposed matrix.
    '''

    dims = list(map(int, component_dims))
    mask = list(map(int, component_mask))
    nsys = len(dims)

    # Construct a look-up table for component axes.
    #
    # Tensor representation of kronecker-product structured matrix has
    # interleaved axes. 

    system_axes = [ (k, k + nsys) for k in range(nsys) ]

    # Construct a permutation vector to reorganize the tensor representation
    # so that axes of the components to be transposed are exchanged.

    permutation = (
        [ system_axes[k][mask[k]]     for k in range(nsys) ] + 
        [ system_axes[k][1 - mask[k]] for k in range(nsys) ]
    )

    # (1) Reshape the matrix representation into a tensor representation. 
    #     Note that this tensor representation has interleaved axes.
    # (2) Reorganize the tensor representation to perform the desired
    #     partial transposition.
    # (3) Reshape the resulting (transposed) tensor back into a martrix. 

    return (matrix
        .reshape(dims + dims)
        .transpose(permutation)
        .reshape(matrix.shape)
    )

