
import base64
import cv2
from Transport.MqttPublisher import Publisher
import logging
from datetime import datetime

def play():
    cap = cv2.VideoCapture(0)
    p = Publisher('topic/video')
    counter = 0
    skip_frame = True
    while True:
        ret, frame = cap.read()
        if frame is None:
            break
        counter=counter+1
        if counter%3==0:
            frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
            flipped = cv2.flip(frame, -1)
            now = datetime.now()
            cv2.putText(flipped, str(now),(20, 20), 0, 0.7, (255, 255, 255), 1)
            encoded, buffer = cv2.imencode('.jpg', flipped)
            message = base64.b64encode(buffer)
            p.send_message(message)
        if counter >100:
            counter = 0
    cap.release()
    p.send_message('eof')
    logging.info('finished sending video')


if __name__ == '__main__':
    filename = '../Datasets/fourway.avi'
    play()
