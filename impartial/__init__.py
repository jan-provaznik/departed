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

def mask_from_index_list (index_list, system_size, inverse = False):
    '''
    Constructs a mask from a list of indices specifying which components
    of a Kronecker-product structured matrix should be either kept unaltered.

    If inverse is set to True, the index_list instead 
    specifies components which should be modified (transposed, traced out).

    Parameters
    ----------
    index_list : iterable
        The list of indices to carry unaltered.
    system_size : int
        The total number of components.
    inverse : bool
        Inverts behavior.

    Returns
    -------
    list
        Mask compatible with ptrace and ptranspose procedures.
    '''

    target_value = 0, 1
    if inverse:
        target_value = 1, 0

    index_list_set = set(index_list)
    return [
        target_value[0] if (index in index_list_set) else target_value[1]
        for index in range(system_size)
    ]

# Module exports 

__all__ = [
    'ptrace',
    'ptranspose',
    'mask_from_index_list',
    'version'
]

