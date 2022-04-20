FROM python:3.9-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN git clone https://github.com/200920082007/TigerShroff
RUN /bin/sh -c pip install
RUN mkdir /TigerShroff
WORKDIR /TigerShroff
COPY start.sh /start.sh
CMD ["/bin/bash", "/start.sh"]
