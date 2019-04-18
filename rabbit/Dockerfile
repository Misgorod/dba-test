FROM debian:stretch
RUN apt update && \
    apt install -y wget dpkg gnupg2
WORKDIR /data
COPY rabbit_install.sh /data
RUN ./rabbit_install.sh
CMD rabbitmq-server