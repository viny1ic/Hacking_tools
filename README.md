# Hacking_tools
## This repository contains hacking tools I made using Python.

## Mac changer tool:
changes the mac address for your linux machine

## IP tracker:
tracks the target's location using his IP address
## Keylogger
stores the keystrokes of the user

## Network scanner
scans the network and returns the IP and MAC addresses of other systems in the defined IP range. \
run as root \
unstable (might give wrong output)

## reverse connection malware and handler
reverse TCP payload and Handler using sockets \
run server.py for the handler and the client.py for payload \
execute shell commands on victim \
tested on ubuntu and kali \
currently works on LAN only \
executes most commands but is buggy for a few commands

## ransomware
ransomware built on the reverse TCP connection malware


## hashcat.ipynb
Using hashcat on google colab to take advantage of their GPUs for super fast password cracking
