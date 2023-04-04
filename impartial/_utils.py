#!/usr/bin/env python3
#
# 2021 - 2023 Jan Provaznik (jan@provaznik.pro)

import operator

def mask_from_component_list (component_list, mask_width, set_ones = True):
    '''
    Constructs a component_mask from a list of component indices. By default 1
    set for components listed in component_list and 0 for those unlisted. 

    This logic can be inverted by setting set_ones = False. The resulting mask
    will have 0 is set for listed components and 1 for those unlisted.

    Parameters
    ----------
    component_list : iterable
        The list of indices to carry unaltered.
    mask_width : int
        The total number of components (width of the mask).
    set_ones : bool
        Defines how component_list is translated into component_mask.

    Returns
    -------
    list
        Mask compatible with ptrace and ptranspose procedures.
    '''

    assert max(component_list) < mask_width

    lookup = set(component_list)
    component_mask = [ (index in lookup) for index in range(mask_width) ]

    if not(set_ones):
        component_mask = map(operator.not_, component_mask)

    return list(map(int, component_mask))

