
#测试一下opencv
import cv2 as cv
# 
img = cv.imread("F:/1.png")
# 
cv.namedWindow("Image")
cv.imshow("Image",img)
cv.waitKey(0)
 
cv2.destroyAllWindows()
