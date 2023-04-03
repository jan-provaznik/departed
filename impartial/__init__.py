#!/usr/bin/env python3
#
# 2021 - 2022 Jan Provaznik (jan@provaznik.pro)
#
# Partial trace and partial transposition for Kronecker representation of
# multi-partite discrete variable quantum systems.
#
# See README for detailed discussion of its operating principles.

version = '0.3.0'

# Partial trace and partial transpose.

from ._ptrace import ptrace
from ._ptranspose import ptranspose

# Utility functions.

def mask_from_index_list (index_list, nsys):
    '''
    Constructs a mask from a list of indices specifying which components
    of a kronecker-product structured matrix should be kept unaltered.

    Parameters
    ----------
    index_list : iterable
        The list of indices to carry unaltered.
    nsys : int
        The total number of components.

    Returns
    -------
    list
        Mask compatible with ptrace and ptranspose procedures.
    '''

    kset = set(index_list)
    return [
        0 if (index in kset) else 1
        for index in range(nsys)
    ]

# Module exports 

__all__ = [
    'ptrace',
    'ptranspose',
    'mask_from_index_list',
    'version'
]

