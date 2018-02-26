#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org
import  sys
import  paramiko
hostname = '192.168.192.100'
port = 22
username = 'root'
#pkey = '/root/.ssh/id_rsa'
pkey = '/Users/kevim/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(pkey)
s = paramiko.SSHClient()
s.load_system_host_keys()
s.connect(hostname,port,username,pkey=key)

stdin,stdout,stderr=s.exec_command("system status network")
name = stdout.read()
print(name)
