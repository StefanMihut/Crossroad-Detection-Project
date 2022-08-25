
## Crosswalk detection 

### Description  
Object detection is one of the fundamental problems in the field of artificial intelligence. It has lots of applications in robotics, automation, and human-computer interaction. The aim of the project is to identify a crosswalk object by localizing it inside bounding boxes. We used the yolov3 pretained object detection model and customised it to detect the crosswalk. 

### Usage
1. `generate_annotation.ipynb` file is used to create the label for each of the images according to the yolo format.
2. The `static\images` folder contains the images that are used for testing.
3. The `yolo-files` folder contains files required to train the and test the model
4. The `templates` folder contains all the html pages used in the application.
5. `app.py` is the main python program that runs the application.
6. `training_yolov3.ipynb` is the file used to train the model in the google colab.

### Run Locally  
1. Clone the project  `git clone git@github.com:StefanMihut/Crosswalk-Detection.git`
2. Go to the project directory  `cd Crosswalk-Detection`
3. Install dependencies   `pip install - r requirements.txt`
4. Download trained model with 10.000 Crosswalk pictures.  [Weights 10.000 Trained](https://wetransfer.com/downloads/ef34c320e818294aedd6a5682c831f3920220825075438/8f718f)  and save it in the yolo-files folder.  
5. Run the Model locally `python app.py`.  Click on the link that appears in the command line which will open up in the browser.  
6. Browse the image for testing the detection 
![Browser](https://i.imgur.com/rEnlMcY.png")  

![Browser2](https://i.imgur.com/zfVhRxw.png)  

We advice to place the photos beforehand in ` static\images` folder.    

![Browser3](https://i.imgur.com/ESexIzl.png)  

 
 ### Project 
1. Understand and analyse the image data with the annotation file 
2. Select the pretrained model (yolov3)
3. Label the images according to the yolo requirement.
4. Make the custom config file to detect the `zebra_cross` class.
5. Train the model with subset of images.
6. Test the model for crosswalk detection and check the performance of the model using the `mAP`.
7. Repeat `step 5` and `6` increasing the number of images.
7. Convert the model to a CoreML version to use in the iOS.
8. Create a flask app to test the model locally without the darknet framework.

### Training the model in the google colab  
1. Use the `generate_annotation.ipynb` file to create the labels for the images. Zip the folder
and upload in in the google drive
2. Unzip the folder with images in the google drive
5. Upload both  `classes.txt` , `classes.names`,`create_files.py` and `create_train_test.py` from this repo to the image folder in the drive
6. Open the `create_files.py` and `create_train_test.py` files in the image folder, change the path to the image and run it.
7. Create a new folder `darknet` and clone the darknet repo using `!git clone https://github.com/AlexeyAB/darknet` in the correct folder.
8. In order to use GPU, open the `Makefile` in the darknet folder and change the value of `OPENCV`, `GPU` and `CUDNN` to `1`.
9. build the darknet using `make` command
10. Create a new folder `custom_weight` and download the pretained model from `http://pjreddie.com/media/files/darknet53.conv.74` and upload in this directory.
11. Upload the `custom_yolov3_100000.cfg` config file from this repo in the `darknet/cfg`.
12. Open the `custom_yolov3_100000.cfg` config file and comment the `batch` and subdivisions` under `Testing`
and uncomment those two in the `Training` sections.
13. Create a `backup` folder in the drive. This folder will contain the trained models.
14. Train the model using the command `darknet/darknet detector train training_10000_images/labelled_data.data darknet/cfg/custom_yolov3.cfg custom_weight/darknet53.conv.74 -dont_show -map`. Make sure that the folder names are correct.

