import numpy as np
from typing import Optional, List, Union

def signal_distort(
    signal: np.ndarray,
    sampling_rate: int = 1000,
    noise_shape: str = "laplace",
    noise_amplitude: float = 0,
    noise_frequency: int = 100,
    powerline_amplitude: float = 0,
    powerline_frequency: int = 50,
    artifacts_amplitude: float = 0,
    artifacts_frequency: int = 100,
    artifacts_number: int = 5,
    linear_drift: bool = False,
    random_state: Optional[Union[int, np.random.RandomState, np.random.Generator]] = None,
    silent: bool = False,
):
    ...
