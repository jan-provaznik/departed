#!/usr/bin/env python3
#
# 2021 - 2022 Jan Provaznik (jan@provaznik.pro)
#
# Partial transposition for Kronecker representation of
# multi-partite discrete variable quantum systems.
#
# See README for discussion of the operating principles.

def ptranspose (R, dims, mask):
    '''
    Partial transpose of kronecker-product structured matrix.

    Parameters
    ----------
    R : numpy.ndarray
        Matrix to be partially transposed
    dims : iterable
        Dimensions of individual components.
    mask : iterable
        Which components should be transposed (1) and which should be left unaltered (0).

    Returns
    -------
    numpy.ndarray
        Partially transposed matrix.
    '''

    dims = list(dims)
    mask = list(mask)
    nsys = len(dims)

    system_axes = [ (k, k + nsys) for k in range(nsys) ]
    permutation = (
        [ system_axes[k][mask[k]]     for k in range(nsys) ] + 
        [ system_axes[k][1 - mask[k]] for k in range(nsys) ]
    )

    return (R
        .reshape(dims + dims)
        .transpose(permutation)
        .reshape(R.shape)
    )

