#!/bin/bash
yum install -y    vim  openssl openssl-devel epel-release make m4  autoconf bzip2 bzip2-devel gcc curl-devel libjpeg-devel libpng-devel freetype-devel gmp-devel pcre-devel glib2-devel libxml2  libxml2-devel  gcc-c++ wget gdb php-mcrypt cloud-init libmcrypt libmcrypt-devel psmisc cpp zlib-devel curl gd gd-devel mhash-devel  libevent-devel libmcrypt libtermcap-devel ncurses-devel GeoIP GeoIP-devel lua lua-devel  libcurl libcurl-devel libpcap-devel libpcap openssl-libs git nc nmap-ncat

wget http://php.net/distributions/php-5.6.31.tar.gz
tar xvf php-5.6.31.tar.gz
cd php-5.6.31
 ./configure --prefix=/usr/local/php --with-config-file-path=/usr/local/php/etc --with-mysqli --with-gd --with-iconv --with-zlib --enable-xml --enable-bcmath --enable-shmop --enable-sysvsem --enable-inline-optimization --enable-mbregex --enable-fpm --enable-mbstring --enable-ftp --enable-gd-native-ttf --with-openssl --enable-pcntl --enable-sockets --with-xmlrpc --enable-zip --enable-soap --without-pear --with-gettext --enable-session --with-mcrypt --with-curl --with-freetype-dir --with-jpeg-dir  --with-pdo-mysql  --with-mysql
make &&make install 

