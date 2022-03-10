FROM python:3.8-slim

WORKDIR /src

COPY app.py /src
COPY main.py /src
COPY requirements.txt /src

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]