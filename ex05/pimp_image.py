import numpy as np
from PIL import Image


def validate_array(array):
    """
    Validates that the input array is a 3D NumPy array in (H, W, RGB) format.

Parameters:
    array (np.ndarray): The image array to validate. Must be a 3D array with \
shape (H, W, 3) representing RGB channels.

Return:
    None
    """
    if array is None:
        raise ValueError("Input array is None")
    if array.ndim != 3:
        raise ValueError("Array must be in (H, W, RGB) format")
    if array.shape[2] != 3:
        raise ValueError("Input array must be a 3D array (H, W, RGB)")


def ft_invert(array) -> np.ndarray:
    """
Inverts the color of the image received.
    """
    try:
        validate_array(array)
        invert_arr = 255 - array
        Image.fromarray(invert_arr).show()
        return invert_arr
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: ft_invert: {e}")
    return None


def ft_red(array) -> np.ndarray:
    """
Keeps only the red channel, sets green and blue to zero.
    """
    try:
        validate_array(array)
        red_img = np.zeros_like(array)
        red_img[:, :, 0] = array[:, :, 0]
        Image.fromarray(red_img).show()
        return red_img
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: ft_red: {e}")
    return None


def ft_green(array) -> np.ndarray:
    """
Keeps only the green channel, sets red and blue to zero.
    """
    try:
        validate_array(array)
        green_img = np.zeros_like(array)
        green_img[:, :, 1] = array[:, :, 1]
        Image.fromarray(green_img).show()
        return green_img
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: ft_green: {e}")
    return None


def ft_blue(array) -> np.ndarray:
    """
Keeps only the blue channel, sets red and green to zero.
    """
    try:
        validate_array(array)
        blue_img = np.zeros_like(array)
        blue_img[:, :, 2] = array[:, :, 2]
        Image.fromarray(blue_img).show()
        return blue_img
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: ft_blue: {e}")
    return None


def ft_grey(array) -> np.ndarray:
    """
Converts the image to grayscale while keeping the shape (H, W, RGB), \
using only division (/).
    """
    try:
        validate_array(array)
        channels = np.stack([array[:, :, 0], array[:, :, 1], array[:, :, 2]], axis=-1)
        grey = (channels / 3).mean(axis=-1)
        grey = grey.astype(np.uint8)
        grey_img = np.stack([grey, grey, grey], axis=-1)
        Image.fromarray(grey_img).show()
        return grey_img
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: ft_grey: {e}")
    return None
