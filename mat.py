#/bin/sh:python 
import cv2
import numpy as np 
import os 
import matplotlib.pyplot as pp
# __________________***____________________
image = cv2.imread("images/mat2.png")
cnv_gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
_,thresh= cv2.threshold(cnv_gray,127,255,cv2.THRESH_BINARY)
contours, herarchy= cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# __________________***____________________ß
print("--------**--------\n")
print(f"contour length {len(contours)}")
print("--------*contoure*--------\n")
print (f"contour:{contours}")
print("--------*Herarchy*--------\n")
print(f"herarchy:{herarchy}\n")
print("--------**--------\n")
# __________________***____________________
for i, contour in enumerate(contours):
    x, y, w, h = cv2.boundingRect(contour)
    img_crop = image[y:y + h, x:x + w]
    cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
    # cv2.imshow(f"Contour{i}", image)
    filename = f"Contour{i}.jpg"
    cv2.imwrite(f"images/contour/{filename}",img_crop)
    print("--------**--------")
    print(f"--------X,Y,W,H CONTOURE::{i}--------\n")
    print(f"x{i} =>>",x)
    print(f"y{i} =>>",y)
    print(f"w{i} =>>",w)
    print(f"h{i} =>>",h)
    print("--------*END*--------\n")
# __________________*GETTING CROP CONTOURE IMAGES FROM DIRECTORY PRINTING FILE PATH  *____________________
directory ="images/contour"
s = ""
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    print(" File Path ===> ",f)
    img = cv2.imread(f)
    if os.path.isfile(f):
        img = cv2.imread(f)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # __________________*COLOR LOWER AND UPPER RANGE NOT NECESSARY FOR MATRIX IS IN BINARY FORM *____________________
        lower_red = np.array([0, 100, 100])
        upper_red = np.array([10, 255, 255])
        lower_green = np.array([50, 100, 100])
        upper_green = np.array([70, 255, 255])
        lower_blue = np.array([110, 100, 100])
        upper_blue = np.array([130, 255, 255])
        # __________________*RNAGE FOR EACH COLOR *____________________
        red_mask = cv2.inRange(hsv, lower_red, upper_red)
        green_mask = cv2.inRange(hsv, lower_green, upper_green)
        blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
        # cv2.imshow(f"contour",img)
        # __________________*SPLITTING THE IMAGE IN BGR FORM AND CONVERTING INTO BINARY IF ABOVE 255 AND BELOW 255 AND PERFORMING THE OR OPERATION  *____________________
        b, g, r = cv2.split(img)
        _, b_mask = cv2.threshold(b, 0, 255, cv2.THRESH_BINARY)
        _, g_mask = cv2.threshold(g, 0, 255, cv2.THRESH_BINARY)
        _, r_mask = cv2.threshold(r, 0, 255, cv2.THRESH_BINARY) 
        mask = cv2.bitwise_or(red_mask, cv2.bitwise_or(green_mask, blue_mask))
        # NOT USED IN THIS CODE FOR NOW 
        # cv2.drawContours(mask, [contour], -1, 255, -1)
        # __________________***____________________
        # mean_color = cv2.mean(img, mask=mask)[:3]
        # __________________*TAKING MEAN OF EACH CROPED IMAGES FROM WHICH WE ARE ITTRATING *____________________
        mean =cv2.mean(img)[:3]
        # __________________***____________________
        # # b ,g, r =mean_color
        # print("B",b)
        # print("G",g)
        # print("R",r)
        # print("means color ",mean_color)
        # if mean_color[0] > mean_color[1] and mean_color[0] > mean_color[2]:
        #     binary_str += '00'
        # elif mean_color[1] > mean_color[0] and mean_color[1] > mean_color[2]:
        #     binary_str += '01'
        # else:
        #     binary_str += '10'
        # __________________*FINDING COLOR AT CENTER WITH FINDING CENTER OF CONTOURE IMG*____________________
        contour1, herarchy= cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # print(contour1)
        cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
        cv2.imshow('Image with center',img)
        # __________________***____________________
        # crop_contoure = f"img {i}"
        # crop_contoure_gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        # _,thresh1=cv2.threshold(crop_contoure_gray,127,255,cv2.THRESH_BINARY)
        # contour1, herarchy= cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # for n ,cont in enumerate(contour1):
        #     x1, y1, w1, h1 = cv2.boundingRect(cont)
        #     centX = (2 *x1+w1)/2
        #     centY = (2 *y1+h1)/2
        #     # frame = cv2.circle(thresh1, (centX, centY), 5,(0, 0, 255), -1)
        #     # cv2.imshow(f"frame{n}",frame)
        #     print("--------**--------")
        #     print(centX)
        #     print("--------**--------\n")
        #     print(centY)
        #     print("--------**--------")
        #     cv2.waitKey(0)
        #     b ,g,r = cv2.split(cont)
        # cv2.imshow('Image with center', frame)
        # __________________***____________________
        # print("--------*BINARY FORM*--------")
        b ,g ,r = mean
        
        if 200 <= b <= 255 and 200 <= g <= 255 and 200 <= r <= 255:
             s +='1'
             print(" BINARY ==> 1")
        else:
            s += '0'
            print(" BINARY ==> 0")
            
        
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # __________________***____________________
    else:
        print("no contour picture found")
s = int(s)
pr = s
print("\n\n", type(s))

decimal, i = 0, 0
while(s!= 0):
    dec = s % 10
    decimal = decimal + dec * pow(2, i)
    s = s//10
    i += 1

print("Decimal equivalent to ",pr, " = ",decimal)

print("--------*PROGRAM ENDED *--------\n")
cv2.destroyAllWindows()
#  Date : sun 12 march 2023 4:51pm