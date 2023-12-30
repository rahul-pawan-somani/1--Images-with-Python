import sys
import os
from PIL import Image, ImageFilter


def sharpen_image(img):
    return img.filter(ImageFilter.SHARPEN)


def convert_to_gray(img):
    return img.convert("L")


def rotate_image(img, angle):
    return img.rotate(angle)


def resize_image(img, width, height):
    return img.resize((width, height))


def crop_image(img, left, top, right, bottom):
    box = (left, top, right, bottom)
    return img.crop(box)


def create_thumbnail(img, size):
    img.thumbnail((size, size))
    return img


def save_image(img, input_path, image_operation, format="png"):
    directory = os.path.dirname(input_path)
    output_path = os.path.join(directory, f"{image_operation}_image.png")
    img.save(output_path, format)
    print(f"Image saved as {image_operation}_image.png")


def process_image(image_path, image_operation):
    try:
        img = Image.open(image_path)
    except IOError:
        print(
            f"Error: Could not open image file '{image_path}'. Please check the file path and format.")
        sys.exit(1)

    try:
        if image_operation == "sharpen":
            img = sharpen_image(img)
        elif image_operation == "gray":
            img = convert_to_gray(img)
        elif image_operation == "rotate":
            angle = int(input("Enter the rotation angle (in degrees): "))
            img = rotate_image(img, angle)
        elif image_operation == "resize":
            width = int(input("Enter the new width: "))
            height = int(input("Enter the new height: "))
            img = resize_image(img, width, height)
        elif image_operation == "crop":
            left = int(input("Enter the left coordinate: "))
            top = int(input("Enter the top coordinate: "))
            right = int(input("Enter the right coordinate: "))
            bottom = int(input("Enter the bottom coordinate: "))
            img = crop_image(img, left, top, right, bottom)
        elif image_operation == "thumbnail":
            size = int(input("Enter the thumbnail size: "))
            img = create_thumbnail(img, size)
        else:
            print(
                f"Error: Unknown image operation '{image_operation}'. Please choose a valid operation.")
            sys.exit(1)
    except ValueError:
        print("Error: Invalid input for numeric values. Please enter valid numbers.")
        sys.exit(1)

    save_image(img, image_path, image_operation)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <image_path> <image_operation>")
        sys.exit(1)

    image_path = sys.argv[1]
    image_operation = sys.argv[2]

    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' not found.")
        sys.exit(1)

    process_image(image_path, image_operation)
