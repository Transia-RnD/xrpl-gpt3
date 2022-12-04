FROM python:3.10-slim

ENV PYTHONUNBUFFERED True

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt

COPY . /app

CMD ["python", "./main.py"]