import cv2
import random

img_path = '/Users/fletcherpearmaine/Desktop/Augmentations/Handgun_images1/image.png'
img = cv2.imread(img_path)

amount = 0.5
out = img.copy()

for x in range(10):
    # Add 10 black boxes to image
    x1 = x
    y1 = x + 1
    x2 = x + 2
    y2 = x + 3
    # Set up dimensions of black box
    mask_w = (x2 - x1) * 0.5
    mask_h = (y2 - y1) * 0.5
    mask_x1 = random.randint(x1, x2 - mask_w)
    mask_y1 = random.randint(y1, y2 - mask_h)
    mask_x2 = mask_x1 + mask_w
    mask_y2 = mask_y1 + mask_h
    cv2.rectangle(out, (mask_x1, mask_y1), (mask_x2, mask_y2), (0, 0, 0), thickness = -1) # Draw a black rectangle onto the image

cv2.imshow('Black box cut-out image', out) # output blurred image
cv2.waitKey(0) # Close window if key is pressed
cv2.destroyAllWindows()

'''


def cutout(img, gt_boxes, amount=0.5):

    ### Cutout ###
    img: image
    gt_boxes: format [[obj x1 y1 x2 y2],...]
    amount: num of masks / num of objects

'''
