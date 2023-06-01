import numpy as np
from typing import Optional, List, Union


def check_random_state(seed: Optional[Union[int, np.random.RandomState, np.random.Generator]] = None) -> Union[np.random.RandomState, np.random.Generator]:
    ...


def spawn_random_state(rng: Optional[Union[int, np.random.RandomState, np.random.Generator]] = None, n_children: int = 1) -> List[Union[np.random.RandomState, np.random.Generator]]:
    ...


def check_random_state_children(random_state_parent: Optional[Union[int, np.random.RandomState, np.random.Generator]] = None, random_state_children: Union[str, None, int, np.random.RandomState, np.random.Generator] = None, n_children: int = 1) -> List[Union[np.random.RandomState, np.random.Generator]]:
    ...
