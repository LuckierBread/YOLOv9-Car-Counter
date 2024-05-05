<a target="_blank" href="https://colab.research.google.com/github/LuckierBread/YOLOv9-Car-Counter/blob/main/Yolov9_Car_Counter.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

**into**

This project is a demonstration of how a YOLO v9 algorithm can be used to visually process real-time images from camera sources and process them into resolvable data.
In this implementation, I will be using the Ultralytics library as a fast means of implementing YOLO v9.
This YOLO model was trained on the MS COCO dataset and can identify several objects related to our traffic goals namely cars, trucks, and motorcycles.
We will also use object tracking to keep track of which vehicles are traveling in which direction.

![alt text](https://github.com/LuckierBread/YOLOv9-Car-Counter/blob/main/Demo.PNG)

**problem data**
Webcam data was used as the input for this project.
each frame was (384,640,3) with each number representing height width and number of color channels respectively. 
