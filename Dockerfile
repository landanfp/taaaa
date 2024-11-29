FROM python:3.10.8

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt
RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN pip3 install pyrogram 
RUN mkdir /test
WORKDIR /test

CMD python3 bot.py
