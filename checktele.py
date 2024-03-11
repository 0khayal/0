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

    elif choice == "2":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(b)
        f = [c[0], "_", d[0], "_", s[0]]
        username = ''.join(f)

    elif choice == "3":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = ''.join(f)

    elif choice == "4":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], "_", d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "5":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], "_", d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "6":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], "_", d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "7":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], "_", d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "8":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], "_", c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "9":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], "_", c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "10":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], "_", d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "11":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], "_", d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "12":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], "_", c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "13":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], "_", c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "14":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], "_", d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "15":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], "_", d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "16":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], "_", c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "17":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], "_", c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "18":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], "_", c[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
   
    elif choice == "19":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [d[0], "_", c[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "20":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], "_", d[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "21":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], "_", d[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "22":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], "_", c[0], d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "23":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], "_", c[0], d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "24":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], "_", c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "25":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], "_", c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "26":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], "_", d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "27":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], "_", d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "28":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], "_", d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "29":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], "_", d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "30":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], d[0], "_", c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "31":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], "_", c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "32":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], "_", c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "33":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], "_", c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "34":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [d[0], c[0], c[0], "_", c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "35":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [d[0], c[0], c[0], "_", c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "36":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], "_", d[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "37":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], "_", d[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "38":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], "_", d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "39":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], "_", d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "40":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], "_", c[0], d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "41":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], "_", c[0], d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "42":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], d[0], "_", d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "43":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], "_", d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "44":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], "_", d[0], d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "45":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], "_", d[0], d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "46":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], "_", c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "47":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], "_", c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "48":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], "_", d[0], "_", d[0], "_", d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "49":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], "_", d[0], "_", d[0], "_", d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "50":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], "_", d[0], "_", c[0], "_", c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "51":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], "_", d[0], "_", c[0], "_", c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "52":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], "_", c[0], "_", d[0], "_", c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "53":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], "_", c[0], "_", d[0], "_", c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "54":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], "_", c[0], "_", c[0], "_", d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "55":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], "_", c[0], "_", c[0], "_", d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "56":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], d[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "57":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "58":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "59":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "60":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], d[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "61":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "62":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], d[0], d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "63":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], d[0], d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "64":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "65":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "66":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "67":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "68":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "69":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "70":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "71":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "72":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], d[0], c[0], d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "73":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], c[0], d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "74":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], d[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "75":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], d[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "76":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "77":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "78":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], d[0], d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "79":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], d[0], d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "80":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], c[0], d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "81":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], c[0], d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "82":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], d[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "83":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "84":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "85":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "86":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], d[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "87":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], d[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "88":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], d[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "89":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], d[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "90":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "91":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "92":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], d[0], d[0], d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "93":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], d[0], d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "94":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], d[0], d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "95":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], d[0], d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "96":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], c[0], d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "97":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], c[0], d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "98":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "99":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "100":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "101":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "102":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], d[0], c[0], d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "103":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], c[0], d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "104":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], d[0], d[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "105":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], d[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "106":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "107":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "108":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "109":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "110":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], d[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "111":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "112":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "113":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "114":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "115":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "116":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "117":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "118":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], d[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "119":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], d[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "120":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "121":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "122":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], d[0], c[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "123":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], c[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "124":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], d[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "125":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], d[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "126":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
   
    elif choice == "127":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "128":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], c[0], d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "129":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], c[0], d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "130":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "131":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "132":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], d[0], d[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "133":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], d[0], d[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "134":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], c[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "135":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], c[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "136":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], d[0], c[0], c[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "137":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], c[0], c[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "138":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], d[0], c[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "139":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], d[0], c[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "140":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "141":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "142":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "143":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)        

    elif choice == "144":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], c[0], c[0], d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "145":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], c[0], c[0], d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "146":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)       

    elif choice == "147":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
        
    elif choice == "148":
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
**1 : c_1_2
2 : c_1_s / 3 : c_d_s
4 : cc_11 / 5 : cc_dd
6 : c1_1c / 7 : cd_dc
8 : c1_c1 / 9 : cd_cd
10 : c1_11 / 11 : cd_dd
12 : c1_cc / 13 : cd_cc
14 : cc_1c / 15 : cc_dc
16 : cc_c1 / 17 : cc_cd

 18 : d_111 / 19 : d_ccc
 20 : c_1cc / 21 : c_dcc
 22 : c_c1c / 23 : c_cdc
 24 : c_cc1 / 25 : c_ccd
 26 : ccc_1 / 27 : ccc_d
 28 : c11_1 / 29 : cdd_d
 30 : cc1_c / 31 : ccd_c
 32 : c1c_c / 33 : cdc_c
 34 : d11_1 / 35 : dcc_c
 36 : c_1c1 / 37 : c_dcd
 38 : c1c_1 / 39 : cdc_d
 40 : c_c11 / 41 : c_cdd
 42 : cc1_1 / 43 : ccd_d
 44 : c_11c / 45 : c_ddc
 46 : c11_c / 47 : cdd_c

48 : c_1_1_1 / 49 : c_d_d_d
50 : c_1_c_c / 51 : c_d_c_c
52 : c_c_1_c / 53 : c_c_d_c
54 : c_c_c_1 / 55 : c_c_c_d

56 : cc1111 / 57 : ccdddd
58 : c11ccc / 59 : cddccc
60 : cc11cc / 61 : ccddcc
62 : ccc11c / 63 : cccddc
64 : cccc11 / 65 : ccccdd
66 : ccc111 / 67 : cccddd
68 : c1c111 / 69 : cdcddd
70 : c1c1cc / 71 : cdcdcc
72 : cc1c1c / 73 : ccdcdc
74 : ccc1c1 / 75 : cccdcd
76 : c1cc1c / 77 : cdccdc
78 : c1111c / 79 : cddddc
  
80 : c11c11 / 81 : cddcdd
82 : cc1cc1 / 83 : ccdccd
84 : c1ccc1 / 85 : cdcccd
86 : c111c1 / 87 : cdddcd
88 : c1c1c1 / 89 : cdcdcd
90 : c111cc / 91 : cdddcc
92 : cc111c / 93 : ccdddc
94 : c1c11c / 95 : cdcddc
96 : c11c1c / 97 : cddcdc
98 : c1cc11 / 99 : cdccdd

100 : c11cc1 / 101 : cddccd
102 : cc1c11 / 103 : ccdcdd
104 : cc11c1 / 105 : ccddcd

106 : c11111 / 107 : cddddd
108 : c1cccc / 109 : cdcccc
110 : cc1ccc / 111 : ccdccc
112 : ccc1cc / 113 : cccdcc
114 : cccc1c / 115 : ccccdc
116 : ccccc1 / 117 : cccccd

118 : c111111 / 119 : cdddddd
120 : c1ccccc / 121 : cdccccc
122 : cc1cccc / 123 : ccdcccc
124 : ccc1ccc / 125 : cccdccc
126 : cccc1cc / 127 : ccccdcc
128 : ccccc1c / 129 : cccccdc
130 : cccccc1 / 131 : ccccccd

132 : c1111111 / 133 : cddddddd
134 : c1cccccc / 135 : cdcccccc
136 : cc1ccccc / 137 : ccdccccc
138 : ccc1cccc / 139 : cccdcccc
140 : cccc1ccc / 141 : ccccdccc
142 : ccccc1cc / 143 : cccccdcc
144 : cccccc1c / 145 : ccccccdc
146 : ccccccc1 / 147 : cccccccd

148 : csdbot**

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
                    title="CHECKER KHAYAL",
                    about="username was fished/n/nby: @o_o_v - @ppqbot",
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
                    f"**⌯ 𓆩 We are the strongest !'𓆪\n\n⎱ UserName: ↣ (@{username}❳!\n\n⎱ Hunting Log {trys2[0]}\n\n⎱ by : @o_o_v\n\n⎱ by : @ppqbot**",
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
                    title="CHECKER KHAYAL",
                    about="username was fished by : @o_o_v - @ppqbot",
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
        await event.edit("** الصيد  لا يعمل .**")
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
⌯ We are the strongest !'

⎱ UserName: ↣ (@{username}❳!

⎱ by : @o_o_v

⎱ by : @ppqbot **
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
⌯ We are the strongest !'

⎱ UserName: ↣ (@{username}❳!

⎱ by : @o_o_v

⎱ by : @ppqbot
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
