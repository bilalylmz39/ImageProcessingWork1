import cv2

img1  = cv2.imread('mes.jpg')
img2 = cv2.imread('ger.jpg')
img1 = cv2.resize(img1,(1000,500))
img2 = cv2.resize(img2,(1000,500))
print(img1.shape)
print(img2.shape)

totalImg = cv2.add(img1,img2)

print(img1[0,0])
print(img2[0,0])
print(totalImg[0,0])
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow("Mix",totalImg)

cv2.waitKey(0)
