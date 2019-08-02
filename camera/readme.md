# readme


# Read from Webcam
```python
import cv2
import numpy as np
# read from file : cap = cv2.VideoCapture("test.mp4")
cap = cv2.VideoCapture(0) # mac 0, usbcam 1
while True:
    ret, frame = cap.read()
   
    # show the output frame
    cv2.imshow("frame", frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
```

### resize 

```python
# import imutils
frame = imutils.resize(frame, width=480) # scratch stage
```

# 典型用例
### 使用按键截图
从视频流中(视频/camera)截图

```python
if key == ord("s"): # save
    cv2.imwrite( "test.jpg", frame ) # cv2.imread
```


### 从远程树莓派中拿到视频流
[imagezmq](https://github.com/jeffbass/imagezmq)

也可以用于控制多个摄像头