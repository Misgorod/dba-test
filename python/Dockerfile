FROM python:3
WORKDIR /data
COPY requirements.txt /data/
RUN pip install -r requirements.txt
COPY src /data/
ENV HOST_IP=0.0.0.0
ENV HOST_PORT=5000
CMD gunicorn --bind ${HOST_IP}:${HOST_PORT} wsgi:app