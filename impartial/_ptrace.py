#!/usr/bin/env python3
#
# 2021 - 2022 Jan Provaznik (jan@provaznik.pro)
#
# Partial trace for Kronecker representation of
# multi-partite discrete variable quantum systems.
#
# See README for discussion of the operating principles.

import numpy

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

