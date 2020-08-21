import cv2
import numpy as np


class MotionDetection:
    def __init__(self):
        self._backgroundSubtractor = cv2.bgsegm.createBackgroundSubtractorMOG()
        self._noiseSize = (3, 3)

    def process(self, frame):
        color = (57, 255, 20)
        background = self._backgroundSubtractor.apply(frame, 0.2)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, self._noiseSize)
        cv2.threshold(background, 128, 128, cv2.THRESH_BINARY_INV)
        cv2.erode(background, kernel)
        cv2.dilate(background, kernel, iterations=2)
        contours, hierarchy = cv2.findContours(background, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for r in contours:
            x, y, w, h = cv2.boundingRect(r)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        return len(contours), frame

    def __del__(self):
        cv2.destroyAllWindows()


if __name__ == '__main__':
    cap = cv2.VideoCapture('../Datasets/fourway.avi')
    m = MotionDetection()
    while True:
        ret, f = cap.read()
        f = cv2.resize(f, None, fx=0.3, fy=0.3)
        count, show = m.process(f)
        cv2.imshow('frame', show)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
