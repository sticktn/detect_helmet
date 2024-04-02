from ultralytics import YOLO

model = YOLO('yolov8n.pt')

# Run inference on 'bus.jpg' with arguments
model.predict(path='datatset/yolo_type/images/train', save_txt=True, imgsz=320, conf=0.5)