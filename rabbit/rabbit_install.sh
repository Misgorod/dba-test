apt-get update
apt-get install -y wget gnupg2 erlang erlang-nox
add-apt-repository 'deb http://www.rabbitmq.com/debian/ testing main'
wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | apt-key add -
apt-get update
apt-get install -y rabbitmq-server
rabbitmq-server
