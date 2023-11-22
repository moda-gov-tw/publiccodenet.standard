#!/bin/bash

path=`pwd`
docker run -d \
    -v ${path}:/var/www/html \
    -v ${path}/docker/apache-data:/etc/apache2/sites-available \
    -p 8090:80 \
    --name=standard \
    steps/standard
