#Use Python to play GTA 5

###1. Grab screen and show it
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