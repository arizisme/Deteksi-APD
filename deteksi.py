from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2

model= YOLO("DeteksiAPD.pt")

results = model.predict(source="0", show=True)

print(results)