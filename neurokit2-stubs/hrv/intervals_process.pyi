from typing import Optional, Tuple, Union

import numpy as np

def intervals_process(
    intervals: Union[list, np.ndarray],
    intervals_time: Optional[Union[list, np.ndarray]] = None,
    interpolate: bool = False,
    interpolation_rate: int = 100,
    detrend: Optional[str] = None,
    **kwargs
) -> Tuple[np.ndarray, np.ndarray, int]:
    ...
