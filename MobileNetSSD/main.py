import cv2
import time
import numpy as np


with open('object_detection_classes_coco.txt', 'r') as f:
   class_names = f.read().split('\n')

print(class_names)
 
colors = np.random.uniform(0, 255, size=(len(class_names), 3))
 
model = cv2.dnn.readNet(model='ssd_mobilenet_v2_coco_2018_03_29.pb', config='ssd_mobilenet_v2_coco_2018_03_29.pbtxt.txt', framework='TensorFlow')
min_confidence_score = 0.6

# cap = cv2.VideoCapture("Footage.mp4")
cap = cv2.VideoCapture(0)

while cap.isOpened():

    success, img = cap.read()

    imgHeight, imgWidth, channels = img.shape

    blob = cv2.dnn.blobFromImage(img, size=(300,300), mean=(104,117,123), swapRB=True)

    start = time.time()

    model.setInput(blob)

    output = model.forward()
 
    end = time.time()

    fps = 1 / (end-start)

    for detection in output[0,0,:,:]:

        confidence = detection[2]

        if confidence > min_confidence_score:

            class_id = detection[1]

            class_name = class_names[int(class_id)-1]
            color = colors[int(class_id)]

            bboxX = detection[3] * imgWidth
            bboxY = detection[4] * imgHeight

            bboxWidth = detection[5] * imgWidth
            bboxHeight = detection[6] * imgHeight

            cv2.rectangle(img, (int(bboxX), int(bboxY)), (int(bboxWidth), int(bboxHeight)),color, thickness=2)

            cv2.putText(img, class_name, (int(bboxX), int(bboxY - 5)), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.putText(img, f"{fps:.2f} FPS", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow('image', img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
