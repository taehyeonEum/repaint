import cv2

img = cv2.imread("./data/datasets/gt_keep_masks/chair/img_chair256.png" , cv2.IMREAD_GRAYSCALE)
print(img.shape)
cv2.imwrite("./data/datasets/gt_keep_masks/chair_gray/img_chair256_grayscale.png", img)
