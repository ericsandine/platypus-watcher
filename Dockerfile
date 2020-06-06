FROM python:3.8.3-buster

WORKDIR /app

RUN apt update
RUN apt -y update
RUN apt -y install ffmpeg

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./src /app

CMD ["python", "main.py"]