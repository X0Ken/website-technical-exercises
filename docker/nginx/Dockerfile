FROM nginx:latest

ADD . /opt/flask/

RUN cp  /opt/flask/flask.conf /etc/nginx/nginx.conf

VOLUME ["/opt/flask/media"]
VOLUME ["/opt/flask/static"]
EXPOSE 80
