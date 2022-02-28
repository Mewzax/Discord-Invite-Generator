import os, string, json, random, itertools, httpx, ctypes
from colorama import init, Fore

init()

valid = []
invalid = 0

chars = []
chars[:0] = string.ascii_letters + string.digits

__CONFIG__ = json.load(open("./config.json"))
__PROXIES__ = itertools.cycle(
    open(__CONFIG__["path_proxies"], "r+").read().splitlines()
)


def saveCodes(code, file):
    with open(file, "a") as f:
        f.write(code + "\n")
        f.close()


def generateCode():
    code = "".join(random.choices(chars, k=19))
    return code


def checkCode(code):
    try:
        if __CONFIG__["use_proxies"] == "True":
            with httpx.Client(
                proxies=f"http://{next(__PROXIES__)}",
                timeout=__CONFIG__["proxy_timeout"],
            ) as client:
                response = client.get("https://discordapp.com/api/v6/invite/" + code)

                if "expires_at" in str(response.content):
                    print(Fore.LIGHTCYAN_EX + "Valid code: " + code + Fore.RESET)
                    valid.append(code)
                    if saveValidCodes == "y":
                        saveCodes(code, __CONFIG__["path_valid"])

                elif "Unknown Invite" in str(response.content):
                    print(Fore.LIGHTRED_EX + "Invalid code: " + code + Fore.RESET)
                    invalid += 1
                    if saveInvalidCodes == "y":
                        saveCodes(code, __CONFIG__["path_invalid"])

                elif "You are being rate limited" in str(response.content):
                    print(Fore.LIGHTRED_EX + "Rate limited!" + Fore.RESET)

                else:
                    print(Fore.LIGHTRED_EX + "Unknown error!" + Fore.RESET)

        else:
            response = httpx.get("https://discordapp.com/api/v6/invite/" + code)

            if "expires_at" in str(response.content):
                print(Fore.LIGHTGREEN_EX + "Valid code: " + code + Fore.RESET)
                valid.append(code)
                if saveValidCodes == "y":
                    saveCodes(code, __CONFIG__["path_valid"])

            elif "Unknown Invite" in str(response.content):
                print(Fore.LIGHTRED_EX + "Invalid code: " + code + Fore.RESET)
                invalid += 1
                if saveInvalidCodes == "y":
                    saveCodes(code, __CONFIG__["path_invalid"])

            elif "You are being rate limited" in str(response.content):
                print(Fore.LIGHTRED_EX + "Rate limited!" + Fore.RESET)

            else:
                print(Fore.LIGHTRED_EX + "Unknown error!" + Fore.RESET)

    except httpx.HTTPError:
        print(Fore.LIGHTRED_EX + "Error: Could not connect to Discord" + Fore.RESET)


def main():
    print(
        Fore.LIGHTRED_EX
        + """
    
██╗███╗░░██╗██╗░░░██╗██╗████████╗███████╗  ░██████╗░███████╗███╗░░██╗ by github.com/Mewzax
██║████╗░██║██║░░░██║██║╚══██╔══╝██╔════╝  ██╔════╝░██╔════╝████╗░██║
██║██╔██╗██║╚██╗░██╔╝██║░░░██║░░░█████╗░░  ██║░░██╗░█████╗░░██╔██╗██║
██║██║╚████║░╚████╔╝░██║░░░██║░░░██╔══╝░░  ██║░░╚██╗██╔══╝░░██║╚████║
██║██║░╚███║░░╚██╔╝░░██║░░░██║░░░███████╗  ╚██████╔╝███████╗██║░╚███║
╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░░╚═╝░░░╚══════╝  ░╚═════╝░╚══════╝╚═╝░░╚══╝"""
        + Fore.RESET
    )
    print(Fore.CYAN + 'A powerful tool to generate, check and store Discord Invites ✉️\n' + Fore.RESET)
    saveValidCodes = input(Fore.LIGHTGREEN_EX + "Do you want to save valid codes? (y/n) ")
    saveInvalidCodes = input("Do you want to save invalid codes? (y/n) ")
    codesAmount = int(input("How many codes do you want to generate? " + Fore.RESET))
    print(Fore.LIGHTCYAN_EX + "\nGenerating codes...\n" + Fore.RESET)
    for i in range(codesAmount):
        code = generateCode()
        checkCode(code)
        if os.name == "nt":
            ctypes.windll.kernel32.SetConsoleTitleW('Invite Generator - Valid: ' + str(len(valid)) + ' - Invalid: ' + str(invalid))
    print(Fore.CYAN + "\nDone!" + Fore.RESET)
    print(Fore.LIGHTGREEN_EX + "Valid codes: " + str(len(valid)) + Fore.RESET)
    for code in valid:
        print(Fore.LIGHTGREEN_EX + code + Fore.RESET)
    print(Fore.LIGHTRED_EX + "Invalid codes: " + str(invalid) + Fore.RESET)


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()