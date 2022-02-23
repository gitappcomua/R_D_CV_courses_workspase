## Homework 10

In this homework, you are going to use and compare two different trackers (of your liking) and compare the results.

### Step 1
Decide what video you are going to use for this homework, select an object and generate the template. You can use any video you want (your own, from Youtube, etc.)
and track any object you want (e.g. a car, a pedestrian, etc.).

I used video  data/mixkit-curvy-road-on-a-tree-covered-hill-41537.mp4

### Step 2
Initialize a tracker (e.g. KCF).

I compared two traker from OpenCV, KCF and CSRT

### Step 3
Run the tracker on the video and the selected object. Run the tracker for around 10-15 frames.

### Step 4
For each frame, print the bounding box on the image and save it.

### Step 5
Select a different tracker (e.g. CSRT) and repeat steps 2, 3 and 4.

### Step 6
Compare the results:
* Do you see any differences? If so, what are they?
* Does one tracker perform better than the other? In what way?

I did compare two tracker from OpenCV, KCF and CART. 
The results I have recorded to two files treker_result_KCF.mp4 and treker_result_CSRT.mp4 in accordance.
I see that CSRT more robust than KCF. The KCF lost the object as soon the object changed the position relative to the camera. 
The CSRT treker holded the object, until it hid behind an obstacle. 
But the CSRT is more slower than KCF.
