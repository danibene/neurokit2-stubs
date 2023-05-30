from typing import Union, List, Dict, Any, Tuple
import numpy as np
import pandas as pd

def ecg_peaks(
    ecg_cleaned: Union[List[float], np.ndarray, pd.Series],
    sampling_rate: int = 1000,
    method: str = "neurokit",
    correct_artifacts: bool = False,
    **kwargs: Any
) -> Tuple[Dict[str, List[int]], Dict[str, Union[int, float]]]:
    ...