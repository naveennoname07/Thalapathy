FROM python:3.9.1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN mkdir /app
WORKDIR /app
COPY . .
CMD python3 bot.py
