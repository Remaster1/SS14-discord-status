FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN apt-get update
RUN apt-get upgrade -y
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT ["python3", "-m", "main.py"]