import cv2


def play(file):
    cap = cv2.VideoCapture(file)
    while True:
        ret, frame = cap.read()
        if frame is None:
            break
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
        cv2.imshow('Player', frame)
        if cv2.waitKey(33) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    filename = '../Datasets/crosswalk.avi'
    play(filename)
