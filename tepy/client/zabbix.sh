#!/bin/bash
#install zabbix 
	#	yum install -y openssl-devel libmcrypt epel-release make  m4 gcc bzip2 curl-devel  libjpeg-devel  libpng-devel  freetype-devel gmp-devel pcre-devel glib2-devel openssl libxml2 libtermcap-devel ncurses-devel GeoIP GeoIP-devel libpcap
	#	yum install -y libxml2-devel libxml2-devel gcc-c++ wget gdb php-mcrypt psmisc cpp  zlib-devel curl mysql mysql-devel gd gd-devel mhash-devel libmcrypt-devel bzip2-devel autoconf libevent-devel subversionntp lua lua-devel libcurl libcurl-devel libpcap-devel  openssl-libs
rpm -qa|grep zabbix
if [ $? -eq 1 ];then
	cd /usr/src/
	wget http://119.9.108.199:3357/iso/zabbix-3.2.4.tar.gz
	tar xvf zabbix-3.2.4.tar.gz
	cd zabbix-3.2.4
	./configure  --prefix=/usr/local/zabbix --enable-agent 
	make &&make install  
#	cp -av  src/zabbix_agent/zabbix_agentd  dd /usr/local/zabbix/sbin/
	cd ..&&rm -rf zabbix* &&cd /etc/init.d/
	wget  http://119.9.108.199:3357/iso/init/zabbix_agentd 
	chmod +x zabbix_agentd 
	useradd -M -s /sbin/nologin zabbix
	cd /usr/local/zabbix/etc &&mv zabbix_agentd.conf zabbix_agentd.conf.bak
	wget http://119.9.108.199:3357/iso/conf/zabbix_agentd.conf
	mkdir /var/log/zabbix
	chown -R zabbix.zabbix /var/log/zabbix
	service zabbix_agentd start 

else 
	echo "**************失败***************"
fi
o=$(cat /etc/redhat-release  |awk {'print $3'}|awk -F. {'print $1'})
if [ $o -eq 6 ];then
	iptables -I INPUT -p tcp --dport 10050 -j ACCEPT
	service iptables save
elif [$o -eq 7 ]; then
	firewll-cmd --add-port=10050/tcp --permanent 
	firewll-cmd --reload
else 
	echo "***********失败****************"
fi
ps -ef |grep zabbix
