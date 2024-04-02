# 安全帽检测

## 1. 数据集准备
安全帽目标检测数据集来源于[一个github项目](https://github.com/njvisionpower/Safety-Helmet-Wearing-Dataset)，下载下来之后文件夹目录树如下：
```
---VOC2028    
    ---Annotations    # xml文件，保存的图片标签
    ---ImageSets    # 对数据集的划分(训练集，验证集，测试集)
    ---JPEGImages   # 数据集的图片文件
```

使用`gen_data.py`脚本将原始数据集转换为适合yolo格式的数据集，转换后的数据集目录树如下：
```
---yolo_type
    ---images
    ---labels # 标签文件中的种类只有两种,1-head,2-helmet
```
