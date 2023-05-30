import numpy as np
import pandas as pd

from typing import Any

def rsp_process(
    rsp_signal: list | np.array | pd.Series,
    sampling_rate: int = 1000,
    method: str = "khodadad2018",
    method_rvt: str = "harrison2021",
    report: str | None = None,
    **kwargs: Any,
    ) -> tuple[pd.DataFrame, dict]:
    ...