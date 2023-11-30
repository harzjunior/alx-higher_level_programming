#!/bin/bash
# Displays the size of the body of the response in bytes
size=$(curl -sI "$1" | grep -i Content-Length | awk '{print $2}' | tr -d '\r')
echo "$size"
