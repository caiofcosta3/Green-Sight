# IMPORTS
import cv2
import time


# CARREGA CLASSES
class_names = ['bueiro']

#with open("bins/coco.names", "r") as f:
#    class_names = [cname.strip() for cname in f.readlines()]

# CARREGA VIDEO
cap = cv2.VideoCapture("video.mp4")

# CARREGA A REDE NEURAL
net = cv2.dnn.readNet("C:\\Yolo Opencv\\bins\\yolov4-tiny-obj_last.weights", "C:\\Yolo Opencv\\bins\\yolov4-tiny-obj.cfg")

#net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
#net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)


# SETAR PARAMETROS DA REDE
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416,416), scale=1/255)


# RODAR O VIDEO
while True:

    # PEGAR A IMAGEM DO VIDEO O FRAME
    _, frame = cap.read()

    start = time.time()

    #DETECÇÃO
    classes, scores, boxes = model.detect(frame, 0.7, 0.4)

    end = time.time()

    # PERCORRER TODAS AS DETECÇÕES
    for (classId, score, box) in zip(classes, scores, boxes):
        label = f"{class_names[classId]} {score}"
        cv2.rectangle(frame, box, (0,255,0), 2)
        cv2.putText(frame, label, (box[0], box[1]-10), 0, 0.5, (0,255,0), 2) # 0 = font, 0.5= tamanho font, cor da font, espessura do texto

    fps = f"FPS {round(1/(end-start), 2)}"

    cv2.putText(frame, fps, (20,20), 0, 0.5, (0,255,0), 2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()