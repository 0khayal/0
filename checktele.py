import random
import requests

import telethon
from telethon.sync import functions
from user_agent import generate_user_agent
from help import *
import requests
from user_agent import *
from help import *
from config import *
from threading import Thread
import threading
import asyncio
from telethon import events

a = 'qwertyuiopassdfghjklzxcvbnm'
b = '1234567890'
e = 'qwertyuiopassdfghjklzxcvbnm1234567890'

banned = []
with open("banned.txt", "r") as f:
    f = f.read().split()
    banned.append(f)
trys, trys2 = [0], [0]
isclaim = ["off"]
isauto = ["off"]


def check_user(username):
    url = "https://t.me/" + str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    response = requests.get(url, headers=headers)
    if (
        response.text.find(
            'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"'
        )
        >= 0
    ):
        return True
    else:
        return False


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

    elif choice == "2":
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

    elif choice == "3":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], "_", d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], "_", d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "4":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], "_", d[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], "_", d[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "5":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], "_", c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], "_", c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "6":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], "_", d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], "_", d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "7":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], "_", c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], "_", c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "8":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], "_", d[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], "_", d[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "9":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], "_", c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], "_", c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "10":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [d[0], "_", c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], "_", c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "11":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], "_", d[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], "_", d[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "12":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], "_", c[0], d[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], "_", c[0], d[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "13":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], "_", c[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], "_", c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "14":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], "_", d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], "_", d[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "15":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], "_", d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], d[0], "_", d[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "16":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], "_", c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], d[0], "_", c[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "17":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], "_", c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], "_", c[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "18":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [d[0], c[0], c[0], "_", c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [d[0], c[0], c[0], "_", c[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "19":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], "_", d[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], "_", d[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "20":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], "_", d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], "_", d[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "21":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], "_", c[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], "_", c[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "22":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], "_", d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], d[0], "_", d[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "23":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], "_", d[0], d[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], "_", d[0], d[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "24":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], "_", c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], d[0], "_", c[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "25":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], "_", d[0], "_", d[0], "_", d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], "_", d[0], "_", d[0], "_", d[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "26":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], "_", d[0], "_", c[0], "_", c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], "_", d[0], "_", c[0], "_", c[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "27":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], "_", c[0], "_", d[0], "_", c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], "_", c[0], "_", d[0], "_", c[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "28":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], "_", c[0], "_", c[0], "_", d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], "_", c[0], "_", c[0], "_", d[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "29":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], d[0], d[0], d[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], d[0], d[0], d[0], d[0]]
            username = ''.join(f)

    elif choice == "30":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], c[0], c[0], c[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], d[0], c[0], c[0], c[0]]
            username = ''.join(f)

    elif choice == "31":
        c = d = random.choices(a)
        d = random.choices(e)
        f =  [c[0], c[0], d[0], d[0], c[0], c[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f =  [c[0], c[0], d[0], d[0], c[0], c[0]]
            username = ''.join(f)
      
    elif choice == "32":
        c = d = random.choices(a)
        d = random.choices(e)
        f =  [c[0], c[0], c[0], d[0], d[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f =  [c[0], c[0], c[0], d[0], d[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "33":
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

    elif choice == "34":
        c = d = random.choices(a)
        d = random.choices(e)
        f =  [c[0], c[0], c[0], d[0], d[0], d[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f =  [c[0], c[0], c[0], d[0], d[0], d[0]]
            username = ''.join(f)

    elif choice == "35":
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

    elif choice == "36":
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
  
    elif choice == "37":
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
           
    elif choice == "38":
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

    elif choice == "39":
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

    elif choice == "40":
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

    elif choice == "41":
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

    elif choice == "42":
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
            
    elif choice == "43":
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
            
    elif choice == "44":
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
            
    elif choice == "45":
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

    elif choice == "46":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], d[0], d[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "47":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], d[0], d[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], d[0], d[0], d[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "48":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], d[0], d[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], d[0], d[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "49":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], c[0], d[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], d[0], c[0], d[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "50":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], c[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "51":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], d[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "52":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], c[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], d[0], c[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "53":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], d[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], d[0], d[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
                   
    elif choice == "54":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], d[0], d[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], d[0], d[0], d[0], d[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "55":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], c[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], c[0], c[0], c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "56":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], c[0], c[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], d[0], c[0], c[0], c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        
    elif choice == "57":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], d[0], c[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], d[0], c[0], c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "58":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "59":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)

    elif choice == "60":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], c[0], c[0], d[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], c[0], c[0], c[0], d[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
 
    elif choice == "61":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], c[0], c[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
 
    elif choice == "62":
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
        return "error"
    return username


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.الصيد"))
async def _(event):
    await event.edit(
        '''
**.صيد 1 : c_d_1 
.صيد 2 : c_d_s 
.صيد 3 : cc_dd 
.صيد 4 : cd_dc 
.صيد 5 : cd_cd 
.صيد 6 : cd_dd 
.صيد 7 : cd_cc 
.صيد 8 : cc_dc 
.صيد 9 : cc_cd 

.صيد 10 : d_ccc 
.صيد 11 : c_dcc 
.صيد 12 : c_cdc 
.صيد 13 : c_ccd 
.صيد 14 : ccc_d 
.صيد 15 : cdd_d 
.صيد 16 : ccd_c 
.صيد 17 : cdc_c 
.صيد 18 : dcc_c 

.صيد 19 : c_dcd 
.صيد 20 : cdc_d 
.صيد 21 : c_cdd 
.صيد 22 : ccd_d 
.صيد 23 : c_ddc 
.صيد 24 : cdd_c 

.صيد 25 : c_d_d_d 
.صيد 26 : c_d_c_c 
.صيد 27 : c_c_d_c 
.صيد 28 : c_c_c_d 

.صيد 29 : ccdddd 
.صيد 30 : cddccc 
.صيد 31 : ccddcc 
.صيد 32 : cccddc 
.صيد 33 : ccccdd 
.صيد 34 : cccddd 
.صيد 35 : cdcddd 
.صيد 36 : cdcdcc 
.صيد 37 : ccdcdc 
.صيد 38 : cccdcd 

.صيد 39 : cdccdc 
.صيد 40 : cddddc 
.صيد 41 : cddcdd 
.صيد 42 : ccdccd 
.صيد 43 : cdcccd 
.صيد 44 : cdddcd 

.صيد 45 : cdcdcd 
.صيد 46 : cdddcc 
.صيد 47 : ccdddc 
.صيد 48 : cdcddc 
.صيد 49 : cddcdc 
.صيد 50 : cdccdd 
.صيد 51 : cddccd 
.صيد 52 : ccdcdd 
.صيد 53 : ccddcd 

.صيد 54 : cddddddd 
.صيد 55 : cdcccccc 
.صيد 56 : ccdccccc 
.صيد 57 : cccdcccc 
.صيد 58 : ccccdccc 
.صيد 59 : cccccdcc 
.صيد 60 : ccccccdc 
.صيد 61 : cccccccd 

.صيد 62 : csdbot**

'''
    )

@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.الانواع"))
async def _(event):
    if ispay2[0] == "yes":
        await event.edit(tele_checker2)
    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")

@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.صيد"))
async def hunterusername(event):
    msg = event.text.split()
    choice = str(msg[1])
    try:
        ch = str(msg[2])
        if "@" in ch:
            ch = ch.replace("@", "")
        await event.edit(f"حسناً سيتم بدء الصيد في @{ch} .")
    except:
        try:
            ch = await eighthon(
                functions.channels.CreateChannelRequest(
                    title="Checker",
                    about="< We Are The Strongest >",
                )
            )
            ch = ch.updates[1].channel_id
            await event.edit(f"**تم انشاء القناة بنجاح سيتم صيد نوع {choice} !**")
        except Exception as e:
            await eighthon.send_message(
                event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**"
            )
    isclaim.clear()
    isclaim.append("on")
    for i in range(190000000):
        username = gen_user(choice)
        if username == "error":
            await event.edit("** يرجى وضع النوع بشكل صحيح**.")
            break
        isav = check_user(username)
        if isav == True:
            try:
                await eighthon(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_message(
                    event.chat_id,
                    f"**⌯ Hi New Telegram User\n\n⌯ UserName: - (@{username})\n\n⌯ Hunting Log {trys2[0]}\n\n⌯ by : @o_o_v\n\n⌯ by : @ppqbot**",
                )
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                pass
            except Exception as baned:
                if "(caused by UpdateUsernameRequest)" in str(baned):
                    pass
            except telethon.errors.FloodError as e:
                await eighthon.send_message(
                    event.chat_id,
                    f"للاسف تبندت , مدة الباند**-  ({e.seconds}) ثانية .**",
                    event.chat_id,
                    f"للاسف تبندت , مدة الباند**-  ({e.seconds}) ثانية .**",
                )
                break
            except Exception as eee:
                if "the username is already" in str(eee):
                    pass
                else:
                    await eighthon.send_message(
                        event.chat_id,
                        f"""- خطأ مع @{username} , الخطأ :{str(eee)}""",
                    )
                    break
        else:
            pass
        trys[0] += 1
    isclaim.clear()
    isclaim.append("off")
    await event.client.send_message(event.chat_id, "**تم بنجاح الصيد والانتهاء من الفحص**")


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.تثبيت"))
async def _(event):
    msg = event.text.split()
    try:
        ch = str(msg[2])
        await event.edit(f"حسناً سيتم بدء التثبيت في**-  @{ch} .**")
    except:
        try:
            ch = await eighthon(
                functions.channels.CreateChannelRequest(
                    title="Checker",
                    about="< We Are The Strongest >",
                )
            )
            ch = ch.updates[1].channel_id
            await event.edit(f"** تم بنجاح بدأ التثبيت**")
        except Exception as e:
            await eighthon.send_message(
                event.chat_id, f"خطأ في انشاء القناة , الخطأ : {str(e)}"
            )
    isauto.clear()
    isauto.append("on")
    username = str(msg[1])

    for i in range(1000000000):
        isav = check_user(username)
        if isav == True:
            try:
                await eighthon(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_message(
                    event.chat_id,
                    f"**⌯ Hi New Telegram User\n\n·––––––––––––––––·\n\n⌯ User : @{username}\n\n⌯ Hunting Log 0\n\n·––––––––––––––––·\n\n⌯ by : @o_o_v \n\n⎱ @ppqbot**",
                )
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(
                    event.chat_id, f"المعرف **-  @{username} غير صالح . **"
                )
                break
            except telethon.errors.FloodError as e:
                await eighthon.send_message(
                    event.chat_id, f"للاسف تبندت , مدة الباند ({e.seconds}) ثانية ."
                )
                break
            except Exception as eee:
                await eighthon.send_message(
                    event.chat_id,
                    f"""خطأ مع {username} , الخطأ :{str(eee)}""",
                )
                break
        else:
            pass
        trys2[0] += 1

        await asyncio.sleep(1.3)
    isclaim.clear()
    isclaim.append("off")
    await eighthon.send_message(event.chat_id, "**- تم الانتهاء من التثبيت بنجاح**")


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.حالة الصيد"))
async def _(event):
    if "on" in isclaim:
        await event.edit(f"** الصيد وصل لـ({trys[0]}) من المحاولات**")
    elif "off" in isclaim:
        await event.edit("** الصيد لا يعمل .**")
    else:
        await event.edit("- لقد حدث خطأ ما وتوقف الامر لديك")


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.حالة التثبيت"))
async def _(event):
    if "on" in isauto:
        await event.edit(f"**- التثبيت وصل لـ({trys2[0]}) من المحاولات**")
    elif "off" in isauto:
        await event.edit("**- التثبيت بالاصل لا يعمل .**")
    else:
        await event.edit("-لقد حدث خطأ ما وتوقف الامر لديك")
@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.ت (.*)"))
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

            @eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.حالة ت "))
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
                        await eighthon(functions.channels.UpdateUsernameRequest(
                            channel=ch, username=username))
                        await event.client.send_message(event.chat_id, f'''** 
⌯ Hi New Telegram User

⌯ UserName: - (@{username})

⌯ by : @o_o_v ⎱ by : @ppqbot **
    ''')
                        break
                    except telethon.errors.rpcerrorlist.UsernameInvalidError:
                        await event.client.send_message(event.chat_id, f"مبند `{username}` ❌❌")
                        break
                    except Exception as eee:

                        await eighthon.send_message(event.chat_id, f'''خطأ مع {username}
    الخطأ :
    {str(eee)}''')
                        if "A wait of" in str(eee):
                            break
                else:
                    pass
                trys += 1

                await asyncio.sleep(0.1)
            trys = ""
            isclaim.clear()
            isclaim.append("off")
            await eighthon.send_message(event.chat_id, "تم الانتهاء من التثبيت التلقائي")
        if msg[0] == "يدوي":  # تثبيت يدوي يوزر قناة
            await event.edit(f"حسناً سأحاول تثبيت `{username}` على `{ch}` !")
            msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
            username = str(msg[0])
            ch = str(msg[1])
            try:
                await eighthon(functions.channels.UpdateUsernameRequest(
                    channel=ch, username=username))
                await event.client.send_message(event.chat_id, f'''**
⌯ Hi New Telegram User

⌯ UserName: - (@{username})

⌯ by : @o_o_v ⎱ by : @ppqbot
-- -- -- -- -- -- -- -- -- -- -- -- -- **
    ''')
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(event.chat_id, f"مبند `{username}` ❌❌")
            except Exception as eee:
                await eighthon.send_message(event.chat_id, f'''خطأ مع {username}
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
