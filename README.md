Official images for python seem to be found at:

https://github.com/docker-library/python/blob/1dcbfcceba5dc2d3ebf0a414926f2645aec0150e/3.7-rc/alpine3.7/Dockerfile

Used is the 3.6.4-slim
See https://docs.docker.com/get-started/part2/#dockerfile for info,
do note they use python 2.x

Building the image / e.g. the container mold: 
docker build -t bookings-base .

Running the image / e.g. creating a concrete container:
docker run bookings-base

Options have suggested build -e DISPLAY:$DISPLAY -v [some tmp/x11.. folders] to share the display, but randr threw errors



See https://gist.github.com/Hell0w/84513beda0b8bada8b5323afc3e491d9 as an alt to image grab

https://python-mss.readthedocs.io/examples.html#one-screen-shot-per-monitor

https://stackoverflow.com/questions/29217543/why-does-this-solve-the-no-display-environment-issue-with-matplotlib

http://fabiorehm.com/blog/2014/09/11/running-gui-apps-with-docker/
https://linuxmeerkat.wordpress.com/2014/10/17/running-a-gui-application-in-a-docker-container/

https://pythonprogramming.net/canny-edge-detection-gradients-python-opencv-tutorial/

createBackgroundSubtractorMOG2 - an opencv fn to reduce bg
