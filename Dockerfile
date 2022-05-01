FROM python:3.9.1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY start.sh /start.sh
CMD ["/bin/bash", "/start.sh"]
