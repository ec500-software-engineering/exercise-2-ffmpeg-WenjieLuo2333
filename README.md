# python-CI-template
Python CI template for EC500 Software Engineering
<br/>
# Build Instruction
Excute ```python main.py``` to start the convertor.
Excute ```python test.py``` to start the test.
And a file consist of videos' path is need. Each line has one path for a video.

# Threads Definition
Three threads work seperately and communicate with each via specific queue to implement the whole process.<br/>
Theads are defined in ```Threads.py```.
### Input Thread
Input Thread get a file to read video lists and save them into a queue.
### 720p Processing Thread
Get video path from a queue and then convert it into 720p/2M bitrates. 
###  480p processing Thread
Same as 720p Thread but convert videos into 480p/1M bitrates.
