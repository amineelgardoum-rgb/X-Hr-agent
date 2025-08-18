import numpy as np

def get_embedding(text: str) -> np.ndarray:
    """Simulates generating a text embedding."""
    seed = sum(ord(c) for c in text)
    np.random.seed(seed)
    return np.random.rand(128)