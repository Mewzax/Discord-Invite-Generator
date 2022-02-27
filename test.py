import time
import httpx
import random
import string

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

chars = []
chars[:0] = string.ascii_letters + string.digits

while True:
    code = "mantle"

    try:
        response = httpx.post(
            'https://discord.com/invite/' + code
        )
    except httpx.HTTPError:
        print('Error: Could not connect to Discord')
        continue

    
    print(str(response.content))
    time.sleep(100000)
    if 'inputDefault-3FGxgL input-2g-os5' in str(response.content):
        print(code + ' is correct')

        with open('validCodes.txt', 'a') as f:
            f.write('\n' + code)
    
    else:
        print(code + ' is incorrect')

        with open('invalidCodes.txt', 'a') as f:
            f.write('\n' + code)