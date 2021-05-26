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
WORKDIR /home/modsi
COPY ./requirements.txt /home/modsi/requirements.txt
RUN pip install -r requirements.txt

#Copy necessary files to environment
COPY ./db /home/modsi/db
COPY ./templates /home/modsi/templates
COPY ./static /home/modsi/static
COPY ./database_conn.py /home/modsi/database_conn.py
COPY ./app.py /home/modsi/app.py

EXPOSE 65200
CMD [ "/bin/bash","-c","python3 app.py"]