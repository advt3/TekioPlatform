import cv2
import base64
from VideoSenderClient import Client


def play(file):
    c = Client('127.0.0.1', 50101)
    cap = cv2.VideoCapture(file)
    while True:
        ret, frame = cap.read()
        if frame is None:
            break
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5)

        # cv2.imshow('Player', frame)
        encoded, buffer = cv2.imencode('.jpg',frame)
        message = base64.b64encode(buffer)
        c.send(message)
        print('sended')
        if cv2.waitKey(33) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    filename = '../Datasets/crosswalk.avi'
    play(filename)
