#########################################################
# Main Script File #
#########################################################
import os
import random
import string
from .design import coloring as C
import asyncio
import itertools
import aiohttp
headers={"x-fingerprint": "fuckdiscord", "user-agent": "Mozilla/5.0 (Linux; Android 12; 21081111RG Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 UCURSOS/v1.6_269-android"}
prox = False
valid = []
chars = []
chars[:0] = string.ascii_letters + string.digits
if os.stat("Src/proxies.txt").st_size > 0:
	prox = True
	global proxies
	proxies = itertools.cycle(open("Src/proxies.txt", "r+").read().splitlines())
#########################################################
async def proxgen(amount):
	async with aiohttp.ClientSession() as session:
		for i in range(amount):
			code = "".join(random.choices(chars, k=8))
			check = await session.get(f"https://discord.com/api/v9/invite/{code}", proxy=f"https://{next(proxies)}", headers=headers)
			if check.status == 200:
				valid.append(code) 
				print(f"{C.GREEN}	Valid {i}: {code}")	
			elif check.status == 429: # This is my neighbor, ratelimit, he is a pain in my ass.
				print(f"{C.BLUE}	Ratelimited {i+1}" + code)		
			else:
				print(f"{C.RED}	Invalid Invite {i+1} " + code)	

async def gen(amount):
	async with aiohttp.ClientSession() as session:
		for i in range(amount):
			code = "".join(random.choices(chars, k=8))
			check = await session.get(f"https://discordapp.com/api/v9/invite/{code}", headers=headers)
			if check.status == 200:
				valid.append(code)
				print(f"{C.GREEN}	Valid {i}: {code}")	
			elif check.status == 429:
				print(f"{C.BLUE}	Ratelimited {i}: {code}")	
			else:
				print(f"{C.RED}	Invalid Invite {i+1}: {code}")	
				
def start():
	print("	"+ f"{C.RED}-"*69) # Haha funni number.
	print(C.RED + """
	██╗███╗░░██╗██╗░░░██╗██╗████████╗███████╗  ░██████╗░███████╗███╗░░██╗ by github.com/Mewzax
	██║████╗░██║██║░░░██║██║╚══██╔══╝██╔════╝  ██╔════╝░██╔════╝████╗░██║ and github.com/Rooverpy
	██║██╔██╗██║╚██╗░██╔╝██║░░░██║░░░█████╗░░  ██║░░██╗░█████╗░░██╔██╗██║
	██║██║╚████║░╚████╔╝░██║░░░██║░░░██╔══╝░░  ██║░░╚██╗██╔══╝░░██║╚████║
	██║██║░╚███║░░╚██╔╝░░██║░░░██║░░░███████╗  ╚██████╔╝███████╗██║░╚███║
	╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░░╚═╝░░░╚══════╝  ░╚═════╝░╚══════╝╚═╝░░╚══╝
		  """)
	print(C.CYAN + '	A powerful tool to generate, check and store Discord Invites ✉️\n')
	while True:
		try:
			amount = int(input(C.GREEN + "	How many invites do you want to generate? "))
			print("\n")
			break
		except Exception as e:
			print(f"	~ {C.YELLOW}Input Failure | {e}")	
			pass
	if prox:
		asyncio.run(proxgen(amount))
	else:
		asyncio.run(gen(amount))
		with open("Src/valid.txt", "w") as v:
			for invite in valid:
				v.write("discord.gg/" + invite + "\n")
#########################################################
