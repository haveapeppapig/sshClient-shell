#!/usr/bin/python3

import sys
import paramiko
import time


#print(sys.argv)
if len(sys.argv) != 4:
    print("sudo apt install python3-pip")
    print("pip3 install paramiko")
    print("Usage: %s host port user" %sys.argv[0])
    print("       %s 1.1.1.1 22 admin" %sys.argv[0])
    exit()
host = sys.argv[1]
port = sys.argv[2]
user = sys.argv[3]
passwd = input("password: ")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect(host, port, user, passwd, timeout=10)
    print("%s@%s>" %(user, host), end=' ')
    sys.stdout.flush()
except paramiko.AuthenticationException:
    print("[!] Authentication failed")
except Exception:
    print("[!] Connection Failed")
except paramiko.SSHException:
    print("[!] Unable to establish SSH connection: %s"%(sshException))

while True:
    input_cmd = sys.stdin.readline()
    stdin, stdout, stderr = ssh.exec_command(input_cmd)
 
    channel = stdout.channel
    ret = channel.recv_exit_status()
    if ret == 0:
        print(stdout.read().decode())
    else:
        print(stderr.read().decode())
    print("%s@%s>" %(user, host), end=' ')
    sys.stdout.flush()
 
ssh.close()
