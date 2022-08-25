from flask import Flask, request, render_template
import os
import cv2 as cv
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)

# folder where the images are stored
image_folder = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = image_folder

@app.route('/')
def detect():
    return render_template('home.html')

@app.route('/detect', methods=['POST'])
def detect_post():
    img = request.files['image']
    # Extracting uploaded data file name
    img_filename = secure_filename(img.filename)
    image = os.path.join(app.config['UPLOAD_FOLDER'], img_filename)
    result_image = crosswalk_detection(image)
    IMG_LIST = [image, result_image]

    return render_template('show_image.html', imagelist=IMG_LIST)

def crosswalk_detection(image):
    # loading yolo config file and yolo trained model
    net = cv.dnn.readNetFromDarknet("yolo-files\custom_yolov3_10000.cfg","yolo-files\custom_yolov3_10000.weights") 
    # classes for trained model 
    classes = []
    with open('yolo-files\classes.names','r') as f:
        classes = [line.strip() for line in f.readlines()]   

    # image to be detected
    test_img = cv.imread(image)    
    height,width,_ = test_img.shape

    # convert the image to yolo format
    blob = cv.dnn.blobFromImage(test_img, 1/255,(416,416),(0,0,0),swapRB = True,crop= False)
    net.setInput(blob)
    last_layer = net.getUnconnectedOutLayersNames()
    layer_output = net.forward(last_layer)

    boxes =[]
    confidences = []
    class_ids = []
    
    for output in layer_output:
        for detection in output:
            score = detection[5:]
            class_id = np.argmax(score)
            confidence = score[class_id]
            if confidence > 0.6:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3]* height)
                
                x = int(center_x - w/2)
                y = int(center_y - h/2)
                
                boxes.append([x,y,w,h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)

    # find the bounding box
    indexes = cv.dnn.NMSBoxes(boxes,confidences,.6,.4)     
    font = cv.FONT_HERSHEY_PLAIN 
    if  len(indexes)>0:
        for i in indexes.flatten():
            x,y,w,h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i],2))
            cv.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),2)
            cv.putText(test_img,label + " " + confidence, (x,y),font,2,(255,255,255),2)   

    # save the resulting image 
    result_path = os.path.join(app.config['UPLOAD_FOLDER'], 'result.jpg')
    cv.imwrite(result_path, test_img)        
       
    return result_path

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)    