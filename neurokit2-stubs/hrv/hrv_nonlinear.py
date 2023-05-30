import numpy as np
import pandas as pd
from typing import Dict, Any, Union, List


def hrv_nonlinear(
    peaks: Union[List[int], Dict[str, Union[np.ndarray, List[float]]]],
    sampling_rate: int = 1000,
    show: bool = False,
    **kwargs: Any
) -> pd.DataFrame:
    ...