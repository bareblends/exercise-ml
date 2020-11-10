# bb-ml-exercise
###
Reading:
- https://www.tensorflow.org/tutorials/keras/classification
- https://www.tensorflow.org/tutorials/images/classification
## Goal

To use a gyroscope to capture exercise data and classify this data using tensorflow.

### Gyroscope data:
Readings are made with Sensor Node Free available for free on the Android play Store.
- [ ] Create our own simple tcp server.

At the moment readings are read using the listen_server.py file: port 50000

you will have to specify the name of the file the data is dumped to in listen_server.py

### Making a Graph with the data:

make_image.py <filename.csv>
This python script creates a matplotlib graph, with the x and y axis removed. This is used as the image.
Currently on my machine the size of the image is 1600x1200 but it may be different on yours.

### Slicing the data:

frame.py <filename.csv>

The data is currently sliced with frame.py:

float(row[1]) - X axis
float(row[2]) - Y axis
float(row[3]) - Z axis

Each kind of exercise is requires different method to slice. 

For Squats I currently take a snapshot of the peak by measuring all values from -0.6 on the x-axis until it comes back down to -0.6. This makes a nice peak formation.

For knees-up-to-hands exercise I measure from the Y-axis and start the measurement from 0.0 until it loops back to 0.0 although this is still being worked out.

- [ ] Each exercise needs its own method to slice.
( Note: there may be a normalisation algorithm we can use instead)

### Training the model:

run using train.py

### Predicting values:

Once the data is trained you can run: predict.py <PathToDir> 
  where <PathToDir> is the directory that contains the images you want to match.
  


