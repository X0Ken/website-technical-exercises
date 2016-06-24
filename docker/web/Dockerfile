FROM ubuntu:latest
RUN sed -i "s#archive.ubuntu.com#cn.archive.ubuntu.com#g" /etc/apt/sources.list
RUN sed -i "/security.ubuntu.com/d"  /etc/apt/sources.list
RUN (apt-get update && DEBIAN_FRONTEND=noninteractive \
  apt-get install -y build-essential git python python-dev \
  python-setuptools nginx sqlite3 supervisor)
RUN (easy_install pip && pip install uwsgi)
ADD . /opt/flask/

RUN (ln -s /opt/flask/supervisord.conf /etc/supervisor/conf.d/ &&\
  chmod +x /opt/flask/run.sh)

RUN pip install -r /opt/flask/requirements.txt

EXPOSE 8000
CMD ["/opt/flask/run.sh"]
