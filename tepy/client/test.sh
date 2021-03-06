#!/bin/bash
function installPHP(){
       
       yum remove -y php
       yum update -y
       yum install -y  openssl openssl-devel libmcrypt epel-release make libmcrypt-devel.x86_64 m4 autoconf bzip2 bzip2-devel gcc bzip2 libxml2-devel  curl-devel  libjpeg-devel  libpng-devel  freetype-devel  gmp-devel  pcre-devel  glib2-devel  opensssl  libxml2 
	   yum install libxml2-devel  gcc-c++  wget gdb php-mcrypt cloud-init libmcrypt  libmcrypt-devel  psmisc gcc.x86_64 cpp.x86_64 pcre-devel.x86_64 zlib-devel.x86_64  curl.x86_64 curl-devel.x86_64 libmcrypt-devel.x86_64  mysql.x86_64 mysql-devel.x86_64 libxml2-devel.x86_64  gd.x86_64 gd-devel.x86_64 mhash-devel.x86_64  libmcrypt-devel.x86_64 bzip2-devel.x86_64  autoconf.noarch  libevent-devel.x86_64 subversion.x86_64 ntp gcc-c++ libtermcap-devel.x86_64 ncurses-devel.x86_64  GeoIP.x86_64 GeoIP-devel.x86_64  lua.x86_64 lua-devel.x86_64 libcurl.x86_64 libcurl-devel.x86_64  libpcap-devel.x86_64 libpcap.x86_64 openssl-libs.x86_64 openssl-devel.x86_64
       cd
       wget http://mirrors.linuxeye.com/oneinstack/src/php-5.4.45.tar.gz
       service php-fpm stop
         if ［ -d "/usr/local/php" ］;then
               rm -rf /usr/local/php
         fi 
       tar -zxvf php-5.4.45.tar.gz 
       cd php-5.4.45
       ./configure  --prefix=/usr/local/php --enable-fpm --enable-ftp --enable-bcmath --enable-mbstring --enable-shmop --enable-zip --with-bz2 --enable-soap --enable-sockets --with-gettext --with-pcre-dir --with-curl=/usr/include/curl --with-zlib-dir=/usr/include/zlib.h --with-mhash=/usr/include/mhash.h --with-mcrypt=/usr/local/libmcrypt --with-freetype-dir=/usr/local/lib --with-gd --with-jpeg-dir --with-png-dir --enable-gd-native-ttf --with-pear --with-mysql --with-pdo-mysql --enable-debug
       make -j4 && make install
       
       cp /root/php-5.4.45/php.ini-production /usr/local/php/lib/php.ini
       cp /root/php-5.4.45/sapi/fpm/init.d.php-fpm /etc/init.d/php-fpm
       cd /usr/local/php/etc/
       cp php-fpm.conf.default php-fpm.conf
       chmod +x /etc/init.d/php-fpm
       chkconfig --add php-fpm
       service php-fpm start
       ln -s /usr/local/php/bin/php /usr/bin/php
       cd 
       rm -rf php-5.4.45.tar.gz 
       echo "#################################"
       echo "####phpserver install suceess####"
       echo "#################################"
}

function installPHPmemcached(){
       cd 
       wget https://launchpad.net/libmemcached/1.0/1.0.18/+download/libmemcached-1.0.18.tar.gz
       wget http://pecl.php.net/get/memcached-2.2.0.tgz
       yum install -y memcached
       echo "/usr/bin/memcached -d -c 10240 -m 1024 -u root" >>/etc/rc.local
       /usr/bin/memcached -d -c 10240 -m 1024 -u root
       
       tar -zxvf libmemcached-1.0.18.tar.gz 
       cd libmemcached-1.0.18
       ./configure --prefix=/usr/local/libmemcached --with-memcached
       make -j4 && make install
       cd 
       tar -zxvf memcached-2.2.0.tgz 
       cd memcached-2.2.0
       /usr/local/php/bin/phpize 
       ./configure --with-php-config=/usr/local/php/bin/php-config --with-libmemcached-dir=/usr/local/libmemcached --disable-memcached-sasl
       make -j4 && make install
       /usr/local/php/bin/pecl install memcache
       echo "extension = "memcache.so"" >>/usr/local/php/lib/php.ini
       echo "extension = "memcached.so"" >>/usr/local/php/lib/php.ini
       cd 
       rm -rf  libmemcached-1.0.18.tar.gz
       rm -rf  memcached-2.2.0.tgz
       service php-fpm restart
       /usr/local/php/bin/php -m
       echo "#################################"
       echo "##php-memcached install suceess##"
       echo "#################################"
}

function installPHPmysqli(){
       cd /root/php-5.4.45/ext/mysqli/
       /usr/local/php/bin/phpize 
       ./configure --with-php-config=/usr/local/php/bin/php-config
       make -j4 && make install
       echo "extension = "mysqli.so"" >>/usr/local/php/lib/php.ini
       service php-fpm restart
       /usr/local/php/bin/php -m
       echo "#################################"
       echo "####php-mysql install suceess####"
       echo "#################################"
}

function installPHPopenssl(){
       cd /root/php-5.4.45/ext/openssl/
       cp config0.m4 config.m4
       /usr/local/php/bin/phpize 
       ./configure --with-php-config=/usr/local/php/bin/php-config	
       make -j4 && make install
       echo "extension = "openssl.so"" >>/usr/local/php/lib/php.ini
       service php-fpm restart
       /usr/local/php/bin/php -m
       echo "#################################"
       echo "###php-openssl install suceess###"
       echo "#################################"
}
function installPHPxcache(){
       cd 
       wget http://xcache.lighttpd.net/pub/Releases/3.2.0/xcache-3.2.0.tar.gz 
       tar -xvf xcache-3.2.0.tar.gz
       cd xcache-3.2.0
       /usr/local/php/bin/phpize 
       ./configure --with-php-config=/usr/local/php/bin/php-config  --enable-xcache
       make -j4 && make install
       echo "extension = "xcache.so"" >>/usr/local/php/lib/php.ini
       service php-fpm restart
       cd 
       rm -rf xcache-3.2.0.tar.gz
       /usr/local/php/bin/php -m
       echo "#################################"
       echo "### php-xcache install suceess###"
       echo "#################################"
}

function installPHPredis(){
       cd 
       wget https://github.com/nicolasff/phpredis/archive/2.2.4.tar.gz
       tar -zxvf 2.2.4.tar.gz
       cd phpredis-2.2.4 
       /usr/local/php/bin/phpize 
       ./configure --with-php-config=/usr/local/php/bin/php-config  
       make -j4 && make install
       echo "extension = "redis.so"" >>/usr/local/php/lib/php.ini
       service php-fpm restart
       cd 
       rm -rf xcache-3.2.0.tar.gz
       /usr/local/php/bin/php -m
       echo "#################################"
       echo "### php-redis install suceess###"
       echo "#################################"
}



echo "which do you want to?input the number."
echo "1. install PHP service"
echo "2. install PHP-memcached service"
echo "3. install PHP-mysqli user"
echo "4. install PHP-openssl user"
echo "5. install PHP-xcache user"
echo "6. install PHP-redis user"
echo "other nothing,exit";
read num

case "$num" in
[1] ) (installPHP);;
[2] ) (installPHPmemcached);;
[3] ) (installPHPmysqli);;
[4] ) (installPHPopenssl);;
[5] ) (installPHPxcache);;
[6] ) (installPHPredis);;
*) echo "nothing,exit";;
esac
