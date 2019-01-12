FROM alpine

RUN apk update && \
    apk add --no-cache \
    python3 \
    python3-dev \
    build-base \
    linux-headers \
    pcre-dev \
    bash \
    git \
    openssh && \
    python3 -m pip install --upgrade pip && \
    pip3 install --upgrade setuptools && \
    rm -r /root/.cache

COPY ./requirements.txt /home/www-data/app/requirements.txt

RUN pip3 install --no-cache-dir virtualenv && \
    virtualenv /home/www-data/app/env && \
    source /home/www-data/app/env/bin/activate && \
    pip install --no-cache-dir https://github.com/unbit/uwsgi/archive/uwsgi-2.0.zip#egg=uwsgi && \
    pip install --no-cache-dir -r /home/www-data/app/requirements.txt && \
    addgroup -g 1000 -S www-data && \
    adduser -u 1000 -S www-data -G www-data && \
    chown -R www-data:www-data /home/www-data/*

COPY ./ /home/www-data/app

USER www-data
ENV HOME /home/www-data/app
WORKDIR /home/www-data/app

ENTRYPOINT ["/home/www-data/app/env/bin/uwsgi", "--ini", "uwsgi.ini"]
# ENTRYPOINT ["/home/www-data/app/env/bin/python", "main.py"]
# ENTRYPOINT ["bash"]