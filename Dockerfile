FROM python:3.9

WORKDIR /python-app

ADD main.py .
COPY files ./files

CMD ["python","./main.py"]

