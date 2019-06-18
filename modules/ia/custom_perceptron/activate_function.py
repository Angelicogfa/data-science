from math import exp
import numpy as np

def function_step_binary(value: float) -> float:
    return 1 if value >= 0 else 0

def function_sigmoide(value: float) -> float:
    return 1.0 / (1.0 + exp(-value))

def function_tah(value: float) -> float:
    return 2.0 / (1.0 + exp(-2.0 * value)) - 1.0

def function_relu(value: float) -> float:
    return value if value > 0 else 0

def function_softmax(value: float) -> float:
    e = np.exp(value - np.max(value))
    return e / e.sum()