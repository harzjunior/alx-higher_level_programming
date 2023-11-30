#!/bin/bash
# display size of the body of the res
curl -s "$1" | wc -c
