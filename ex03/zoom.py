from load_image import ft_load
import numpy as np
import cv2


def zoom(img: np.ndarray, size: int) -> np.ndarray:
    height, width = img.shape[:2]
    zoom_size = min(size, height, width)
    start_h = max(0, (height - zoom_size) // 2)
    start_w = max(0, (width - zoom_size) // 2)
    end_h = start_h + zoom_size
    end_w = start_w + zoom_size
    
    return img[start_h:end_h, start_w:end_w]


def rgb_to_gray(img: np.ndarray) -> np.ndarray:
    if len(img.shape) == 3 and img.shape[2] == 3:
        gray = np.dot(img[...,:3], [0.2989, 0.5870, 0.1140])
        gray = np.array(gray, dtype=np.uint8)
        gray = gray[..., np.newaxis]
        return gray
    return img


def print_zoom_info(zoomed_img: np.ndarray):
    print(f"New shape after slicing: {zoomed_img.shape} or ({zoomed_img.shape[0]}, {zoomed_img.shape[1]})")
    print(zoomed_img)


def draw_axes_outside(img: np.ndarray):
    height, width = img.shape[:2]
    margin = 40

    if img.ndim == 3:
        img = img.squeeze()
    
    canvas = np.ones((height + margin, width + margin), dtype=img.dtype) * 255
    canvas[:height, margin:] = img

    axis_color = 0
    tick_size = 5
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.4
    thickness = 1

    cv2.line(canvas, (margin, height), (width + margin - 1, height), axis_color, 1) # x axis
    cv2.line(canvas, (margin, 0), (margin, height - 1), axis_color, 1) # y axis

    for x in range(0, width, 50):
        px = margin + x
        cv2.line(canvas, (px, height), (px, height + tick_size), axis_color, 1)

        text = str(x)
        text_size = cv2.getTextSize(text, font, font_scale, thickness)[0] # ex.: (w 18px, h 8px)
        text_x = px - text_size[0] // 2 # text x position (centralized)
        text_y = height + tick_size + text_size[1] + 2 # text y position
        
        cv2.putText(canvas, text, (text_x, text_y), font, font_scale, axis_color, thickness)

    for y in range(0, height, 50):
        py = y
        cv2.line(canvas, ((margin - tick_size), py), (margin, py), axis_color, 1)

        text = str(y)
        text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
        text_x = margin - tick_size - text_size[0] - 2
        text_y = py + text_size[1] // 2

        cv2.putText(canvas, text, (text_x, text_y), font, font_scale, axis_color, thickness)

    return canvas


def show_image(img: np.ndarray):
    cv2.imshow("animal", draw_axes_outside(img))
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def main():
    """Main function to run tests for ft_load function and handle test\
exceptions.

Parameters:
    None

Returns:
    None
    """
    try:
        file_path = "animal.jpeg"
        img = ft_load(file_path)
        if img is None:
            print(f"Failed to load image: {file_path}")
        
        zoomed_img = zoom(img, size=400)
        zoomed_gray = rgb_to_gray(zoomed_img)

        print_zoom_info(zoomed_gray)
        show_image(zoomed_gray)

    except Exception as e:
        print(f"unexpected exception: {e}")


if __name__ == "__main__":
    main()
