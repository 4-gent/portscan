import socket as sk
import sys

import os
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from art import text2art

def single_scan(address, port):
	s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
	s.settimeout(1000)
	if(s.connect_ex((address, port)) == 0):
		print("%d:OPEN at address %s" % (port, address))
	else: print("%d:CLOSED at address %s" % (port, address))
	s.close()

def multi_scan(address, port1, port2):
	count = 0;
	port1 = port1 - 1
	port2 = port2 + 1
	for port in range(port1, port2):
		try:
			s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
			s.settimeout(1000)
			if(s.connect_ex((address, port)) == 0):
				count += 1
				print("%d:OPEN" % (port))
			if(s.connect_ex((address, port)) != 0):
				print("%d:CLOSED" % (port))
			s.close()
		except KeyboardInterrupt:
			print('Scanning Closed')
			sys.exit()
		except: continue
	print("Total open ports: %d at address %s" % (count, address))

def ssh_manager(address, username):
	ssh_string = f"sudo ssh {username}@{address}"
	os.system(ssh_string)

def main():
	cprint(text2art('------------'), 'green', attrs=['bold'])
	cprint(text2art('Port Scanner'), 'green', attrs=['bold'])
	cprint(text2art('------------'), 'green', attrs=['bold'])
	print("Give address to scan: ")
	print("a: localhost")
	print("b: server1  ")
	print("or type in ip...")
	address = input()
	if(address == 'a'):
		address = '127.0.0.1'
	if(address == 'b'):
		address = '174.50.178.181'
	print("a: Single Scan")
	print("b: Multi Scan ")
	print("c: SSH Connection")
	choice = input()
	if(choice == 'a'):
		print("Port to scan: ")
		port = int(input())
		single_scan(address, port)
	if(choice == 'b'):
		print("Give port(s) to scan: ")
		port1 = int(input())
		port2 = int(input())
		multi_scan(address, port1, port2)
	if(choice == 'c'):
		print("Give hostname to conect to")
		username = input()
		ssh_manager(address, username)

main()
