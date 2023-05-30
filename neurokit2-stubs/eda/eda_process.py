from typing import Any, Dict, Optional, Tuple, Union

import numpy as np
import pandas as pd

def eda_process(
    eda_signal: Union[list, np.array, pd.Series],
    sampling_rate: int = 1000,
    method: str = "neurokit",
    report: Optional[str] = None,
    **kwargs
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    ...

def _eda_plot(
    peaks: Union[list, np.array, pd.Series],
    out: pd.DataFrame,
    sampling_rate: int = 1000,
    interpolation_rate: int = 100,
    **kwargs
):
    ...
