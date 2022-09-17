# Import packages
import MoveTinyArm
import Ocr
import winsound
import cv2
frequency_error = 1000
frequency_ok = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second

cam = cv2.VideoCapture(1 + cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cam.set(cv2.CAP_PROP_FPS, 15)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cam.set(cv2.CAP_PROP_BUFFERSIZE, 1);

keys = ['0','1','2','3','4','5','6','7','8','9','CONFIRMA','CORRIGE']

def isKey(key):
    # for item in key:
    if key in keys:
        if key == 'CONFIRMA':
            key = 'C'
        if key == 'CORRIGE':
            key = 'G'
        print(key)
        MoveTinyArm.moveTo(key)
        MoveTinyArm.moveTo("H")
        winsound.Beep(frequency_ok,1000)


cv2.namedWindow("Press space to execute OCR")

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)
    k = cv2.waitKey(1)  # tem que ter esse wait pra exibir frame

    if k % 256 == 32:
        print("Starting OCR...")
        key = Ocr.applyEasyocr(frame)
        print(key)

        try:
            isKey(key[0])
        except:
            pass
