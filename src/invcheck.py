import os
import random
import string
from .design import coloring as C
import asyncio
import itertools
import aiohttp

prox = False
valid = []
chars = []
chars[:0] = string.ascii_letters + string.digits
if os.stat("proxies.txt").st_size > 0:
    prox = True
    global proxies
    proxies = itertools.cycle(open("proxies.txt", "r+").read().splitlines())

async def proxgen(amount):
    async with aiohttp.ClientSession() as session:
        for i in range(amount):
            code = "".join(random.choices(chars, k=8))
            check = await session.get(
                f"https://discord.com/api/v9/invite/{code}",
                proxy=f"https://{next(proxies)}"
            )
            if check.status == 200:
                valid.append(code)
                print(f"{C.GREEN}[=] Valid [{i+1}/{amount}]: {code}")
            elif (
                check.status == 429
            ):
                print(f"{C.BLUE}[-] Ratelimited [{i+1}/{amount}]: " + code)
            else:
                print(f"{C.RED}[x] Invalid Invite [{i+1}/{amount}]: " + code)


async def gen(amount):
    async with aiohttp.ClientSession() as session:
        for i in range(amount):
            code = "".join(random.choices(chars, k=8))
            check = await session.get(
                f"https://discordapp.com/api/v9/invite/{code}"
            )
            if check.status == 200:
                valid.append(code)
                print(f"{C.GREEN}[=] Valid [{i+1}/{amount}]: {code}")
            elif check.status == 429:
                print(f"{C.BLUE}[-] Ratelimited [{i+1}/{amount}]: {code}")
            else:
                print(f"{C.RED}[x] Invalid Invite [{i+1}/{amount}]: {code}")


def start():
    print(f"{C.RED}-" * 69)  # Haha funni number. (no.)
    print(
        C.RED
        + """
██╗███╗░░██╗██╗░░░██╗██╗████████╗███████╗  ░██████╗░███████╗███╗░░██╗ by github.com/Mewzax
██║████╗░██║██║░░░██║██║╚══██╔══╝██╔════╝  ██╔════╝░██╔════╝████╗░██║
██║██╔██╗██║╚██╗░██╔╝██║░░░██║░░░█████╗░░  ██║░░██╗░█████╗░░██╔██╗██║
██║██║╚████║░╚████╔╝░██║░░░██║░░░██╔══╝░░  ██║░░╚██╗██╔══╝░░██║╚████║
██║██║░╚███║░░╚██╔╝░░██║░░░██║░░░███████╗  ╚██████╔╝███████╗██║░╚███║
╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░░╚═╝░░░╚══════╝  ░╚═════╝░╚══════╝╚═╝░░╚══╝
		  """
    )
    print(C.CYAN + "A powerful tool to generate, check and store Discord Invites ✉️\n")
    while True:
        try:
            amount = int(input(C.GREEN + "How many invites do you want to generate? "))
            print("\n")
            break
        except Exception as e:
            print(f"~ {C.YELLOW}Input Failure | {e}")
            pass
    if prox:
        asyncio.run(proxgen(amount))
    else:
        asyncio.run(gen(amount))
        with open("valid.txt", "w") as v:
            for invite in valid:
                v.write("discord.gg/" + invite + "\n")