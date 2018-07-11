FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

WORKDIR /app
COPY ./mazebuilder.py mazebuilder.py
COPY ./mazeapp.py mazeapp.py
COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["mazeapp.py"]

