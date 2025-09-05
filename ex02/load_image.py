from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    try:
        img = Image.open(path)

        if img.format not in ("JPEG", "JPG"):
            raise ValueError("The file is not a JPEG or JPG image")

        img = img.convert("RGB")

        img_array = np.array(img)

        print(f"The shape of image is: {img_array.shape}")
        print(img_array)

        return img_array

    except (FileNotFoundError, IOError, ValueError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None


def ft_load_tests():
    pass


def main():
    """Main function to run tests for ft_load function and handle test\
exceptions.

Parameters:
    None

Returns:
    None
    """
    try:
        pass
    except AssertionError as ae:
        print(f"❌ {ft_load_tests.__name__} assertion failed: {ae}")
    except Exception as e:
        print(f"❌ unexpected exception: {e}")
    else:
        print(f"\n✅ All tests in {ft_load_tests.__name__} passed.")


if __name__ == "__main__":
    main()
