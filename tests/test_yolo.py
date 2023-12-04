from ultralytics import YOLO
from PIL import Image
import cv2

model = YOLO("model_.onnx")
# accepts all formats - image/dir/Path/URL/video/PIL/ndarray. 0 for webcam
# results = model.predict(source="0")
# results = model.predict(source="folder", show=True) # Display preds. Accepts all YOLO predict arguments

# from PIL
im1 = Image.open("negativas/1701128875.2898896.jpg")
results = model.predict(source=im1, save=True)  # save plotted images
print(results)
assert len(results[0].boxes) == 2
vertices = results[0].boxes[1].data.tolist()[0]
x = ((vertices[2] - vertices[0]) / 2) + vertices[0]
y = ((vertices[3] - vertices[1]) / 2) + vertices[1]
print(x, y)

from IPython import embed

embed(header='')

# # from ndarray
# im2 = cv2.imread("bus.jpg")
# results = model.predict(source=im2, save=True, save_txt=True)  # save predictions as labels

# # from list of PIL/ndarray
# results = model.predict(source=[im1, im2])
