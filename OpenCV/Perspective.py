#  !/usr/bin/env  python
#  -*- coding:utf-8 -*-
# @Time   :  2019.
# @Author :  绿色羽毛
# @Email  :  lvseyumao@foxmail.com
# @Blog   :  https://blog.csdn.net/ViatorSun
# @Note   :  透视变换


import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread("img_32984.jpg")
rows , cols ,ch = img.shape

(r, g, b)=cv2.split(img)
img_2 =cv2.merge([b,g,r])



pts1 = np.float32([[156,339],[155,54],[340,45],[346,349]])
pts2 = np.float32([[0,0],[300,0],[300,200],[0,200]])

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img_2 ,M,(300,200))


plt.subplot(121),plt.imshow(img_2),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
