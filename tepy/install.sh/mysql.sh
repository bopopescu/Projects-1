#!/bin/bash
yum install -y    vim  openssl openssl-devel epel-release make m4  autoconf bzip2 bzip2-devel gcc curl-devel libjpeg-devel libpng-devel freetype-devel gmp-devel pcre-devel glib2-devel libxml2  libxml2-devel  gcc-c++ wget gdb php-mcrypt cloud-init libmcrypt libmcrypt-devel psmisc cpp zlib-devel curl gd gd-devel mhash-devel  libevent-devel libmcrypt libtermcap-devel ncurses-devel GeoIP GeoIP-devel lua lua-devel  libcurl libcurl-devel libpcap-devel libpcap openssl-libs git nc nmap-ncat

wget http://119.9.108.199:3357/iso//boost/boost_1_59_0.tar.gz
wget https://cmake.org/files/v2.8/cmake-2.8.0.tar.gz
wget http://119.9.108.199:3357/iso/mysql/mysql-5.6.30.tar.gz 
tar xvf mysql-5.6.30.tar.gz
tar xvf boost_1_59_0.tar.gz
tar xvf cmake-2.8.8.tar.gz
cd  cmake-2.8.8 
./configure
make&&make install &&cd ..
cd  mysql-5.6.30
cmake -DCMAKE_INSTALL_PREFIX=/usr/local/mysql -DSYSCONFDIR=/etc -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_general_ci -DDEFAULT_CHARSET=utf8mb4 -DDEFAULT_COLLATION=utf8mb4_general_ci -DEXTRA_CHARSETS=all -DWITH_INNOBASE_STORAGE_ENGINE=1 -DWITH_ARCHIVE_STORAGE_ENGINE=1 -DWITH_MYISAM_STORAGE_ENGINE=1 -DWITH_BLACKHOLE_STORAGE_ENGINE=1 -DWITH_FEDERATED_STORAGE_ENGINE=1 -DWITH_PARTITION_STORAGE_ENGINE=1 -DENABLE_DTRACE=0 -DMYSQL_TCP_PORT=3306 -DENABLE_DOWNLOADS=1 -DENABLED_LOCAL_INFILE=1 -DWITH_EMBEDDED_SERVER=1 -DWITH_BOOST=/root/boost_1_59_0
make &&make install
cd ..

