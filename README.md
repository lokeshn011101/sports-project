# Table Tennis Stroke Detection and Classification

## Setting up the project
1. Download the data (33gb) from the email.(Private)
2. Clone https://github.com/ultralytics/yolov5 into the present working directory
3. Add a new folder "imagedata"
    1. Add two more folders "images" and "labels" ````(imagedata/images, imagedata/labels)````.
    2. Add "train" folder under both images and labels ````(imagedata/images/train, imagedata/labels/train)````
    3. Put all the labels from CVAT into the ````imagedata/labels/train```` folder
4. Run main.ipynb.
5. Create ```image.yaml``` in the yolov5 directory.
    1. Add the below contents to the file
```
path: imagedata/
train: images/train
val: images/train
nc: 1
names: ["stroke"]
```    
6. Then run:
    1. ```cd yolov5```
    2. For training: ```python train.py --img 1024 --batch 1 --epochs 1 --data image.yaml```
    3. For detection: ```python detect.py --source ../data/videos/71023710613.mp4 --weights best.pt```
7. The output video can be viewed in the folder ```./yolov5/runs/detect/exp*```
