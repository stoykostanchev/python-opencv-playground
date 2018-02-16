Official images for python seem to be found at:

https://github.com/docker-library/python/blob/1dcbfcceba5dc2d3ebf0a414926f2645aec0150e/3.7-rc/alpine3.7/Dockerfile

Used is the 3.6.4-slim
See https://docs.docker.com/get-started/part2/#dockerfile for info,
do note they use python 2.x

Building the image / e.g. the container mold: 
docker build -t bookings-base .

Running the image / e.g. creating a concrete container:
docker run -p 4000:80 bookings-base



