# Copyright (c) 2023 Julian Müller (ChaoticByte)


from colorsys import rgb_to_hsv as _rgb_to_hsv


def rgb_to_hsv(r:int, g:int, b:int) -> tuple:
    '''Convert RGB colors `(255, 220, 100)` to HSV `(0.129, 0.608, 1.0)`'''
    assert type(r) == int
    assert type(g) == int
    assert type(b) == int
    r_ = r / 255.0
    g_ = g / 255.0
    b_ = b / 255.0
    return _rgb_to_hsv(r_, g_, b_)
