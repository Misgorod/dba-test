wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb
dpkg -i erlang-solutions_1.0_all.deb
echo 'deb http://www.rabbitmq.com/debian/ testing main' >> /etc/apt/sources.list.d/rabbitmq.list
wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | apt-key add -
apt-get update
apt-get install -y erlang erlang-nox rabbitmq-server
