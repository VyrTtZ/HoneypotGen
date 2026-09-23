#!/bin/bash
curl -fsSL https://docker.com -o get-docker.sh
sudo sh get-docker.sh

sudo systemctl enable docker
sudo systemctl start docker


#ip addres
ip addr show | while read line
do
#gets the ip + subnet mask
	ip addr show scope global | grep -E  '[0-9]{1,3}\.[0-9]{1-3}\.[0-9]{1-3}\.[0-9]{1,3}/[0-9]{1-2}'
#gets the name of u NIC
ip addr show scope global | grep -E 'wlp.*\:' 2>/dev/null
