Docker Basic Commands

install docker on linux:sudo yum -y update ; sudo yum install -y docker

start : service docker start

version: docker version

help: docker --help

login in hub.docker.com: docker login

Lists containers : docker ps -a

list images: docker images

run container: docker run -ti ubuntu bash

remove unused data\(images and containers \): docker system prune

