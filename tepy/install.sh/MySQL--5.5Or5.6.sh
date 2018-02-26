#!/bin/sh
echo "create mysql user..."
useradd -M -s /sbin/nologin mysql
echo "install environment..."
yum -y install ntp vim-enhanced gcc gcc-c++ flex bison autoconf automake bzip2-devel ncurses-devel zlib-devel libjpeg-devel libpng-devel libtiff-devel freetype-devel libXpm-devel gettext-devel  pam-devel libtool libtool-ltdl openssl openssl-devel fontconfig-devel libxml2-devel curl-devel  libicu libicu-devel libmcrypt libmcrypt-devel libmhash libmhash-devel
echo "install cmake..."
wget http://www.cmake.org/files/v2.8/cmake-2.8.7.tar.gz
tar -xvf cmake-2.8.7.tar.gz
cd cmake-2.8.7
sh configure
make&&make install
cd ..
echo "install mysql5.5 or mysql5.6..."
if [ ! -d /usr/local/mysql ];then
mkdir -pv /usr/local/mysql
fi
if [ ! -f mysql-5.5.41.tar.gz ] || [ ! -f mysql-5.6.22.tar.gz];then
echo "install mysql5.5 input 1,install mysql5.6 input 2:"
read num
case $num in
1)
wget https://downloads.mariadb.com/archives/mysql-5.5/mysql-5.5.41.tar.gz
tar -xvf mysql-5.5.41.tar.gz
cd mysql-5.5.41
cmake -DCMAKE_INSTALL_PREFIX=/usr/local/mysql -DMYSQL_DATADIR=/usr/local/mysql/data -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_unicode_ci -DWITH_READLINE=1 -DWITH_SSL=system -DWITH_EMBEDDED_SERVER=1 -DENABLED_LOCAL_INFILE=1 -DDEFAULT_COLLATION=utf8_general_ci -DWITH_MYISAM_STORAGE_ENGINE=1 -DWITH_INNOBASE_STORAGE_ENGINE=1 -DWITH_DEBUG=0
make&&make install 
echo "mysql make install complete..."
echo "modify mysql  configuration file..."
cp -vrf  support-files/my-medium.cnf /etc/my.cnf
cp -vrf  support-files/my-medium.cnf /etc/my.cnf
chmod +x /usr/local/mysql
chown -R mysql:mysql /usr/local/mysql
chown -R mysql:mysql /usr/local/mysql/data
echo "StartUp Actions Manager..."
cp -vrf support-files/mysql.server /etc/init.d/mysqld
chmod +x /etc/init.d/mysqld
chkconfig --add mysqld
chkconfig mysqld on
echo "initialize mysql..."
chmod a+x /usr/local/mysql/scripts/mysql_install_db
/usr/local/mysql/scripts/mysql_install_db --user=mysql --basedir=/usr/local/mysql --datadir=/usr/local/mysql/data
service mysqld start
/usr/local/mysql/bin/mysqladmin -uroot password '123456'
ln -s /usr/local/mysql/bin/mysql /usr/local/sbin/mysql
echo "mysql5.5 install all..."
echo "the root passwd 123456"
;;
2)
wget https://downloads.mariadb.com/archives/mysql-5.6/mysql-5.6.22.tar.gz
tar -xvf  mysql-5.6.22.tar.gz
cd mysql-5.6.22
cmake -DCMAKE_INSTALL_PREFIX=/usr/local/mysql -DMYSQL_DATADIR=/usr/local/mysql/data -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_unicode_ci -DWITH_READLINE=1 -DWITH_SSL=system -DWITH_EMBEDDED_SERVER=1 -DENABLED_LOCAL_INFILE=1 -DDEFAULT_COLLATION=utf8_general_ci -DWITH_MYISAM_STORAGE_ENGINE=1 -DWITH_INNOBASE_STORAGE_ENGINE=1 -DWITH_DEBUG=0
make&&make install 
echo "mysql make install complete..."
echo "modify mysql  configuration file..."
cp -vrf  support-files/my-default.cnf /etc/my.cnf
chmod +x /usr/local/mysql
chown -R mysql:mysql /usr/local/mysql
chown -R mysql:mysql /usr/local/mysql/data
echo "StartUp Actions Manager..."
cp -vrf support-files/mysql.server /etc/init.d/mysqld
chmod +x /etc/init.d/mysqld
chkconfig --add mysqld
chkconfig mysqld on
echo "initialize mysql..."
chmod a+x /usr/local/mysql/scripts/mysql_install_db
/usr/local/mysql/scripts/mysql_install_db --user=mysql --basedir=/usr/local/mysql --datadir=/usr/local/mysql/data
service mysqld start
/usr/local/mysql/bin/mysqladmin -uroot password '123456'
ln -s /usr/local/mysql/bin/mysql /usr/local/sbin/mysql
echo "mysql5.6 install all..."
echo "the root passwd 123456"
;;
*)
echo "please input 1 or 2"
exit 0
esac
else
echo "mysql-5.5.41.tar.gz is exits"
fi
