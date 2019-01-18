FROM python:latest

RUN mkdir -p /opt/app

COPY . /opt/app
WORKDIR /opt/app

RUN pip install -r requirements.txt

EXPOSE 5000
ENV FLASK_APP=entry.py

CMD exec gunicorn entry:app -w 4 -b 0.0.0.0:5000
