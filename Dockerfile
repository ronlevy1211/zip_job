FROM centos:7

MAINTAINER RonLevy


ENV VERSION 1.2

RUN yum install -y python3 zip unzip

COPY ./zip_job.py /tmp/zip_job.py
COPY ./entrypoint.sh /entrypoint.sh

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ./entrypoint.sh

