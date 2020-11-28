FROM continuumio/miniconda3

WORKDIR /home

ADD . /home

RUN apt-get update -y && \
	apt-get install -y libchromaprint-tools && \
	pip install -r requirements.txt && \
	pip install --no-cache-dir -e . &&\
	cd ..
