import numpy as np
from typing import Optional, List, Union

def signal_simulate(
    duration: int = 10,
    sampling_rate: int = 1000,
    frequency: int = 1,
    amplitude: float = 0.5,
    noise: float = 0,
    silent: bool = False,
    random_state: Optional[Union[int, np.random.RandomState, np.random.Generator]] = None,
) -> np.array:
    ...
