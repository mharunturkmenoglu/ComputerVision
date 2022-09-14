import threading, time
import cv2
import queue


def detect_object():
    while True:
        print("get")
        frame = input_buffer.get()
        if frame is not None:
            time.sleep(1)
            detection_buffer.put(frame)
        else:
            break
    return


def show():
    while True:
        print("show")
        frame = detection_buffer.get()
        if frame is not None:
            cv2.imshow("Video", frame)
        else:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return


if __name__ == "__main__":

    input_buffer = queue.Queue()
    detection_buffer = queue.Queue()

    cap = cv2.VideoCapture(0)

    for i in range(5):
        t = threading.Thread(target=detect_object)
        t.start()

    t1 = threading.Thread(target=show)
    t1.start()

    while True:
        ret, frame = cap.read()
        if ret:
            input_buffer.put(frame)
            time.sleep(0.025)
        else:
            break

    print("program ended")