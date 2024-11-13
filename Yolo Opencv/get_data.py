# IMPORTS
import cv2


# CARREGA VIDEO
cap = cv2.VideoCapture(0)


# RODAR O VIDEO
while True:

    # PEGAR A IMAGEM DO VIDEO O FRAME
    _, frame = cap.read()

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()