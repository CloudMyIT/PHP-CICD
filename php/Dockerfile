ARG VERSION
FROM php:${VERSION}-fpm

RUN apt update && apt upgrade -y && \
    apt install -y libxml2-dev wget

# Copy over our script to check if the extension is already installed
COPY ./docker-php-ext-install-check.sh /opt/php-ext-check.sh
# Check and/or Install core modules
RUN /opt/php-ext-check.sh bcmath ctype \
    fileinfo json mbstring openssl pdo tokenizer xml

# Install Composer
# e3e43bde99447de1c13da5d1027545be81736b27 = 04DEC2020
RUN wget https://raw.githubusercontent.com/composer/getcomposer.org/e3e43bde99447de1c13da5d1027545be81736b27/web/installer -O - -q | php -- --quiet

# Install Xdebug
RUN pecl install xdebug \
    && echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini