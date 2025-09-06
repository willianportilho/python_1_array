from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the given file path and return its pixel data \
as a NumPy array.

    Parameters:
        path (str): The path to the image file. Only JPEG/JPG images \
are supported.

    Returns:
        np.ndarray: A 3-dimensional array representing the image in RGB \
format with shape (height, width, 3), or None if an error occurs.

    Notes:
        - The function prints the shape of the image and the pixel values.
        - The returned array has dtype corresponding to the image \
(usually uint8).
        - Errors are caught and printed; the function returns None \
in case of failure.
    """
    try:
        if not path.lower().endswith((".jpg", ".jpeg")):
            raise TypeError("The file is not a JPEG or JPG extension")

        try:
            img = Image.open(path)
        except Exception:
            raise AssertionError(f"Cannot find or corrupted file '{path}'")

        if img.format not in ("JPEG", "JPG"):
            raise ValueError("The file is not a JPEG or JPG image")

        img = img.convert("RGB")

        img_array = np.array(img)

        return img_array

    except (FileNotFoundError, IOError, ValueError, TypeError, AssertionError
            ) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None
