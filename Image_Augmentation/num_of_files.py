# Just gets nuymber of images in directory (needed for other augmentations)
import os

initial_count = 0
dir = "/Users/fletcherpearmaine/Desktop/Handgun_images/images"

for path in os.listdir(dir):
    if os.path.isfile(os.path.join(dir, path)):
        initial_count += 1
print(initial_count)
