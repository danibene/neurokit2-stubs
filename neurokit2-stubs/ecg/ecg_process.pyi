from typing import Any, Union, List, Tuple, Dict
import pandas as pd
from pandas import DataFrame
import numpy as np

def ecg_process(
    ecg_signal: Union[List, np.ndarray, pd.Series],
    sampling_rate: int = 1000,
    method: str = "neurokit"
) -> Tuple[DataFrame, Dict[str, Any]]:
    ...