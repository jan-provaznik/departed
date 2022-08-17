#!/usr/bin/env python3
#
# 2021 - 2022 Jan Provaznik (jan@provaznik.pro)
#
# Partial trace and partial transposition for Kronecker representation of
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

def ptrace (R, dims, mask):
    '''
    Partial trace of kronecker-product structured matrix.
    
    
    Parameters
    ----------
    R : numpy.ndarray
        Matrix to be partially traced.
    dims : iterable
        Dimensions of individual components.
    mask : iterable
        Which components should be traced out (1) and which should be kept (0).
    
    Returns
    -------
    numpy.ndarray
        Partially transposed matrix.
    '''

    import numpy
    
    dims = list(dims)
    mask = list(mask)
    
    nsys = len(dims)
    
    index_trace = [ m for m in range(nsys) if     mask[m] ]
    index_carry = [ m for m in range(nsys) if not mask[m] ]
    
    width_trace = numpy.prod([ dims[m] for m in index_trace ])
    width_carry = numpy.prod([ dims[m] for m in index_carry ])
    
    system_axes = [ (m, m + nsys) for m in range(nsys) ]
    permutation = (
        [ system_axes[m][0] for m in index_trace ] + 
        [ system_axes[m][1] for m in index_trace ] + 
        [ system_axes[m][0] for m in index_carry ] + 
        [ system_axes[m][1] for m in index_carry ]
    )
    
    return (R
        .reshape(dims + dims)
        .transpose(permutation)
        .reshape(width_trace, width_trace, width_carry, width_carry)
        .trace()
        .reshape(width_carry, width_carry)
    )

def mask_from_carry (index_carry_list, nsys):
    '''
    Constructs a mask from a list of indices specifying which components
    of a kronecker-product structured matrix should be kept unaltered.

    Parameters
    ----------
    index_carry_list : iterable
        The list of indices to carry unaltered.
    nsys : int
        The total number of components.

    Returns
    -------
    list
        Mask compatible with ptrace and ptranspose procedures.
    '''

    kset = set(index_carry_list)
    return [
        0 if (index in kset) else 1
        for index in range(nsys)
    ]

# Exports 

__all__ = [
    'ptrace',
    'ptranspose',
    'mask_from_carry'
]

