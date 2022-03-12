from typing import Tuple
from math import pi, sin, cos


def linear(percent: float) -> float:
    """
    Function for linear easing.
    """
    return percent


def _flip(percent: float) -> float:
    return 1.0 - percent


def ease_in(percent: float) -> float:
    """
    Function for quadratic ease-in easing.
    """
    return percent * percent


def ease_out(percent: float) -> float:
    """
    Function for quadratic ease-out easing.
    """
    return _flip(_flip(percent) * _flip(percent))


def ease_in_out(percent: float) -> float:
    """
    Function for quadratic easing in and out.
    """

    return 2 * percent**2 if percent < 0.5 else 1 - (-2 * percent + 2)**2 / 2


def ease_out_elastic(percent: float) -> float:
    """
    Function for elastic ease-out easing.
    """
    c4 = 2 * pi / 3
    result = 0.0
    if percent == 1:
        result = 1
    elif percent > 0:
        result = (2 ** (-10 * percent)) * sin((percent * 10 - 0.75) * c4) + 1
    return result


def ease_out_bounce(percent: float) -> float:
    """
    Function for a bouncy ease-out easing.
    """
    n1 = 7.5625
    d1 = 2.75

    if percent < 1 / d1:
        return n1 * percent * percent
    elif percent < 2 / d1:
        percent_modified = percent - 1.5/d1
        return n1 * percent_modified * percent_modified + 0.75
    elif percent < 2.5 / d1:
        percent_modified = percent - 2.25/d1
        return n1 * percent_modified * percent_modified + 0.9375
    else:
        percent_modified = percent - 2.625/d1
        return n1 * percent_modified * percent_modified + 0.984375


def ease_in_back(percent: float) -> float:
    """
    Function for ease_in easing which moves back before moving forward.
    """
    c1 = 1.70158
    c3 = c1 + 1

    return c3 * percent * percent * percent - c1 * percent * percent


def ease_out_back(percent: float) -> float:
    """
    Function for ease_out easing which moves back before moving forward.
    """
    c1 = 1.70158
    c3 = c1 + 1

    return 1 + c3 * pow(percent - 1, 3) + c1 * pow(percent - 1, 2)


def ease_in_sin(percent: float) -> float:
    """
    Function for ease_in easing using a sin wave
    """
    return 1 - cos((percent * pi) / 2)


def ease_out_sin(percent: float) -> float:
    """
    Function for ease_out easing using a sin wave
    """
    return sin((percent * pi) / 2)


def ease_in_out_sin(percent: float) -> float:
    """
    Function for easing in and out using a sin wave
    """
    return -cos(percent * pi)*0.5 + 0.5


def smoothstep(percent: float) -> float:
    """
    Function for smoothstep easing.
    """
    percent = percent * percent * (3.0 - 2.0 * percent)
    return percent



