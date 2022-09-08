import cv2
import numpy as np
import sklearn as sk
from scipy import stats


def compute_mean(image: np.ndarray) -> float:
    """
    @author: Vo, Huynh Quang Nguyen; Hoang, Anh Minh
    """
    return np.mean(image.flatten())

def compute_median(image: np.ndarray) -> float:
    """
    @author: Vo, Huynh Quang Nguyen; Hoang, Anh Minh
    """
    return np.median(image.flatten())

def compute_std(image: np.ndarray) -> float:
    """
    @author: Vo, Huynh Quang Nguyen; Hoang, Anh Minh
    """
    return np.std(image.flatten())

def compute_max(image: np.ndarray) -> float:
    """
    @author: Vo, Huynh Quang Nguyen; Hoang, Anh Minh
    """
    return np.amax(image.flatten(), axis = 0)

def compute_min(image: np.ndarray) -> float:
    """
    @author: Vo, Huynh Quang Nguyen; Hoang, Anh Minh
    """
    return np.amin(image.flatten(), axis = 0)

def compute_mode(image: np.ndarray) -> float:
    """
    @author: Vo, Huynh Quang Nguyen; Hoang, Anh Minh
    """
    return stats.mode(image.flatten(), axis = 0)[0]

def compute_means_from_images(images):
    """
    @author: Vo, Huynh Quang Nguyen; Hoang, Anh Minh
    """
    means = []
    for image in images:
        mean = compute_mean(image)
        means.append(mean)
    
    return np.array(means)

def compute_median_from_images(image):
    pass