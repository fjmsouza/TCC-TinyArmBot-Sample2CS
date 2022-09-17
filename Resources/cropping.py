# Import packages
import cv2
from easygui import fileopenbox

path_open = fileopenbox(title="choose a picture", multiple=False)
img = cv2.imread(path_open)

print(img.shape) # Print image shape
cv2.imshow("ui",img)
#
# # # Cropping an image
frame_display = img[286:468, 466:1329]
frame_leds = img[530:853, 1202:1502]
frame_lcd = img[678:1019, 271:539]
# #
# #
# # # Display cropped image
cv2.imshow("display", frame_display)
cv2.imshow("leds", frame_leds)
cv2.imshow("lcd", frame_lcd)
# #
# # # Save the cropped image
cv2.imwrite("display.jpg", frame_display)
cv2.imwrite("leds.jpg", frame_leds)
cv2.imwrite("lcd.jpg", frame_lcd)
# #
cv2.waitKey(0)
cv2.destroyAllWindows()