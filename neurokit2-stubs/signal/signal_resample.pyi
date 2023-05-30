import numpy as np
import pandas as pd

from typing import Union

def signal_resample(
    signal: Union[list, np.array, pd.Series],
    desired_length: int = None,
    sampling_rate: int = None,
    desired_sampling_rate: int = None,
    method: str = "interpolation"
) -> np.array:
    ...