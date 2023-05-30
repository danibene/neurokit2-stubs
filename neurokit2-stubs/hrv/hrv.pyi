import pandas as pd

def hrv(peaks: dict or pd.DataFrame, sampling_rate: int = 1000, show: bool = False, **kwargs) -> pd.DataFrame:
    ...

def _hrv_plot(peaks: dict or pd.DataFrame, out: pd.DataFrame, sampling_rate: int = 1000, interpolation_rate: int = 100, **kwargs):
    ...