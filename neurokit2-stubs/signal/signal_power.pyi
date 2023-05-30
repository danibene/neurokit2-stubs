from typing import Union

import numpy as np
import pandas as pd

def signal_power(
    signal: Union[list, np.ndarray, pd.Series],
    frequency_band: Union[tuple, list],
    sampling_rate: int = 1000,
    continuous: bool = False,
    show: bool = False,
    normalize: bool = True,
    **kwargs,
) -> pd.DataFrame:
    ...