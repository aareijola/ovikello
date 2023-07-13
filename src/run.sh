#!/bin/bash
hostname=$(hostname -I)
echo Running server. Your ip address is: $hostname
python -m http.server 6969 --cgi