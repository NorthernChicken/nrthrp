from PIL import Image
import numpy as np

def load_image(image_path):
    img = Image.open(image_path)
    img = img.convert('L')
    pixels = np.array(img)
    return pixels, img.size

def encode_image(pixels):
    encoded_pixels = (pixels / 25.5).astype(int)
    return encoded_pixels

pixels, (width, height) = load_image("encode.png")
encoded_pixels = encode_image(pixels)

def save_custom_image(encoded_pixels, width, height, output_file):
    with open(output_file, 'w') as file:
        file.write(f"{width} {height}\n")
        for row in encoded_pixels:
            file.write(''.join(map(str, row)) + "\n")

save_custom_image(encoded_pixels, width, height, "result.nrthrp")