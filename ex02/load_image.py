from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    try:
        if not path.lower().endswith((".jpg", ".jpeg")):
            raise TypeError("The file is not a JPEG or JPG extension")

        try:
            img = Image.open(path)
        except Exception:
            raise ValueError(f"Cannot identify or corrupted file '{path}'")

        if img.format not in ("JPEG", "JPG"):
            raise ValueError("The file is not a JPEG or JPG image")

        img = img.convert("RGB")

        img_array = np.array(img)

        print(f"The shape of image is: {img_array.shape}")
        print(img_array)

        return img_array

    except (FileNotFoundError, IOError, ValueError, TypeError) as e:
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
        print(f"unexpected exception: {e}")


if __name__ == "__main__":
    main()
