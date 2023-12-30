# PictureTools

This Python script provides a set of image-processing tools using the Pillow (PIL) library. It allows users to perform various operations on images, including sharpening, grayscale conversion, rotation, resizing, cropping, and thumbnail creation. The script takes command-line arguments specifying the image file path and the desired image operation.

## Usage

To use the script, run it from the command line with the following format:

```bash
python PictureTools.py <image_path> <image_operation>
```

- `<image_path>`: The path to the input image file.
- `<image_operation>`: The desired image operation. Choose from "sharpen," "gray," "rotate," "resize," "crop," or "thumbnail."

### Examples:

1. **Sharpen Image:**

   ```bash
   python PictureTools.py input_image.jpg sharpen
   ```

2. **Convert to Grayscale:**

   ```bash
   python PictureTools.py input_image.jpg gray
   ```

3. **Rotate Image:**

   ```bash
   python PictureTools.py input_image.jpg rotate
   ```

   (Follow the prompts to enter the rotation angle)

4. **Resize Image:**

   ```bash
   python PictureTools.py input_image.jpg resize
   ```

   (Follow the prompts to enter the new width and height)

5. **Crop Image:**

   ```bash
   python PictureTools.py input_image.jpg crop
   ```

   (Follow the prompts to enter the left, top, right, and bottom coordinates)

6. **Create Thumbnail:**

   ```bash
   python PictureTools.py input_image.jpg thumbnail
   ```

   (Follow the prompts to enter the thumbnail size)

## Dependencies

This script relies on the Pillow library (`PIL`). Ensure that you have it installed:

```bash
pip install Pillow
```

## Notes

- The script handles various error scenarios, such as invalid file paths, unsupported image operations, and input validation for numeric values.
- Make sure to provide the correct number of command-line arguments and follow the prompts for specific operations.
- Processed images are saved in the same directory as the input image.

Feel free to explore and use this script for convenient image processing tasks!
