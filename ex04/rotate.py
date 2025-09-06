from load_image import ft_load
import numpy as np
import cv2


def cut(img: np.ndarray, size: int) -> np.ndarray:
    height, width = img.shape[:2]
    zoom_size = min(size, height, width)

    if height < 1 or width < 1:
        raise ValueError("Image dimensions are too small for zoom.")

    offset_w = 135
    offset_h = 85

    start_h = max(0, (height - zoom_size) // 2 - offset_h)
    start_w = max(0, (width - zoom_size) // 2 + offset_w)
    end_h = start_h + zoom_size
    end_w = start_w + zoom_size

    return img[start_h:end_h, start_w:end_w]


def rgb_to_gray(img: np.ndarray) -> np.ndarray:
    """Converts an RGB image to grayscale. If image is already grayscale, \
returns it unchanged.

Parameters:
    img (np.ndarray): Input image array (H, W, 3) for RGB or (H, W) for \
grayscale.

Returns:
    np.ndarray: Grayscale image of shape (H, W, 1) or (H, W) if already \
grayscale.
    """
    if img.ndim not in [2, 3]:
        raise ValueError("Invalid image dimensions")

    if len(img.shape) == 3 and img.shape[2] == 3:
        gray = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])
        gray = np.array(gray, dtype=np.uint8)
        gray = gray[..., np.newaxis]
        return gray
    return img


def transpose(img: np.ndarray) -> np.ndarray:
    if img is None or img.size == 0:
        raise ValueError("Invalid image format to transpose")
    
    height, width = img.shape[:2]
    transposed = np.zeros((width, height), dtype=img.dtype)
    for i in range(height):
        for j in range(width):
            transposed[j][i] = img[i][j]
    return transposed


def main():
    """Main function to load an image, slices, convert to grayscale, \
print info, and transposes the image.

Parameters:
    None

Returns:
    None
    """
    try:
        file_path = "animal.jpeg"
        img = ft_load(file_path)
        if img is None:
            raise FileNotFoundError(f"Failed to load image: {file_path}")
        
        square_img = cut(img, 400)
        gray = rgb_to_gray(square_img)
        print("The shape of image is: " + \
              f"{gray.shape} or ({gray.shape[0]}, {gray.shape[1]})")
        print(gray)

        gray = gray.squeeze()
        transposed = transpose(gray)
        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)
        
    except Exception as e:
        print(f"Exception: Rotate Program: {e}")
    finally:
        cv2.destroyAllWindows()
        print("\nProgram ended...")


if __name__ == "__main__":
    main()
