# Use Python to play GTA 5

## Outline of Project
Use Python to read the game screen and be able to self drive along the roads.  
We will use OpenCv along with numpy, PIL and neural networks for machine learning  
then into Tensor Flow to help detect objects around the vehicle.  
By the end, hope to have a self driving car on the streets of GTA 5.

## 1. Grab screen and show it
Some necessary items:  
* pip install numpy  
* pip install matlablib  
* pip install pillow  

OpenCv:  
For windows download [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv)  
Download corresponding .whl file and use 
* pip install on downloaded file

Using Pillow we grab frames of game running in windowed version.  
Then we can show it in seperate window to the game window.  
Color needs to be converted to get it looking the same as the game itself.  
From here we have about 10-12 frames a second.  
Also have a timestamp to check how long screen grabs are taking to see any  
problems that might arise.

## 2 Add greyscale and edge Detection
Did some refactoring.   
Process screen seperately and change to grayscale and do edge detection with Canny
Pass processed image back in  
You can change thresholds in edge detection to get more or less detail.  
For now can see enough, edges, people etc.

## 3 Add key functionality
Can use [keyboard](https://github.com/boppreh/keyboard) to send key scan codes
* pip install keyboard  
  
Scan Codes found [here](http://www.gamespp.com/directx/directInputKeyboardScanCodes.html)  
Using sleep for now to press 1 key howevert this is affecting opencv
too, making it slow

## 4 Region of interest (ROI)
Add in vertices in the image processing to create a region of interest.  
Use this as a mask to find the data or road markings in the area we expect  
and not for example looking in the sky for the road.  
We expect to find the road in the area of the screen.  
The top will be sky and the bottom will be part of the vehicle you  
are driving.  

## 5 Draw some lines

Using [HoughLineP](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html) 
along with [GaussianBlur](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_filtering/py_filtering.html) to smooth the image we can  
draw lines on the image 

## 6 Find lanes
Look for lines with rise. This is to eliminate the horizontal lines  
since they are probably not wanted (at least for now).  
Need to what actual lane and what is not.
WHat set a frame/two lines that are attached to the user/car then form there detect if they   
moving along the lanes we are detecting.  
(going to need better computer, this one is not paying high enough graphics)

## 7 Use the lanes to try steer
Use the lanes to try steer.  
If too close to one side try to turn to the other side.  
Script can now go straight, right and left.
We have a shitty driver for now