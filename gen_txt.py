from ultralytics import YOLO

DATA_PATH = "./datatset/yolo_type/images"

TRAIN_DATA_PATH = DATA_PATH + "/train"
TEST_DATA_PATH = DATA_PATH + "/test"
VAL_DATA_PATH = DATA_PATH + "/val"


model = YOLO('yolov8n.pt')

# Run inference on 'bus.jpg' with arguments
# model.predict(source=TRAIN_DATA_PATH, save_txt=True, imgsz=320, conf=0.5)
# model.predict(source=TEST_DATA_PATH, save_txt=True, imgsz=320, conf=0.5)
model.predict(source=VAL_DATA_PATH, save_txt=True, imgsz=320, conf=0.5)
