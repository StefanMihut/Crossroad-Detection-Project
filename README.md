
# Project:Crosswalk detection 
A project to detect crosswalk for impaired people 

# Team members:
Pragati
Stephan
Soukaina

# Project Summary:
Mission:Create a deep learning model to detect crosswalk for impaired people

# Objectives:
be able to preprocess data for deep learning
be able to train apply and evaluate Yolov4 model with real world data

# Datast:
Dataset from google can be found which consists of 2 zip files all_images folder contains 35000 images  for the training and csv file all_annotations.csv contains the dataset for the preprocessing 

 # files in this repo:
 
 
 # Workflow for this project:
 # Libraries used:
 Tensorflow
 pandas
 numpy
 opencv
 # Step1: installation
 How to Use YOLO
I) Clone the Repository
git clone https://github.com/pjreddie/darknet
II) Compile the Source
We can directly compile the source using make. Just go to the directory where darknet is cloned and run the command:https://github.com/pjreddie/darknet

Full Weight
To get full weights for YOLO V3, download it from https://pjreddie.com/media/files/yolov3.weights
This is the weight trained on full 9000+ classes.
Test YOLO
everything is run using the darknet exeutable file. Suppose we have an image named test.jpeg, then we can try predicting the objects as:
./darknet detect yolov3-tiny.cfg yolov3-tiny.weights test.jpeg
