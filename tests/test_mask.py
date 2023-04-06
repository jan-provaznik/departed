from departed import mask_from_component_list

def test_mask ():
    mask_target = [ 1, 0, 0, 1 ]
    mask_result = mask_from_component_list([ 1, 2 ], 4, True)

    assert mask_target == mask_result

    mask_target = [ 0, 1, 1, 0 ]
    mask_result = mask_from_component_list([ 1, 2 ], 4)

    assert mask_target == mask_result

    mask_target = [ 1, 1, 1, 1 ]
    mask_result = mask_from_component_list([ 0, 1, 2, 3 ], 4)

    assert mask_target == mask_result

