import cv2
import numpy as np
import sklearn as sk
from scipy import stats


def compute_mean(image: np.ndarray) -> float:
    return np.mean(image.flatten())


def compute_median(image: np.ndarray) -> float:
    return np.median(image.flatten())


def compute_std(image: np.ndarray) -> float:
    return np.std(image.flatten())


def compute_max(image: np.ndarray) -> float:
    return np.amax(image.flatten(), axis = 0)


def compute_min(image: np.ndarray) -> float:
    return np.amin(image.flatten(), axis = 0)


def compute_mode(image: np.ndarray) -> float:
    return stats.mode(image.flatten(), axis = 0)
