import cv2
# read from file : cap = cv2.VideoCapture("test.mp4")
cap = cv2.VideoCapture(0)  # mac 0, usbcam 1
while True:
    ret, frame = cap.read()

    # show the output frame
    cv2.imshow("frame", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("s"):  # save
        screenshot_name = "test.jpg"
        cv2.imwrite(screenshot_name, frame)  # cv2.imread
        print(f'screenshot: {screenshot_name}')
    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()