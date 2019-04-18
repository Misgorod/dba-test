FROM python:3
WORKDIR /data
COPY test.py requirements.txt /data/
RUN pip install -r requirements.txt
CMD python test.py