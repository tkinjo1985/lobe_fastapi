FROM tensorflow/tensorflow:latest

WORKDIR /work

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    sudo \
    git \
    libopencv-dev \
    opencv-data

RUN pip install --upgrade pip

COPY requirements.txt /work
RUN pip install -r requirements.txt
