import cv2
import numpy as np 
import os 
image = cv2.imread("images/mat.png")
cnv_gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
_,thresh= cv2.threshold(cnv_gray,127,255,cv2.THRESH_BINARY)
contours, herarchy= cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("--------**--------\n")
print(f"contour length {len(contours)}")
print("--------**--------\n")
print (f"contour:{contours}")
print("--------**--------\n")
print(f"herarchy:{herarchy}")
print("--------**--------\n")
for i, contour in enumerate(contours):
    x, y, w, h = cv2.boundingRect(contour)
    img_crop = image[y:y + h, x:x + w]
    cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
    # cv2.imshow(f"Contour{i}", image)
    filename = f"Contour{i}.jpg"
    cv2.imwrite(f"images/contour/{filename}",img_crop)

    # for n in range(len(contour)-1):
    #     variable = f"A{n}"
    #     variable = cv2.imread(f"images/contour/{filename}")
    # cv2.imshow(f"image{n}",variable)

directory ="images/contour"
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    cnt= 0
    if os.path.isfile(f):
        img = cv2.imread(f)
        new_cnt=cnt+1
        print(f"length:{new_cnt}")
        cv2.imshow(f"contour{new_cnt}",img)        
    else:
        print("no contour picture found")

cv2.waitKey(0)
cv2.destroyAllWindows()