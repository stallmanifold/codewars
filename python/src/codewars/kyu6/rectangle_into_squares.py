def sq_in_rect(length, width):
    """
    Solve the rectangle tiling problem using a greedy algorithm.
    """
    def step(length, width):
        longer_side  = min(length, width)
        new_length   = length - longer_side
        new_width    = width - longer_side
        # At least one of the sides is nonzero since we subtract the minimum
        # of two sides above.
        shorter_side = max(new_length, new_width)

        return (longer_side, shorter_side)

    if length == width:
        return None
    
    sides = []
    rect = (max(length, width), min(length, width))
    while True:
        rect = step(rect[0], rect[1])
        side = rect[0]

        if side <= 0:
            break

        sides.append(side)
    
    return sides


def sqInRect(length, width):
    """
    This is a wrapper function to comply with the naming convention in the
    problem definition.
    """
    return sq_in_rect(length, width)
