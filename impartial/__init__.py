#!/usr/bin/env python3
#
# 2021 - 2022 Jan Provaznik (jan@provaznik.pro)
#
# Partial trace and partial transposition for Kronecker representation of
# multi-partite discrete variable quantum systems.
#
# See README for discussion of the operating principles.

version = '0.2.2'

#

from ._ptrace import ptrace
from ._ptranspose import ptranspose

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
    'mask_from_carry',
    'version'
]

