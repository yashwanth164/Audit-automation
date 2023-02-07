#!/bin/bash

# Set the file to be read
file="/home/kali/Desktop/iplist.txt"

# Use a while loop to read the file line by line
while read line; do
	#Scanning each IP using nmap
	ping_output=$(ping -c 1 $line)
	if echo "$ping_output" | grep -q "ttl=128"; then
	  	echo "able to ping $line initiating nmap scan\n"
	  	sudo nmap -sV -O -v  $line -oN "/home/kali/Desktop/SCAN outputs/$line" 2>&1
	else
		echo "$line is not accessible\n"
	fi
  	echo $line
done < $file

