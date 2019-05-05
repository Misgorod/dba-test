apt update
apt install -y gnupg2
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
echo "deb http://repo.mongodb.org/apt/debian stretch/mongodb-org/4.0 main" >> /etc/apt/sources.list.d/mongodb-org-4.0.list
apt update 
apt install -y mongodb-org 
mkdir -p /data/db
config="systemLog:
    destination: file
    logAppend: true
    path: /var/log/mongodb/mongod.log
net:
    port: 27017
    bindIp: 0.0.0.0
processManagement:
    timeZoneInfo: /usr/share/zoneinfo
security:
    authorization: 'enabled'"

echo "$config" > /etc/mongod.conf
mongod -f /etc/mongod.conf