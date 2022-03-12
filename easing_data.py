from dataclasses import dataclass
from typing import Callable


@dataclass
class EasingData:
    """
    Data class for holding information about easing.
    """
    start_period: float
    cur_period: float
    end_period: float
    start_value: float
    end_value: float
    ease_function: Callable

