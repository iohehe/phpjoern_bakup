FROM ubuntu:14.04
RUN apt-get update && apt-get install -y \
    gcc \
    libxml2-dev \
    make \
    autoconf \
    libtool
ADD php-7.0.0 /tmp/php-7.0.0
WORKDIR /tmp/php-7.0.0
RUN autoconf
RUN ./configure --prefix=/tmp/php-7.0.0/output/
RUN make && make install
RUN cp /tmp/php-7.0.0/php.ini-development /tmp/php-7.0.0/output/lib/php.ini
WORKDIR /tmp/php-7.0.0/php-ast
RUN /tmp/php-7.0.0/output/bin/phpize
RUN ./configure --with-php-config=/tmp/php-7.0.0/output/bin/php-config
RUN make && make install
WORKDIR /tmp/php-7.0.0/phpjoern
