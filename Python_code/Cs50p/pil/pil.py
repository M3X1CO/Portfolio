import sys
from PIL import Image

images = []

# Iterate over command-line arguments (image file paths)
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

# Optionally, remove a specific image from the list by index
if len(images) >= 3:  # Check if there are at least three images in the list
    del images[1]  # Remove the second image (index 1) from the list

# Create the GIF with the remaining images
images[0].save(
    "slice.gif", save_all=True, append_images=images[1:], duration=300, loop=0
)


# python pil.py slice1_0_0.gif slice1_0_1.gif slice1_0_2.gif slice1_0_3.gif slice1_0_4.gif