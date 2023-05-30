from typing import Optional, Union, List

import numpy as np

def eda_simulate(
    duration: int = 10,
    length: Optional[int] = None,
    sampling_rate: int = 1000,
    noise: float = 0.01,
    scr_number: int = 1,
    drift: Union[float, List[float]] = -0.01,
    random_state: Optional[Union[int, np.random.RandomState, np.random.Generator]] = None,
    random_state_distort: Union[str, None, int, np.random.RandomState, np.random.Generator] = "spawn",
) -> np.ndarray:
    ...
    
def _eda_simulate_scr(
    sampling_rate: int = 1000,
    length: Optional[int] = None,
    time_peak: float = 3.0745,
    rise: float = 0.7013,
    decay: List[float] = [3.1487, 14.1257]
) -> np.ndarray:
    ...
    
def _eda_simulate_bateman(
    sampling_rate: float = 1000,
    t1: float = 0.75,
    t2: float = 2
) -> np.ndarray:
    ...