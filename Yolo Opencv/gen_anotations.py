import cv2
import os

classe = 0 # caso for treinar mais classes, trocar o valor por uma lista ex: [0,1,2,3]


boxes = []

x1,y1,x2,y2 = 0,0,0,0

img_original = None

text = ""

def save_all(img, txt):
    name = f"data/{len(os.listdir('data'))}"
    cv2.imwrite(f"{name}.jpg", img)

    f = open(f"{name}.txt", "w+")
    f.write(txt.replace('(', '').replace(')', '').replace(',', ''))

def create_text(txt):
    global text
    text = text+txt

def yolo(img, x1, y1, x2, y2):
    size = img.shape
    dw = 1./size[1]
    dh = 1./size[0]
    x = (x1 + x2)/2.0
    y = (y1 + y2)/2.0
    w = x2 - x1
    h = y1 - y2
    x = abs(x*dw)
    w = abs(w*dw)
    y = abs(y*dh)
    h = abs(h*dh)
    return (x,y,w,h)


def get_box(event,x,y,flags,param):
    global x1,y1,x2,y2,img_original,boxes

    draw_img = img_original.copy()
    if event == 5:
        boxes= []
    if event == 1:
        x1,y1,x2,y2 = 0,0,0,0
        x1 = x
        y1 = y
        x2 = x
        y2 = y
    if flags == 1:
        x2 = x
        y2 = x
    if event == 4:
        boxes.append([(x1,y1),(x2,y2)])
    
    for b in boxes:
        cv2.rectangle(draw_img, b[0],b[1], (0,255,0), 2)
    cv2.rectangle(draw_img, (x1,y1),(x2,y2), (0,255,0), 2)
    cv2.imshow('frame', draw_img)

cv2.namedWindow('frame')
cv2.setMouseCallback('frame', get_box)

files = os.listdir("raw")


for f in files:
    boxes = []
    x1,y1,x2,y2 = 0,0,0,0
    text = ""

    frame = cv2.imread(f"raw/{f}")

    img_original = frame.copy()

    cv2.imshow('frame', frame)

    if cv2.waitKey(0) == 27:
        break

    if len(boxes) > 0:
        for b in boxes:
            create_text(f"{classe} {str(yolo(img_original, b[0][0], b[0][1], b[1][0], b[1][1]))}\n")
        save_all(img_original, text)        
    
cv2.destroyAllWindows()