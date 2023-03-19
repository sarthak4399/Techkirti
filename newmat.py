import cv2

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame, (300, 300))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY_INV)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    max_area = 1000
    max_contour = None
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area and area < 60000:
            max_area = area
            max_contour = contour
    if max_contour is not None:
        cv2.drawContours(frame, [max_contour], -1, (0, 255, 0), 3)
        x, y, w, h = cv2.boundingRect(max_contour)
        crop = frame[y:y+h, x:x+w]
        cv2.imshow("Crop", crop)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break
    cv2.imshow("gray",thresh)
cap.release()
cv2.destroyAllWindows()