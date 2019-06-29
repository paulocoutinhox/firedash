FROM python:3.7

RUN mkdir -p /app/server
COPY server/requirements.txt /app/server/requirements.txt

WORKDIR /app/server

RUN pip install uwsgi
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["uwsgi", "--ini", "/app/server/uwsgi.ini"]