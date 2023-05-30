import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from typing import Union, List, Dict

def hrv_time(peaks: Union[List[int], Dict[str, Union[np.ndarray, List[float]]]],
             sampling_rate: int = 1000,
             show: bool = False,
             **kwargs) -> pd.DataFrame:
    ...