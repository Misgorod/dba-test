FROM debian:stretch
RUN apt update && \
    apt install -y gnupg2
WORKDIR /data
COPY mongo_install.sh /data
RUN ./mongo_install.sh
CMD mongod
