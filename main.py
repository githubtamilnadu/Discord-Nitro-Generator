
# Fix code format and add proxy system
# - Zenqi

import requests
import Prawler
import random
import string
import time

def main():
    try:
        num_proxy = int(input("Enter number of proxy to use (Default: 50) > "))
    expect:
        num_proxy = 50
    try:
        amount    = int(input("Enter the amount of nitro to generate (Default: 1000) > "))
    expect:
        amount = 1000
    value = 1

    if num_proxy == "":
        num_proxy = 50

    elif amount == "":
        amount = 50

    print("generating proxy")
    # generate proxy

    proxy_list = Prawler.get_proxy_list(num_proxy, 'http', 'elite', 'US')


    while value <= amount:

        
        _proxy = random.choice(proxy_list)
        proxies = {
            "http": f"http://{_proxy}"
        }
        
        nitro = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)])
        print(f"trying -> {nitro} with proxy -> {_proxy}\n")
        r = requests.get(f'https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}', proxies=proxies, timeout=3)

        if r.status_code == 200:
            print(f"wow, -> {nitro} is accepted.")
            with open('Codes.txt', 'w+') as f:
                f.write(f"\ndiscord.gift/{nitro}")
                f.close()

        elif r.status_code == 404:
            print(f"invalid code -> {nitro}")

        elif r.status_code == 429:
            print('too many request. proxy -> rate limit?\n')

        value += 1

if __name__ == "__main__":
    main()
