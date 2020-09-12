from Transport.MqttSubscriber import Subscriber
import cv2
import base64
import numpy as np


def show_image(client, userdata, msg):
    if len(msg.payload) < 4:
        if msg.payload.decode() == 'eof':
            cv2.destroyAllWindows()
        else:
            print('message received', msg.payload)
    else:
        frame = msg.payload
        frame = base64.b64decode(frame)
        frame = np.frombuffer(frame, dtype=np.uint8)
        frame = cv2.imdecode(frame, flags=1)
        #flipped = cv2.flip(frame, -1)
        cv2.imshow('Remote Player', frame)
        cv2.waitKey(30)
    pass

def execute():
    with Subscriber(show_image, 'topic/video','192.168.1.29') as s:
        s.subscribe()

if __name__ == '__main__':
    execute()
