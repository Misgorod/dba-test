import os
import re

host_regex = re.compile(
    r'(?:(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.?)+(?:[A-Za-z]{2,6}\.?|'
    r'[A-Za-z0-9-]{2,}\.?)|'
    r'localhost|'
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', re.IGNORECASE)

MONGO_CONF = f"systemLog: \n\
    destination: file \n\
    logAppend: true \n\
    path: /var/log/mongodb/mongod.log \n\
net: \n\
    port: 27017 \n\
    bindIp: 0.0.0.0 \n\
processManagement: \n\
    timeZoneInfo: /usr/share/zoneinfo \n\
security: \n\
    authorization: 'enabled' \n"

MONGO_REPL = f"replication: \n\
    replSetName: 'rs'\n"

def get_mongo(is_replicated):
    return f"apt update \n\
apt install -y gnupg2 \n\
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4 \n\
echo \"deb http://repo.mongodb.org/apt/debian stretch/mongodb-org/4.0 main\" >> /etc/apt/sources.list.d/mongodb-org-4.0.list \n\
apt update  \n\
apt install -y mongodb-org  \n\
mkdir -p /data/db \n\
config=\"{MONGO_CONF + MONGO_REPL if is_replicated else MONGO_CONF}\" \n\
echo \"$config\" > /etc/mongod.conf \n\
mongod -f /etc/mongod.conf \n"

def get_rabbit():
    return f"apt-get update \n\
apt-get install -y wget gnupg2 erlang erlang-nox \n\
add-apt-repository 'deb http://www.rabbitmq.com/debian/ testing main' \n\
wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | apt-key add - \n\
apt-get update \n\
apt-get install -y rabbitmq-server \n\
rabbitmq-server \n"