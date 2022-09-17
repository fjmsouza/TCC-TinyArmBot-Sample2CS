import cv2

# cam = cv2.VideoCapture(1)
import Ocr

cam = cv2.VideoCapture(1 + cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cam.set(cv2.CAP_PROP_BUFFERSIZE, 1);

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # text = Ocr.applyEasyocr(frame)
        text = Ocr.applyEasyocr(frame)
        print(text)
        # SPACE pressed
        # img_name = "opencv_frame_{}.jpg".format(img_counter)
        # cv2.imwrite(img_name, frame)
        # print("{} written!".format(img_name))
        # img_counter += 1

cam.release()

cv2.destroyAllWindows()