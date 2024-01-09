from typing import List, Union, Optional, Tuple
import numpy as np
import pandas as pd


def signal_interpolate(
    x_values: Union[List[float], np.ndarray, pd.Series],
    y_values: Optional[Union[List[float], np.ndarray, pd.Series]] = None,
    x_new: Optional[Union[List[float], np.ndarray, pd.Series, int]] = None,
    method: str = "quadratic",
    fill_value: Optional[Union[float, Tuple[float, float], str]] = None,
) -> np.ndarray: ...
