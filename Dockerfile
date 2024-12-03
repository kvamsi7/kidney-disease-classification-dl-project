FROM python:3.8.2-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app/
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt --verbose

CMD [ "python3","app.py" ]