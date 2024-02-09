import random
import threading
import asyncio
import telethon
from telethon import events
from queue import Queue
import requests
from telethon.sync import functions
from user_agent import generate_user_agent
import requests
from user_agent import *
from help import *
from config import *
from threading import Thread

a = 'qwertyuiopassdfghjklzxcvbnm'
b = '1234567890'
e = 'qwertyuiopassdfghjklzxcvbnm1234567890'

banned = []
isclaim = ["off"]
isauto = ["off"]
with open("banned.txt", "r") as f:
    f = f.read().split()
    banned.append(f)

que = Queue()


def check_user(username):
    url = "https://t.me/"+str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}

    response = requests.get(url, headers=headers)
    if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
        return "Available"
    else:
        return "Unavailable"

def gen_user(choice):
    if choice == "1":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], "_", d[0], "_", s[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "2":
        c = random.choices(a)
        d = random.choices(a)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], "_", d[0], "_", s[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "3":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], "_", d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], "_", d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "4":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], "_", d[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], "_", d[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "5":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], "_", c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], "_", c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "6":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], "_", d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], "_", d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "7":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], "_", c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], "_", c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "8":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], "_", d[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], "_", d[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "9":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], "_", c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], "_", c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "10":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], "_", c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], "_", c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "11":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], "_", d[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], "_", d[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "12":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], "_", c[0], d[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], "_", c[0], d[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "13":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], "_", c[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], "_", c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "14":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], "_", d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], "_", d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "15":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], "_", d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], d[0], "_", d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "16":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], d[0], "_", c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], d[0], "_", c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "17":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], "_", c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], "_", c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "18":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], c[0], c[0], "_", c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], c[0], c[0], "_", c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "19":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], "_", d[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], "_", d[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "20":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], "_", d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], "_", d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "21":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], "_", c[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], "_", c[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "22":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], d[0], "_", d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], d[0], "_", d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "23":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], "_", d[0], d[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], "_", d[0], d[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "24":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], "_", c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], d[0], "_", c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "25":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], "_", d[0], "_", d[0], "_", d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], "_", d[0], "_", d[0], "_", d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "26":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], "_", d[0], "_", c[0], "_", c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], "_", d[0], "_", c[0], "_", c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "27":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], "_", c[0], "_", d[0], "_", c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], "_", c[0], "_", d[0], "_", c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "28":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], "_", c[0], "_", c[0], "_", d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], "_", c[0], "_", c[0], "_", d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "29":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], c[0], d[0], d[0], d[0], d[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], c[0], d[0], d[0], d[0], d[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "30":
        c = random.choices(a)
        d = random.choices(a)
        s = random.choices(e)
        f = [c[0], d[0], d[0], c[0], c[0], c[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], d[0], d[0], c[0], c[0], c[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "31":
        c = d =random.choices(a)
        d = random.choices(a)
        s = random.choices(b)
        f =  [c[0], c[0], d[0], d[0], c[0], c[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = d =random.choices(a)
            d = random.choices(a)
            s = random.choices(b)
            f =  [c[0], c[0], d[0], d[0], c[0], c[0]]
            username = ''.join(f)
        else:
            pass      
    if choice == "32":
        c = d =random.choices(a)
        d = random.choices(e)
        s = random.choices(b)
        f =  [c[0], c[0], c[0], d[0], d[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(e)
            s = random.choices(b)
            f =  [c[0], c[0], c[0], d[0], d[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "33":
        c = d = random.choices(a)
        d = random.choices(e)
        f =  [c[0], c[0], c[0], c[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f =  [c[0], c[0], c[0], c[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "34":
        c = d =random.choices(a)
        d = random.choices(e)
        s = random.choices(b)
        f =  [c[0], c[0], c[0], d[0], d[0], d[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = d =random.choices(a)
            d = random.choices(e)
            s = random.choices(b)
            f =  [c[0], c[0], c[0], d[0], d[0], d[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "35":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f =  [c[0], d[0], c[0], d[0], d[0], d[0]]                
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "36":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f =  [c[0], d[0], c[0], d[0], c[0], c[0]]                
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass  
    if choice == "37":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], c[0], d[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f =  [c[0], c[0], d[0], c[0], d[0], c[0]]                
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass           
    if choice == "38":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], d[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], d[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "39":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], d[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f =  [c[0], d[0], c[0], c[0], d[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "40":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], d[0], d[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], d[0], d[0], d[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "41":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], c[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], d[0], c[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "42":
        c = d = random.choices(a)
        d = random.choices(e)
        f =  [c[0], c[0], d[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f =  [c[0], c[0], d[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass            
    if choice == "43":
        c = d = random.choices(a)
        d = random.choices(e)
        f =  [c[0], d[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f =  [c[0], d[0], c[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass            
    if choice == "44":
        c = d = random.choices(a)
        d = random.choices(e)
        f =  [c[0], d[0], d[0], d[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f =  [c[0], d[0], d[0], d[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass            
    if choice == "45":
        c = d = random.choices(a)
        d = random.choices(e)
        f =  [c[0], d[0], c[0], d[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f =  [c[0], d[0], c[0], d[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "46":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], d[0], d[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "47":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], d[0], d[0], d[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], d[0], d[0], d[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "48":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], d[0], d[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], d[0], d[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "49":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], c[0], d[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], d[0], c[0], d[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "50":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], c[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "51":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], d[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "52":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], d[0], c[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], d[0], c[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "53":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], d[0], d[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], d[0], d[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass                   
    if choice == "54":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], d[0], d[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "55":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "56":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], d[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], d[0], c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "57":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], d[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "58":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], c[0], d[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass        
    if choice == "59":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass            
    if choice == "60":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], d[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], d[0], d[0], d[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "61":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], c[0], c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "62":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], d[0], c[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], d[0], c[0], c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "63":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], d[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], d[0], c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "64":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "65":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], c[0], d[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], c[0], c[0], d[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass        
    if choice == "66":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], c[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass 
    if choice == "67":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], d[0], d[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], d[0], d[0], d[0], d[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "68":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], c[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], c[0], c[0], c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "69":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], d[0], c[0], c[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], d[0], c[0], c[0], c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "70":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], d[0], c[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], d[0], c[0], c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "71":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "72":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "73":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], c[0], c[0], d[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], c[0], c[0], c[0], d[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass        
    if choice == "74":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], c[0], c[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "75":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], s[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = username+'bot'
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], s[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bot'
        else:
            pass     
    if choice == "76":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], "_", d[0], "_", d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], "_", d[0], "_", d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "77":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], "_", d[0], d[0], "_", d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], "_", d[0], d[0], "_", d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "78":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], d[0], "_", d[0], "_", d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], d[0], "_", d[0], "_", d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass          
    if choice == "79":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], "_", d[0], "_", d[0], "_", d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], "_", d[0], "_", d[0], "_", d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass          
    if choice == "80":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], "_", d[0], d[0], "_", d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], "_", d[0], d[0], "_", d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "81":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], d[0], "_", d[0], d[0], "_", d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], d[0], "_", d[0], d[0], "_", d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "82":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], d[0], "_", d[0], "_", d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], d[0], "_", d[0], "_", d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "83":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], "_", d[0], d[0], d[0], "_", d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], "_", d[0], d[0], d[0], "_", d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "84":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], "_", d[0], "_", d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], "_", d[0], "_", d[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "85":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], d[0], d[0], "_", d[0], "_", d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], d[0], d[0], "_", d[0], "_", d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "86":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], "_", d[0], d[0], "_", d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], "_", d[0], d[0], "_", d[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "87":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], d[0], d[0], "_", d[0], d[0], "_", d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], d[0], d[0], "_", d[0], d[0], "_", d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "88":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], d[0], "_", d[0], "_", d[0], d[0], d[0]] 
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], d[0], "_", d[0], "_", d[0], d[0], d[0]] 
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "89":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], d[0], d[0], "_", d[0], "_", d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], d[0], d[0], "_", d[0], "_", d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "90":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], "_", d[0], d[0], d[0], "_", d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], "_", d[0], d[0], d[0], "_", d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "91":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], d[0], "_", d[0], d[0], d[0], "_", d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], d[0], "_", d[0], d[0], d[0], "_", d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "92":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], d[0], "_", d[0], d[0], "_", d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], d[0], "_", d[0], d[0], "_", d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "93":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], "_", d[0], d[0], d[0], d[0], "_", d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], "_", d[0], d[0], d[0], d[0], "_", d[0]]
            random.shuffle(f)
            username = ''.join(f)

    if choice == "94":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], "_", d[0], d[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], "_", d[0], d[0], d[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "95":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], d[0], "_", d[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], d[0], "_", d[0], d[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "96":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], d[0], d[0], "_", d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], d[0], d[0], "_", d[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "97":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], d[0], d[0], d[0], "_", d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], d[0], d[0], d[0], "_", d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass        
    if choice == "98":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], d[0], d[0], d[0], d[0], "_", d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], d[0], d[0], d[0], d[0], "_", d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass           
    if choice == "99":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], "_", d[0], d[0], d[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], "_", d[0], d[0], d[0], d[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "100":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], d[0], "_", d[0], d[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], d[0], "_", d[0], d[0], d[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "101":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], d[0], d[0], "_", d[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], d[0], d[0], "_", d[0], d[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "102":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], d[0], d[0], d[0], "_", d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], d[0], d[0], d[0], "_", d[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "103":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], d[0], d[0], d[0], d[0], "_", d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], d[0], d[0], d[0], d[0], "_", d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "104":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], d[0], d[0], d[0], d[0], d[0], "_", d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], d[0], d[0], d[0], d[0], d[0], "_", d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass                    
    if choice == "105":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], "_", d[0], d[0], d[0], d[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], "_", d[0], d[0], d[0], d[0], d[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "106":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], d[0], "_", d[0], d[0], d[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], d[0], "_", d[0], d[0], d[0], d[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "107":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], d[0], d[0], "_", d[0], d[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], d[0], d[0], "_", d[0], d[0], d[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "108":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], d[0], d[0], d[0], "_", d[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], d[0], d[0], d[0], "_", d[0], d[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "109":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], d[0], d[0], d[0], d[0], "_", d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], d[0], d[0], d[0], d[0], "_", d[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "110":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], d[0], d[0], d[0], d[0], d[0], "_", d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], d[0], d[0], d[0], d[0], d[0], "_", d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "111":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], d[0], d[0], d[0], d[0], d[0], d[0], "_", d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], d[0], d[0], d[0], d[0], d[0], d[0], "_", d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass                   
    return username

@sython.on(events.NewMessage(outgoing=True, pattern=r"\.تشيكر"))
async def _(event):
    if ispay2[0] == "yes":
        await event.edit(tele_checker)
        
@sython.on(events.NewMessage(outgoing=True, pattern=r"\.اليوزرات المبندة"))
async def _(event):
    if ispay2[0] == "yes":
        await sython.send_file(event.chat_id, 'banned.txt')


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.الانواع"))
async def _(event):
    if ispay2[0] == "yes":
        await event.edit(tele_checker2)
# صيد عدد نوع قناة


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.صيد (.*)"))
async def _(event):
    if ispay2[0] == "yes":
        isclaim.clear()
        isclaim.append("on")
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 2)
        ch = str(msg[2])
        choice = str(msg[1])
        trys = 0
        await event.edit(f"حسناً سأفحص نوع `{choice}` من اليوزرات على `{ch}` , بعدد `{msg[0]}` من المحاولات !")

        @sython.on(events.NewMessage(outgoing=True, pattern=r"\.حالة الصيد"))
        async def _(event):
            if ispay2[0] == "yes":
                if "on" in isclaim:
                    await event.edit(f"الصيد وصل لـ({trys}) من المحاولات")
                elif "off" in isclaim:
                    await event.edit("لايوجد صيد شغال !")
                else:
                    await event.edit("خطأ")
            else:
                pass
        for i in range(int(msg[0])):
            if ispay2[0] == 'no':
                break
            username = ""

            username = gen_user(choice)
            t = Thread(target=lambda q, arg1: q.put(
                check_user(arg1)), args=(que, username))
            t.start()
            t.join()
            isav = que.get()
            if "Available" in isav:
                await asyncio.sleep(1)
                try:
                    await sython(functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username))
                    await event.client.send_message(event.chat_id, f'''
- Hi New Telegram User
·–––––––––––––––·
- User : @{username} 
·–––––––––––––––·
- by : @o_o_v - @ppqbot
    ''')
                    break
                except telethon.errors.rpcerrorlist.UsernameInvalidError:
                    with open("banned.txt", "a") as f:
                        f.write(f"\n{username}")
                except Exception as eee:
                    await sython.send_message(event.chat_id, f'''خطأ مع {username}
    الخطأ :
    {str(eee)}''')
                    if "A wait of" in str(eee):
                        break
                    else:
                        await sython.send_message(event.chat.id, " اجاك متاح !")
            else:
                pass
            trys += 1

        isclaim.clear()
        isclaim.append("off")
        trys = ""
        await event.client.send_message(event.chat_id, "! انتهى الصيد")
        
@sython.on(events.NewMessage(outgoing=True, pattern=r"\.تثبيت (.*)"))
async def _(event):
    if ispay2[0] == "yes":
        trys = 0
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        if msg[0] == "تلقائي":  # تثبيت تلقائي عدد يوزر قناة
            isauto.clear()
            isauto.append("on")
            msg = ("".join(event.text.split(maxsplit=2)[2:])).split(" ", 2)
            username = str(msg[2])
            ch = str(msg[1])
            await event.edit(f"حسناً سأحاول تثبيت `{username}` على `{ch}` , بعدد `{msg[0]}` من المحاولات !")

            @sython.on(events.NewMessage(outgoing=True, pattern=r"\.حالة التثبيت التلقائي"))
            async def _(event):
                if "on" in isauto:
                    msg = await event.edit(f"التثبيت وصل لـ({trys}) من المحاولات")
                elif "off" in isauto:
                    await event.edit("لايوجد تثبيت شغال !")
                else:
                    await event.edit("خطأ")
            for i in range(int(msg[0])):
                if ispay2[0] == 'no':
                    break
                t = Thread(target=lambda q, arg1: q.put(
                    check_user(arg1)), args=(que, username))
                t.start()
                t.join()
                isav = que.get()
                if "Available" in isav:
                    try:
                        await sython(functions.channels.UpdateUsernameRequest(
                            channel=ch, username=username))
                        await event.client.send_message(event.chat_id, f'''
- Hi New Telegram User
·–––––––––––––––·
- User : @{username} 
·–––––––––––––––·
- by : @o_o_v - @ppqbot

    ''')
                        break
                    except telethon.errors.rpcerrorlist.UsernameInvalidError:
                        await event.client.send_message(event.chat_id, f"مبند `{username}` ❌❌")
                        break
                    except Exception as eee:

                        await sython.send_message(event.chat_id, f'''خطأ مع {username}
    الخطأ :
    {str(eee)}''')
                        if "A wait of" in str(eee):
                            break
                else:
                    pass
                trys += 1

                await asyncio.sleep(8)
            trys = ""
            isclaim.clear()
            isclaim.append("off")
            await sython.send_message(event.chat_id, "تم الانتهاء من التثبيت التلقائي")
        if msg[0] == "يدوي":  # تثبيت يدوي يوزر قناة
            await event.edit(f"حسناً سأحاول تثبيت `{username}` على `{ch}` !")
            msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
            username = str(msg[0])
            ch = str(msg[1])
            try:
                await sython(functions.channels.UpdateUsernameRequest(
                    channel=ch, username=username))
                await event.client.send_message(event.chat_id, f'''
- Hi New Telegram User
·–––––––––––––––·
- User : @{username} 
·–––––––––––––––·
- by : @o_o_v - @ppqbot
    ''')
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(event.chat_id, f"مبند `{username}` ❌❌")
            except Exception as eee:
                await sython.send_message(event.chat_id, f'''خطأ مع {username}
    الخطأ :
    {str(eee)}''')
Threads=[] 
for t in range(100):
    x = threading.Thread(target=_)
    le = threading.Thread(target=gen_user)
    x.start()
    le.start()
    Threads.append(x)
    Threads.append(le)
for Th in Threads:
    Th.join()
    
