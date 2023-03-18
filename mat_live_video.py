# #/bin/sh:python
import cv2
import numpy as np
import os
import time
# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     low_b = np.uint8([5,5,5])
#     high_b = np.uint8([0,0,0])
#     mask = cv2.inRange(frame,)
#     contours, hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_NONE)
#     length =len(contours)

#     if  length >0:
#         c = max (contours,key=cv2.contourArea)
#         M = cv2.moments(c)
#     cv2.drawContours(frame, contours, -1, (0,255,0), 1)
#     cv2.imshow("Mask",mask)
#     cv2.imshow("Frame",frame)
#     if cv2.waitKey(1) & 0xff == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

# ------------**------------ #
cap = cv2.VideoCapture(0)

while (cap.isOpened()):

    ret, frame = cap.read()

    if ret:

        cnv_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        _, thresh = cv2.threshold(cnv_gray, 127, 255, cv2.THRESH_BINARY)

        contours, herarchy = cv2.findContours(
            thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for i, contour in enumerate(contours):

            x, y, w, h = cv2.boundingRect(contour)

            img_crop = frame[y:y + h, x:x + w]

            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)

            filename = f"Contour{i}.jpg"
            cv2.imwrite(f"images/contour/{filename}", img_crop)

            print("--------**--------")
            print(f"--------X,Y,W,H CONTOUR::{i}--------\n")
            print(f"x{i} =>>", x)
            print(f"y{i} =>>", y)
            print(f"w{i} =>>", w)
            print(f"h{i} =>>", h)
            print("--------*END*--------\n")

            f = os.path.join('images/contour', filename)
            img = cv2.imread(f)
            if os.path.isfile(f):
                img = cv2.imread(f)

                hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

                lower_red = np.array([0, 100, 100])
                upper_red = np.array([10, 255, 255])
                lower_green = np.array([50, 100, 100])
                upper_green = np.array([70, 255, 255])
                lower_blue = np.array([110, 100, 100])
                upper_blue = np.array([130, 255, 255])

                red_mask = cv2.inRange(hsv, lower_red, upper_red)
                green_mask = cv2.inRange(hsv, lower_green, upper_green)
                blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)

                b, g, r = cv2.split(img)

                _, b_mask = cv2.threshold(b, 0, 255, cv2.THRESH_BINARY)
                _, g_mask = cv2.threshold(g, 0, 255, cv2.THRESH_BINARY)
                _, r_mask = cv2.threshold(r, 0, 255, cv2.THRESH_BINARY)
                mask = cv2.bitwise_or(
                    red_mask, cv2.bitwise_or(green_mask, blue_mask))
                mean = cv2.mean(img)[:3]
                contour1, herarchy = cv2.findContours(
                    mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                # print(contour1)
                cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
                cv2.imshow('Image with center', img)
                b, g, r = mean
                if 200 <= b <= 255 and 200 <= g <= 255 and 200 <= r <= 255:
                    print(" BINARY ==> 1")
                else:
                    print(" BINARY ==> 0")
                time.sleep(5)
# ------------**------------ #
# import cv2

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     blur = cv2.GaussianBlur(gray, (5, 5), 0)
#     ret, thresh = cv2.threshold(blur,70, 255, cv2.THRESH_BINARY)
#     contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     if contours:
#         max_contour = max(contours, key=cv2.contourArea)
#         x, y, w, h = cv2.boundingRect(max_contour)
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         crop_img = frame[y:y + h, x:x + w]
#         cv2.imshow('cropped', crop_img)
#     cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
#     cv2.imshow('frame',frame)
#     if cv2.waitKey(1) == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
# ------------**------------ #