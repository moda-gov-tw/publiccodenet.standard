#!/bin/bash
docker run -d \
    -v ./:/var/www/html \
    -p 8090:80 \
    --name=standard \
    steps/standard
