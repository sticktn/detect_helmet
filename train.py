from multiprocessing import freeze_support

from ultralytics import YOLO
if __name__ =="__main__":
    freeze_support()

    # Load a model

    model = YOLO('yolov8m.pt')  # build from YAML and transfer weights
    # Train the model
    results = model.train(data='helmet.yaml',epochs=100, imgsz=640)
