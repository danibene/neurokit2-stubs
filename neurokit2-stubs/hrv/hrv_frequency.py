from typing import List, Dict, Union
import pandas as pd
import numpy as np

def hrv_frequency(
    peaks: Union[List[int], Dict[str, Union[np.ndarray, List[float]]]],
    sampling_rate: int = 1000,
    ulf: tuple = (0, 0.0033),
    vlf: tuple = (0.0033, 0.04),
    lf: tuple = (0.04, 0.15),
    hf: tuple = (0.15, 0.4),
    vhf: tuple = (0.4, 0.5),
    psd_method: str = "welch",
    show: bool = False,
    silent: bool = True,
    normalize: bool = True,
    order_criteria: str = None,
    interpolation_rate: int = 100,
    **kwargs
) -> pd.DataFrame:
    ...