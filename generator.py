import random
import time
import httpx
import string
import itertools
import json

__CONFIG__ = json.load(open('./config.json'))
__PROXIES__ = itertools.cycle(open(__CONFIG__['path_proxies'], 'r+').read().splitlines())

print(
    '''
    
██╗███╗░░██╗██╗░░░██╗██╗████████╗███████╗  ░██████╗░███████╗███╗░░██╗
██║████╗░██║██║░░░██║██║╚══██╔══╝██╔════╝  ██╔════╝░██╔════╝████╗░██║
██║██╔██╗██║╚██╗░██╔╝██║░░░██║░░░█████╗░░  ██║░░██╗░█████╗░░██╔██╗██║
██║██║╚████║░╚████╔╝░██║░░░██║░░░██╔══╝░░  ██║░░╚██╗██╔══╝░░██║╚████║
██║██║░╚███║░░╚██╔╝░░██║░░░██║░░░███████╗  ╚██████╔╝███████╗██║░╚███║
╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░░╚═╝░░░╚══════╝  ░╚═════╝░╚══════╝╚═╝░░╚══╝'''
)
print('Made by Mewzax')

saveValidCodes = input('Do you want to save valid codes? (y/n) ')
saveInvalidCodes = input('Do you want to save invalid codes? (y/n) ')

def saveCodes(code, file):
    with open(file, 'a') as f:
        f.write('\n' + code)

def getCode():
    code = 'mantle'
    return code

def getResponse(code):
    try:
        with httpx.Client(proxies=f'http://{next(__PROXIES__)}') as client:
            response = client.post(
                'https://discordapp.com/api/v6/invite/' + code
            )
    except httpx.HTTPError:
        print('Error: Could not connect to Discord')

    return response

def checkCode(code):
    try:
        response = getResponse(code)
    except httpx.HTTPError:
        print('Error: Could not connect to Discord')
    
    if response.status_code == 200:
        print('Valid code')

        if saveValidCodes == 'y':
            saveCodes(code, __CONFIG__['path_valid'])
    
    elif response.status_code == 400:
        print('Invalid code')

        if saveInvalidCodes == 'y':
            saveCodes(code, __CONFIG__['path_invalid'])


def main():
    while True:
        code = getCode()
        checkCode(code)