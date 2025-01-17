from cloudseg.utils.constants import *
import cv2
import os
import numpy as np

full_mask = cv2.imread(os.path.join(PROJECT_PATH, "cloudseg/datasets/resources/full_mask.bmp"), -1)
background_mask = cv2.imread(os.path.join(PROJECT_PATH, "cloudseg/datasets/resources/background_mask.bmp"), -1)


def apply_background_mask(img):
    """
    Apply background mask to image by setting masked pixels to NaN
    """
    img[background_mask == 255] = np.nan
    return img


def apply_full_mask(img, fill=np.nan):
    """
    Apply common mask to image by setting masked pixels to the given fill value
    """
    img[full_mask == 255] = fill
    return img


def apply_mask(img, mask, fill=np.nan):
    """
    Apply given mask by setting masked pixels to the given fill value
    """
    img[mask == 255] = fill
    return img
