#!/bin/sh
echo " install ==========nginx=============="
echo"cc-c++ autoconf automake libtool make pcre pcre-devel" >/root/install
INATLL=$(cat /root/install)
for i in $INATLL
do
if[(rpm -q $i ) -eq 1]; then
	yum install $i 

