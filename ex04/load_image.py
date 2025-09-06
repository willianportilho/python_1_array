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


def main():
    """Main function to run tests for ft_load function and handle test\
exceptions.

Parameters:
    None

Returns:
    None
    """
    try:
        tests = [
            ("landscape.jpg", True),
            ("animal.jpeg", True),
            ("non_existent_file.jpg", False),
            ("non_image_file.txt", False),
            ("empty_image.jpeg", False),
            ("corrupted_image.jpg", False),
            ("not_jpeg_or_jpg_image.png", False)
        ]

        for path, expected in tests:
            print(f"\n=== TESTING: {path}")
            result = ft_load(path)

            is_loaded = result is not None

            if is_loaded == expected:
                print(f"✅ Expected behavior!: path: {path}\n")
            else:
                print(f"❌ Unexpected behavior!: path: {path}\n")

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()
