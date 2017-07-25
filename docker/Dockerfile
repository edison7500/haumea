FROM        python:3.6
MAINTAINER	jiaxin	<jiaxin@bichengidea.com>
RUN         apt-get clean
RUN         apt-get update --fix-missing && apt-get -y install libopencc-dev gcc make supervisor \
                    libmysqlclient-dev git
RUN         ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
                echo "Asia/Shanghai" > /etc/timezone
COPY        requirements.txt /tmp/requirements.txt
COPY		gunicorn /etc/default/gunicorn
COPY        supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ENV         DJANGO_SETTINGS_MODULE="haumea.settings.production"

RUN         pip install -r /tmp/requirements.txt
VOLUME		["/data/www/haumea", "/data/static/haumea ", "/tmp/haumea"]
WORKDIR     /data/www/haumea
EXPOSE 		8000
CMD         ["/usr/bin/supervisord"]