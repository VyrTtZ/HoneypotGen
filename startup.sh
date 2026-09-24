#!/bin/bash
curl -fsSL https://docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo yay install nmap
sudo systemctl enable docker
sudo systemctl start docker


#ip addres
ip addr show | while read line
do
#gets the ip + subnet mask
	ip addr show scope global | grep -E  '[0-9]{1,3}\.[0-9]{1-3}\.[0-9]{1-3}\.[0-9]{1,3}/[0-9]{1-2}'
#gets the name of u NIC
ip addr show scope global | grep -E 'wlp.*\:' 2>/dev/null

#ip -o addr | grep "inet\ " | awk '{print $4}'
#prints both loopback and normal ip

#ip -o addr | grep "wl.*" | grep "inet\ " 2>/dev/null | awk '{print $4}'
#prints just the normal IP YIPPEEEE


ip -o addr | grep "wl.*" | grep "inet\ " 2>/dev/null | awk '{print $2}'
#prints just the wireless NIC name YIPEEEEEE

ip -o addr | grep "wl.*" | grep "inet\ " 2>/dev/null | awk '{print $6}'
#prints the default gateway


nmap -sn -T4 -n -PR $(ip -o addr | grep "wl" | awk '/inet / {print $4}')
#prints out the hosts currently on the network, quick scan, no dns lookups, aggresive timing templates
