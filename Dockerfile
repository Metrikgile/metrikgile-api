FROM python:3

WORKDIR /metrikgile/

ADD requirements.txt /metrikgile/
RUN pip3 install -r requirements.txt

ADD . /metrikgile/

CMD ["python3","manage.py","runserver"]
