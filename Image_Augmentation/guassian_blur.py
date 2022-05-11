import cv2
import numpy

# image.png is a generic name, I would change this for each Type-Basic images
# Path works for mac, change if using widnows/linix

img_path = '/Users/fletcherpearmaine/Desktop/Augmentations/Handgun_images1/image.png'

# Load/Read an image
image = cv2.imread(img_path)

# show the image on the newly created image window
cv2.imshow('Input image', image)

blur_img = cv2.GaussianBlur(image, (5, 5), 50) # blur input image

cv2.imshow('Blur image', blur_img) # output blurred image

cv2.waitKey(0) # Close window if key is pressed
cv2.destroyAllWindows()
