import cv2
import numpy as np

matrix = np.ones((255, 255))
wvR = np.arange(1,128) 
wvL = np.flip(wvR)
wvM = np.ones(1)
wvX = np.concatenate((wvL, wvM, wvR), axis=0)
wvY = np.arange(0, 255)
wvY = wvY.reshape(255,1)

print(wvY)
matrix = matrix *wvX*wvX *wvY
min_val = np.min(matrix)
max_val = np.max(matrix)

# 정규화 수행
normalized_matrix = (matrix - min_val) / (max_val - min_val) * 255

# 정수형으로 변환
normalized_matrix = normalized_matrix.astype(np.uint8)

print(normalized_matrix)

gray_image = (normalized_matrix).astype(np.uint8)
cv2.imshow('Gray Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()