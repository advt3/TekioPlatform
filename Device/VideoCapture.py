import base64
import cv2
from Transport.MqttPublisher import Publisher
import logging

def play(file):
    cap = cv2.VideoCapture(file)
    p = Publisher('topic/video')
    while True:
        ret, frame = cap.read()
        if frame is None:
            break
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
        encoded, buffer = cv2.imencode('.jpg', frame)
        message = base64.b64encode(buffer)
        p.send_message(message)
    cap.release()
    p.send_message('eof')
    logging.info('finished sending video')


if __name__ == '__main__':
    filename = '../Datasets/fourway.avi'
    play(filename)
