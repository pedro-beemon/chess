from ultralytics import YOLO
import cv2

model = YOLO("model_.onnx")

img = cv2.imread("pos1.jpg")
results = model.predict(source=img, save=True)  # save predictions as labels

assert len(results[0].boxes) == 32

img = cv2.imread("pos2.jpg")
results = model.predict(source=img, save=True)  # save predictions as labels

print(results)
assert len(results[0].boxes) == 32


def get_vertice(box):
    vertices = box.data.tolist()[0]
    w = vertices[2] - vertices[0]
    h = vertices[3] - vertices[1]
    x = ((w) / 2) + vertices[0]
    y = ((h) / 2) + vertices[1]
    return int(x), int(y), int(w), int(h)


class Peca:
    vertice = 0, 0
    multi = 0

    @property
    def x(self):
        return self.vertice[0]

    @property
    def y(self):
        return self.vertice[1]

    @property
    def w(self):
        return self.vertice[2]

    @property
    def h(self):
        return self.vertice[3]

    def __repr__(self) -> str:
        return f'<{self.vertice}>'

    def __eq__(self, __value: object) -> bool:
        a = self.multi
        b = __value.multi
        return a == b

    def __gt__(self, __value) -> bool:
        return self.multi > __value.multi

    def __lt__(self, __value) -> bool:
        return self.multi < __value.multi


pecas = []
for box in results[0].boxes:
    vertice = get_vertice(box)
    peca = Peca()
    peca.vertice = vertice
    peca.multi = vertice[0] * vertice[1]
    pecas.append(peca)

from IPython import embed

embed(header='')

max_peca = max(pecas)
min_peca = min(pecas)

x = min_peca.x - int(min_peca.w/2)
w = max_peca.x - min_peca.x + max_peca.w
y = min_peca.y - int(min_peca.h/2)
h = max_peca.y - min_peca.y + min_peca.h

# Cropping an image
img = cv2.imread("pos1.jpg")
crop_img = img[y : y + h, x : x + w]
area_utilizavel = (x,y,w,h)
# Save the cropped image

color = (255, 255, 0)

quadrado = w/8 , h/8
wi,hi,_ = crop_img.shape
for i in range(8):
    p_x = int(quadrado[0]*i)
    cv2.line(crop_img,(p_x,0),(p_x,hi-1),color)

    p_y = int(quadrado[1]*i)
    cv2.line(crop_img,(0,p_y),(wi-1,p_y),color)

cv2.imwrite("Cropped Image.jpg", crop_img)
