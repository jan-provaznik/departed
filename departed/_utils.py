# 2021 - 2023 Jan Provaznik (jan@provaznik.pro)
#
# Partial trace and transpose operations
# for matrices with a structure induced by the Kronecker product.
#
# See README for detailed discussion of its operating principles.

import operator

def mask_from_component_list (component_list, mask_width, invert = False):
    '''
    Constructs a component_mask from a list of component indices.

    By default, 1 is set for components listed in index_list and 0 for those
    unlisted. These values can be inverted by setting invert = True. 

    Parameters
    ----------
    component_list : iterable
        The list of component indices (starting from 0).
    mask_width : int
        The total number of components comprising the system.
    invert : bool
        Defines how component_list is translated into component_mask.

    Returns
    -------
    list
        Mask compatible with ptrace and ptranspose procedures.
    '''

    assert max(component_list) < mask_width

    lookup = set(component_list)
    component_mask = [ (index in lookup) for index in range(mask_width) ]

    if invert:
        component_mask = map(operator.not_, component_mask)

    return list(map(int, component_mask))

