FROM python:latest
 
COPY . /Test

RUN pip install -r /Test/requirements.txt
WORKDIR /Test
CMD python python.py

