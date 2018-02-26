#!/bin/sh
#install nginx 编译安装
#安装编译线程和c语言
read -p "本地源是否搭建（y/n）" BEN
if [$BEN -eq  y];then
  echo "将要进行安装c语言"
  yum install -y  openssl openssl-devel libmcrypt zlib-devel  epel-release make libmcrypt-devel.x86_64 m4 autoconf bzip2 bzip2-devel gcc bzip2 libxml2-devel  curl-devel  libjpeg-devel  libpng-devel  freetype-devel  gmp-devel  pcre-devel  glib2-devel  opensssl  libxml2 yum install libxml2-devel  gcc-c++  wget gdb php-mcrypt cloud-init libmcrypt  libmcrypt-devel  psmisc gcc.x86_64 cpp.x86_64 pcre-devel.x86_64 zlib-devel.x86_64  curl.x86_64 curl-devel.x86_64 libmcrypt-devel.x86_64  mysql.x86_64 mysql-devel.x86_64 libxml2-devel.x86_64  gd.x86_64 gd-devel.x86_64 mhash-devel.x86_64  libmcrypt-devel.x86_64 bzip2-devel.x86_64  autoconf.noarch  libevent-devel.x86_64 subversion.x86_64 ntp gcc-c++ libtermcap-devel.x86_64 ncurses-devel.x86_64  GeoIP.x86_64 GeoIP-devel.x86_64  lua.x86_64 lua-devel.x86_64 libcurl.x86_64 libcurl-devel.x86_64  libpcap-devel.x86_64 libpcap.x86_64 openssl-libs.x86_64 openssl-devel.x86_64
elif [ $BEN -eq  n ];then
	echo "没有检测到本地源，请使用系统镜像部署本地yum源"
	mkdir /etc/yum.repos.d/backup
	mv /etc/yum.repos.d/CentOS* /etc/yum.repos.d/backup 
	echo "[cdrom]
	      name = cdrom
		  baseurl = file:///mnt
		  gpgcheck = 0" >>/etc/yum.repos.d/cdrom.repo
	echo "请你直接挂在系统系统光盘"
else 
	exit  1
fi
tar xvf nginx-1.10.0.tar.gz
cd nginx-1.10.0
./configure --prefix=/usr/local/nginx --without-http_memcached_module --user=daemon --group=daemon  --http-fastcgi-temp-path=/tmp/nginx/fastcgi_temp  --http-client-body-temp-path=/tmp/nginx/client_body_temp  --without-http_autoindex_module --without-http_scgi_module   --without-http_uwsgi_module  --with-http_gzip_static_module --with-http_stub_status_module --with-pcre=/root/pcre-8.38 --http-proxy-temp-path=/tmp/nginx/nginx_proxy_temp    --with-openssl=/usr/
echo "编译"
make 
echo ""编译安装
make install

echo "
#!/bin/bash
# nginx Startup script for the Nginx HTTP Server
# it is v.0.0.2 version.
# chkconfig: - 85 15
# description: Nginx is a high-performance web and proxy server.
# It has a lot of features, but it's not for everyone.
# processname: nginx
# pidfile: /var/run/nginx.pid
# config: /usr/local/nginx/conf/nginx.conf
nginxd=/usr/local/nginx/sbin/nginx
nginx_config=/usr/local/nginx/conf/nginx.conf
nginx_pid=/usr/local/nginx/logs/nginx.pid
RETVAL=0
prog="nginx"
# Source function library.
. /etc/rc.d/init.d/functions
# Source networking configuration.
. /etc/sysconfig/network
# Check that networking is up.
[ ${NETWORKING} = "no" ] && exit 0
[ -x $nginxd ] || exit 0
# Start nginx daemons functions.
start() {
if [ -e $nginx_pid ];then
echo "nginx already running...."
exit 1
fi
echo -n $"Starting $prog: "
daemon $nginxd -c ${nginx_config}
RETVAL=$?
echo
[ $RETVAL = 0 ] && touch /var/lock/subsys/nginx
return $RETVAL
}
# Stop nginx daemons functions.
stop() {
echo -n $"Stopping $prog: "
killproc $nginxd
RETVAL=$?
echo
[ $RETVAL = 0 ] && rm -f /var/lock/subsys/nginx /usr/local/nginx/logs/nginx.pid
}
reload() {
echo -n $"Reloading $prog: "
#kill -HUP `cat ${nginx_pid}`
killproc $nginxd -HUP
RETVAL=$?
echo
}
# See how we were called.
case "$1" in
start)
start
;;
stop)
stop
;;
reload)
reload
;;
restart)
stop
start
;;
status)
status $prog
RETVAL=$?
;;
*)
echo $"Usage: $prog {start|stop|restart|reload|status|help}"
exit 1
esac
exit $RETVAL"
>/etc/init.d/nginx
chmod +x /etc/init.d/nginx
