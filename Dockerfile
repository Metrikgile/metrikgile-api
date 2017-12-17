FROM python:3

RUN mkdir /metrikgile
WORKDIR /metrikgile/

ADD requirements.txt /metrikgile/
RUN pip3 install -r requirements.txt

ADD . /metrikgile/
