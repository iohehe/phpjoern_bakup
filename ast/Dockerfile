FROM php:7.1-cli
COPY . /phpjoern
WORKDIR /phpjoern

RUN apt-get update && apt-get install -y \
    gcc \
    libxml2-dev \
    make \
    autoconf \
    libtool

COPY php.ini /usr/local/etc/php/php.ini
WORKDIR php-ast
RUN phpize
RUN ./configure --with-php-config=/usr/local/bin/php-config
RUN make && make install
WORKDIR /phpjoern
