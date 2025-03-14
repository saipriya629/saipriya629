import pyautogui
import numpy
import cv2
import datetime as dt

current_dt = dt.datetime.now().strftime('%d-%m-%Y_%I-%M-%S')
file_name = current_dt + '.mp4'

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(file_name, fourcc, 20.0, (1920, 1080))

while True:
    img = pyautogui.screenshot()
    img_np = numpy.array(img)
    img_rgb = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow('Screen Recorder', img_rgb)
    video.write(img_rgb)

    if cv2.waitKey(1) == ord('q'):
        break