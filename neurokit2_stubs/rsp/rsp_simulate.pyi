from typing import Optional, Union, List

import numpy as np

def rsp_simulate(
    duration: int = 10,
    length: Optional[int] = None,
    sampling_rate: int = 1000,
    noise: float = 0.01,
    respiratory_rate: float = 15,
    method: str = "breathmetrics",
    random_state: Optional[Union[int, np.random.RandomState, np.random.Generator]] = None,
    random_state_distort: Optional[Union[str, int, np.random.RandomState, np.random.Generator]] = "spawn",
) -> np.ndarray:
    ...