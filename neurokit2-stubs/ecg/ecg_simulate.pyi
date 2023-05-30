from typing import Optional, Union

import numpy as np
import pandas as pd

def ecg_simulate(
    duration: int = 10,
    length: Optional[int] = None,
    sampling_rate: int = 1000,
    noise: float = 0.01,
    heart_rate: int = 70,
    heart_rate_std: int = 1,
    method: str = "ecgsyn",
    random_state: Union[None, int, np.random.RandomState, np.random.Generator] = None,
    random_state_distort: Union[str, None, int, np.random.RandomState, np.random.Generator] = "spawn",
    **kwargs,
) -> np.ndarray:
    ...