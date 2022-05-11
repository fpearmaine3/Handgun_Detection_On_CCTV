import numpy
import cv2

# image path, image.png is a generic name
img_path = '/Users/fletcherpearmaine/Desktop/Augmentations/Handgun_images1/image.png'

image = cv2.imread(img_path) # Load/Read an image/ make a copy
image = img.copy()

prob = 0.05
if len(image.shape) == 2:
    black = 0
    white = 255
else:
    colorspace = image.shape[2]

    if colorspace == 3:  # (Considering all images in dataset have 3 channels (RGB))
        black = np.array([0, 0, 0], dtype = 'uint8') # add black
        white = np.array([255, 255, 255], dtype = 'uint8') # add white
    else:
        black = np.array([0, 0, 0, 255], dtype = 'uint8')
        white = np.array([255, 255, 255, 255], dtype = 'uint8')
probs = np.random.random(image.shape[:2])
image[probs < (prob / 2)] = black
image[probs > 1 - (prob / 2)] = white

cv2.imshow('Image with random noise', image) # output blurred image

cv2.waitKey(0) # Close window if key is pressed
cv2.destroyAllWindows()
