# YOLOv9 Car Counter

This project is a demonstration of how a YOLO v9 algorithm can be used to visually process real-time images from camera sources and process them into resolvable data.
In this implementation, I will be using the Ultralytics library as a fast means of implementing YOLO v9.
This YOLO model was trained on the MS COCO dataset and can identify several objects related to our traffic goals namely cars, trucks, and motorcycles.
We will also use object tracking to keep track of which vehicles are traveling in which direction.

![alt text](https://github.com/LuckierBread/YOLOv9-Car-Counter/blob/main/Demo.PNG)

## How to run
Click the Google Colab badge to get redirected to the Colab implementation.

<a target="_blank" href="https://colab.research.google.com/github/LuckierBread/YOLOv9-Car-Counter/blob/main/Yolov9_Car_Counter.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

Run the notebook by clicking the play buttons on each code chunk, making sure you run them from top to bottom.
when the final code section is done, open the "files" folder on the left side of the screen.
Navigate to the "YOLOv9_Car_Counter" folder and download output.avi this will output the processed video
