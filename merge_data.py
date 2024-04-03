import os

DATASET_LABEL = './datatset/VOC2028/Labels/'
YOLO_LABEL = './datatset/label/'

if __name__ == "__main__":
    yolo_dirs_list = os.listdir(YOLO_LABEL)

    for file_name in yolo_dirs_list:

        file_path = YOLO_LABEL + file_name

        with(open(file_path, "r")) as f:
            for line in f.readlines():
                if line.split()[0] != '0':
                    continue
                data_path = DATASET_LABEL + file_name
                print(data_path)
                # 汇总到数据集的标注文件
                with open(data_path, "a") as fd:
                    fd.write(line)
