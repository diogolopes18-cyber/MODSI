FROM python:3.6.9

ARG apache_version=apache2

RUN apt-get update && apt-get install -y \
    software-properties-common \
    ${apache_version} \
    curl \
    git \
    python3-pip \
    nano

RUN pip install --upgrade pip
WORKDIR /home/kpw/
COPY ./requirements.txt /home/kpw/requirements.txt
COPY ./db /home/kpw
RUN pip install -r requirements.txt