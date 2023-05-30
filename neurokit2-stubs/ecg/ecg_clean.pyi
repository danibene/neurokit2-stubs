from typing import Union, Any
import numpy as np
import pandas as pd

def ecg_clean(
    ecg_signal: Union[list, np.array, pd.Series],
    sampling_rate: int = 1000,
    method: str = "neurokit",
    **kwargs: Any,
) -> np.array:
    ...