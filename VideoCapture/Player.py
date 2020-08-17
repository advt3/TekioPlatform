import base64
import cv2
from Transport.MqttPublisher import Publisher


def play(file):
    cap = cv2.VideoCapture(file)
    p = Publisher('topic/video')
    while True:
        ret, frame = cap.read()
        if frame is None:
            break
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
        #cv2.imshow('Player', frame)
        encoded, buffer = cv2.imencode('.jpg', frame)
        message = base64.b64encode(buffer)
        p.send_message(message)
        if cv2.waitKey(33) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    filename = '../Datasets/Browse1.mpg'
    play(filename)
