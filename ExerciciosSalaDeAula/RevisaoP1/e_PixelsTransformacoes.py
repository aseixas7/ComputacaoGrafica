import cv2

img = cv2.imread("Media/jovensTitas.png")
negativo = 255 - img

cv2.imshow("Original", img)
cv2.imshow("Negativo", negativo)
cv2.waitKey(0)
cv2.destroyAllWindows()
