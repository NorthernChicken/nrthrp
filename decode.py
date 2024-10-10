from PIL import Image
import numpy as np

def load_custom_image(file_path):
    with open(file_path, 'r') as file:
        width, height = map(int, file.readline().split())
        pixels = []
        for line in file:
            pixels.append([int(char) for char in line.strip()])
        return np.array(pixels), (width, height)

def decode_image(encoded_pixels, output_image_path):
    decoded_pixels = (encoded_pixels * 25.5).astype(np.uint8)
    img = Image.fromarray(decoded_pixels)
    img.save(output_image_path)

encoded_pixels, (width, height) = load_custom_image("result.nrthrp")
decode_image(encoded_pixels, "decoded_image.png")
