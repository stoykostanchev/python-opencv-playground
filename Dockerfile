FROM python:3.4

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

RUN apt-get update -y 
    #&& apt-get install -y gcc \
    #&& apt-get install imagemagick
# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run app.py when the container launches
CMD ["python", "app.py"]
