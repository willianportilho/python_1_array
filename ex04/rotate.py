from load_image import ft_load
import numpy as np
import cv2


def cut(img: np.ndarray, size: int) -> np.ndarray:
    """
Crops a square region from the input image with optional offsets.

Parameters
    img : np.ndarray
        Input image as a NumPy array in (H, W, C) format, where H is height,
W is width, and C is the number of channels (e.g., 3 for RGB).
    size : int
        Desired size of the square crop. The actual crop size will be the \
minimum of this value and the image dimensions.

Returns
    np.ndarray
        Cropped image as a NumPy array. The output shape will be \
(crop_size, crop_size, C),
        where crop_size is determined by the minimum of `size` and the image \
dimensions.
    """
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
    """Transposes a 2D image array (flips rows and columns).

Parameters
    img : np.ndarray
        Input image as a 2D NumPy array.

Returns
    np.ndarray
        Transposed image as a 2D NumPy array.
    """
    if img is None or img.size == 0:
        raise ValueError("Invalid image format to transpose")
    
    height, width = img.shape[:2]
    transposed = np.zeros((width, height), dtype=img.dtype)
    for i in range(height):
        for j in range(width):
            transposed[j][i] = img[i][j]
    return transposed


def draw_axes_outside(img: np.ndarray):
    """Draws X and Y axes outside the image with ticks and numbers.

Parameters:
    img (np.ndarray): Input grayscale image (H, W) or (H, W, 1).

Returns:
    np.ndarray: Image with axes drawn outside (canvas of size \
H+margin x W+margin).
    """
    height, width = img.shape[:2]
    margin = 40

    if height < 1 or width < 1:
        raise ValueError("Image too small for drawing axes")

    if img.ndim == 3 and img.shape[2] == 1:
        img = img.squeeze()

    canvas = np.ones((height + margin, width + margin), dtype=img.dtype) * 255
    canvas[:height, margin:] = img

    axis_color = 0
    tick_size = 5
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.4
    thickness = 1

    cv2.line(canvas, (margin, height), (
        width + margin - 1, height), axis_color, 1)  # x axis
    cv2.line(canvas, (margin, 0), (
        margin, height - 1), axis_color, 1)  # y axis

    for x in range(0, width, 50):
        px = margin + x
        cv2.line(canvas, (px, height), (
            px, height + tick_size), axis_color, 1)

        text = str(x)
        text_size = cv2.getTextSize(
            text, font, font_scale, thickness)[0]  # ex.: (w 18px, h 8px)
        text_x = px - text_size[0] // 2  # text x position (centralized)
        text_y = height + tick_size + text_size[1] + 2  # text y position

        cv2.putText(canvas, text, (
            text_x, text_y), font, font_scale, axis_color, thickness)

    for y in range(0, height, 50):
        py = y
        cv2.line(canvas, ((margin - tick_size), py), (
            margin, py), axis_color, 1)

        text = str(y)
        text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
        text_x = margin - tick_size - text_size[0] - 2
        text_y = py + text_size[1] // 2

        cv2.putText(canvas, text, (
            text_x, text_y), font, font_scale, axis_color, thickness)

    return canvas


def show_image(img: np.ndarray):
    """Displays an image in a window with OpenCV and \
handles user interruptions.

Parameters:
    img (np.ndarray): Input image to display.

Returns:
    None
    """
    try:
        cv2.imshow("animal", draw_axes_outside(img))
        cv2.waitKey(0)
    except KeyboardInterrupt:
        print("\nRotate Program: Operation cancelled by user (Ctrl+C).")
    except cv2.error as e:
        print(f"Rotate Program: OpenCV error: {e}")
    finally:
        cv2.destroyAllWindows()


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
        show_image(transposed)
        
    except Exception as e:
        print(f"Exception: Rotate Program: {e}")
    finally:
        cv2.destroyAllWindows()
        print("\nProgram ended...")


if __name__ == "__main__":
    main()
