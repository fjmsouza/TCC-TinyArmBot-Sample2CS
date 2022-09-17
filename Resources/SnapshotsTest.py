import cv2

import Determinant
import StatusScreen
import time
import numpy as np

def flushLoadCamera():
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
    return frame

cam = cv2.VideoCapture(1 + cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cam.set(cv2.CAP_PROP_BUFFERSIZE, 1);

cv2.namedWindow("test")

img_counter = 0
fp1 = None
fp2 = None

while True:

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        print("starting test")
        frame = flushLoadCamera()
        cv2.imshow("1", frame)

        # cv2.imshow("foto1 processada", fp1)
        print("foto 1 tirada!!")

        time.sleep(10)

        frame2 = flushLoadCamera()
        cv2.imshow("2", frame2)
        print("foto 2 tirada!!")

        fp1 = StatusScreen.preprocess(frame)
        fp2 = StatusScreen.preprocess(frame2)
        # cv2.imshow("foto2 processada", fp2)

        # calculate difference and update previous frame
        diff_frame = cv2.absdiff(src1=fp1, src2=fp2)
        cv2.imshow("diff ", diff_frame)

        # 4. Dilute the image a bit to make differences more seeable; more suitable for contour detection
        kernel = np.ones((5, 5))
        diff_frame = cv2.dilate(diff_frame, kernel, 3)
        cv2.imshow("diff + dilate ", diff_frame)

        # 5. Only take different areas that are different enough (>20 / 255)
        thresh_frame = cv2.threshold(src=diff_frame, thresh=15, maxval=255, type=cv2.THRESH_BINARY)[1]
        # thresh_frame = cv2.adaptiveThreshold(diff_frame, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 3)
        # ret, thresh_frame = cv2.threshold(diff_frame, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # frame = cv2.bilateralFilter(frame, 20, 200, 250)
        cv2.imshow("diff + dilate + thres ", thresh_frame)

        contours, _ = cv2.findContours(image=thresh_frame, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if cv2.contourArea(contour) < 10:
                # too small: skip!
                continue
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(img=frame, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=2)

        cv2.imshow("diff detector", frame)
        # fp1 = Determinant.determinant(fp1)
        # fp2 = Determinant.determinant(fp2)
        # if fp1 == fp2:
        #     print("iguais")
        # else:
        #     print("diferentes")
        #     print(fp1)
        #     print(fp2)


cam.release()

cv2.destroyAllWindows()