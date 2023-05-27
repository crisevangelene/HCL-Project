import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1150)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # to get the centre of the frame
    height, width, _ = frame.shape

    cx = int(width / 2)
    cy = int(height / 2)

    # Pick pixel value
    pixel_center = hsv_frame[cy, cx]
    h, s, v = pixel_center

    if h < 180 and s < 255 and v < 30 and h > 0 and s > 0 and v> 0:
        color = 'black'
    elif h < 180 and s < 18 and v < 255 and h > 0 and s > 0 and v> 231:
        color = 'white'
    elif h < 180 and s < 255 and v < 255 and h > 159 and s > 50 and v> 70:
        color = 'red'
    elif h < 9  and s <55 and v < 255 and h > 0 and s > 50 and v> 70:
        color = 'red'
    elif h < 89 and s <255 and v < 255 and h > 36 and s > 50 and v> 70:
        color = 'green'
    elif h < 128 and s < 255 and v < 255 and h > 90 and s > 50 and v> 70:
        color = 'blue'
    elif h < 35 and s <255 and v < 255 and h > 25 and s > 50 and v> 70:
        color = 'yellow'
    elif h < 158 and s < 255 and v < 255 and h > 129 and s > 50 and v> 70:
        color = 'pink'
    elif h < 24 and s <255 and v < 255 and h > 10 and s > 50 and v> 70:
        color = 'orange'
    elif h < 180 and s < 18 and v < 230 and h > 0 and s > 0 and v> 40:
        color = 'gray'

    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    cv2.putText(frame, color, (10, 70), 0, 2, (b, g, r), 2)
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
