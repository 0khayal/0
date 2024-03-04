from pyrogram import Client,filters,idle
from pyrogram.raw import functions
import user_agent
from user_agent import generate_user_agent
import os
import random
from pyrogram.types import ReplyKeyboardMarkup
from queue import Queue
import datetime
import asyncio
from pyromod import listen
import pyromod
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup







kid = 26965358
khash = "0ef9b3131e2168949a634b7d5014290f"

bot = os.environ.get("token")

app = Client("jfd", api_id=kid, api_hash=khash, bot_token=bot)

ac = Client("tg", api_id=kid, api_hash=khash)

@app.on_message(filters.command("start"))
async def m(app,msg):
	await app.send_video(msg.chat.id, "https://telegra.ph/file/70b26b23a9febd3e34f3d.mp4", caption=f"""**Welcome .
This BoT Checker TeLeGram 🐊 
||ProGmMer : [hussien](https://t.me/hussien_pyrogram) .||**""", reply_markup=ReplyKeyboardMarkup(
    [[
      "– Turbo", f"@{msg.from_user.username}"
    ]]
  ))

@app.on_message(filters.command(" Turbo","–"))
async def m(app,msg):
    		await app.send_message(msg.chat.id, "اهلا بك في لوحه تحكم اختيار الرقم \n قم بتحديد الرقم لتذهب الى ازرار تحكم التيربو", reply_markup=ReplyKeyboardMarkup(
    [[
      "– Number ①", "– Number ②"
    ],[
      "– Number ③", "– Number ④"
    ],[
      "– Number ⑤", "– Number ⑥"
    ],[
      "– Number ⑦", "– Number ⑧"
    ],[
      "– Number ⑨", "– Number ①⓪"
    ],[ 
    "– Number ①①", "– Number ①②"
    ],[
      "– Number ①③", "– Number ①④"
    ]]
  ))
a = 'qwertyuiopassdfghjklzxcvbnm'
b = '1234567890'
e = 'qwertyuiopassdfghjklzxcvbnm'
	 	
sed = ["off"]

@app.on_message(filters.command(" Number ①","–"))
async def greetings(app,msg):
    	await app.send_message(msg.chat.id, "Wel .", reply_markup=ReplyKeyboardMarkup(
    [[
      "– DeLeTe The Number ①"
    ],[
      "– Add LiSt ①", "– DeLeTe LiSt ①"
    ],[
      "– Clicks LiSt ①"
    ],[
      "– UserName Availble ①"
    ],[
      "– UserName Last SeeN ①"
    ],[
      "– Add User in List ①", "– Delete ①"
    ],[
      "– Edit NaMe ①", "– Edit Bio ①"
    ]]
  ))


@app.on_message(filters.command(" Clicks LiSt ①","–"))
async def bhton(app,msg):
        while True :
            await asyncio.sleep(0.0)
            tr1 += 1 
        if "run" in sed:
       	 await app.send_message(msg.chat.id, f"List NuMber ① : ( {tr1} ) ")
        elif "off" in sed:
        		await app.send_message(msg.chat.id, " The NuMber ① . OFF 😤")

@app.on_message(filters.command(" DeLeTe The Number ①","–"))
async def bh(app,msg):
    	await app.send_message(msg.chat.id, "𝚃𝙷𝙴 𝙰𝙲𝙲𝙾𝚄𝙽𝚃 𝙸𝚂 𝙱𝙴𝙸𝙽𝙶 𝙻𝙾𝙶𝙶𝙴𝙳 𝙾𝚄𝚃....")
    	await app.send_message(msg.chat.id, "𝚂𝙸𝙶𝙽𝙴𝙳 𝙾𝚄𝚃 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 🫠🜾🫠")
    	# -
    	# -
    	# -
    	
@app.on_message(filters.command(" Add LiSt ①","–"))
async def turbo(app,msg):
    	await app.send_message(msg.chat.id, "𝐭.", reply_markup=ReplyKeyboardMarkup(
    [[
      "– CH ①", "– BotF ①"
    ]]
  ))

@app.on_message(filters.command(" DeLeTe LiSt ①","–"))
async def nn(app,msg):
	   	await app.send_message(msg.chat.id, "I am waiting ...")
	   	filename = "list.txt"
	   	os.remove(filename)
	   	f = open("list.txt", "x")
	   	await app.send_message(msg.chat.id,"DoNe DeLeTe ALL LiSt")
	   	
@app.on_message(filters.command(" Edit NaMe ①","–"))
async def Bh(app,msg):
	   	jmth = await app.ask(msg.chat.id, "Please SeNd Name NoW\nEx: Ahmed Ali")
	   	jmt = jmth.text
	   	await ac.update_profile(first_name=jmt)
	   	await app.send_message(msg.chat.id, f"تم بنجاح تغيير الاسم الى . {j}")
	   	return
@app.on_message(filters.command(" Edit Bio ①","–"))
async def mm(app,msg):
	   	pktk = await app.ask(msg.chat.id, "Please SeNd ThE Bio \nEx: hello me ali . . .")
	   	pio = pktk.text
	   	await ac.update_profile(bio=pio)
	   	await app.send_message(msg.chat.id, f"تم بنجاح تغيير البايو الى \n {pio}")
	   	
	   	
@app.on_message(filters.command(" UserName Availble ①","–"))
async def kkjs(app, msg):
    	await app.send_message(msg.chat.id, f"اهلا بك عزيزي . {msg.from_user.first_name} .\nاختر النوع الان من الازرار التاليه . ", reply_markup=ReplyKeyboardMarkup(
    [[
      "vip139 - ①", "aaaab"
    ],[
       "a_b_n - ①", "a_1_n - ①"
    ],[
      "a_6_1 - ①", "ab111 - ①"
    ],[
      "aaa111 - ①", "aaabbb - ①"
    ]]
  ))
  
@app.on_message(filters.command("_b_n - ①","a"))
async def ks(app, msg):
    	now = datetime.datetime.now()
    	await app.send_message(msg.chat.id, "DonE , a_b_n - ①")
    	c = random.choices(a)
    	d = random.choices(a)
    	s = random.choices(e)
    	f = [c[0], "_", s[0], "_", d[0]]
    	username = ''.join(f)
    	try: 
            await ac(GetPeerDialogsRequest(peers=[(username)])) 
            if "tgme_username_link" in username:
            	await app.send_message(msg.chat.id, f"متاح . @{username}\n وقت البوت هو . {now}")
    	except Exception as e:
    		print(e)

@app.on_message(filters.command("_1_n - ①","a"))
async def ks(app, msg):
    	await app.send_message(msg.chat.id, "DonE , a_1_n - ①")
    	now = datetime.datetime.now()
    	cc = random.choices(a)
    	dd = random.choices(b)
    	ss = random.choices(e)
    	f = [cc[0], "_", ss[0], "_", dd[0]]
    	username1 = ''.join(f)
    	try: 
            await ac(GetPeerDialogsRequest(peers=[(username)])) 
            if "tgme_username_link" in username1:
            	await app.send_message(msg.chat.id, f"متاح . @{username1}\n وقت البوت هو . {now}")
    	except Exception as e:
    		print(e)

   
   
	 		
@app.on_message(filters.command("_6_1 - ①","a"))
async def ksb(app, msg):
    	await app.send_message(msg.chat.id, "DonE , a_6_1 - ①")
    	ccc = random.choices(a)
    	ddd = random.choices(b)
    	sss = random.choices(b)
    	f = [ccc[0], "_", sss[0], "_", ddd[0]]
    	username = ''.join(f)
    	try: 
            await ac(GetPeerDialogsRequest(peers=[(username)])) 
            if "tgme_username_link" in username:
            	await app.send_message(msg.chat.id, f"متاح . @{username}\n وقت البوت هو . {now}")
    	except Exception as e:
    		print(e)
            	
@app.on_message(filters.command("aaab - ①","a"))
async def ks(app, msg):
    	await app.send_message(msg.chat.id, "DonE , aaaab - ①")
    	now = datetime.datetime.now()
    	cb = random.choices(a)
    	db = random.choices(b)
    	sb = random.choices(e)
    	f =  [cb[0], cb[0], cb[0], cb[0], sb[0]]
    	username = ''.join(f)
    	random.shuffle(f)
    	try: 
            await ac(GetPeerDialogsRequest(peers=[(username)])) 
            if "tgme_username_link" in username:
            	await app.send_message(msg.chat.id, f"متاح . @{username}\n وقت البوت هو . {now}")
    	except Exception as e:
    		print(e)

@app.on_message(filters.command("b111 - ①","a"))
async def ks(app, msg):
    	await app.send_message(msg.chat.id, "DonE , ab111 - ①")
    	now = datetime.datetime.now()
    	cq = random.choices(a)
    	dq = random.choices(b)
    	sq = random.choices(e)
    	f =  [cq[0], sq[0], dq[0], dq[0], dq[0]]
    	username = ''.join(f)
    	random.shuffle(f)
    	try: 
            await ac(GetPeerDialogsRequest(peers=[(username)])) 
            if "tgme_username_link" in username:
            	await app.send_message(msg.chat.id, f"متاح . @{username}\n وقت البوت هو . {now}")
    	except Exception as e:
    		print(e)
    		
@app.on_message(filters.command("ip139 - ①","v"))
async def ks(app, msg):
    	await app.send_message(msg.chat.id, "DonE , vip - ①")
    	now = datetime.datetime.now()
    	ka = random.choices(a)
    	fh = random.choices(b)
    	kk = random.choices(fh)
    	f =  ["vip", kk[0], kk[0], kk[0]]
    	username = ''.join(f)
    	try: 
            await ac(GetPeerDialogsRequest(peers=[(username)])) 
            if "tgme_username_link" in username:
            	await app.send_message(msg.chat.id, f"متاح . @{username}\n وقت البوت هو . {now}")
    	except Exception as e:
    		print(e)
    		
@app.on_message(filters.command("aa111 - ①","a"))
async def ks(app, msg):
    	await app.send_message(msg.chat.id, "DonE , aaa111 - ①")
    	now = datetime.datetime.now()
    	ia = random.choices(a)
    	ds = random.choices(b)
    	sb = random.choices(e)
    	f =  [ia[0], ia[0], ia[0], ds[0], ds[0], ds[0]]
    	username = ''.join(f)
    	random.shuffle(f)
    	try: 
            await ac(GetPeerDialogsRequest(peers=[(username)])) 
            if "tgme_username_link" in username:
            	await app.send_message(msg.chat.id, f"متاح . @{username}\n وقت البوت هو . {now}")
    	except Exception as e:
    		print(e)
    		ch = await ac.create_channel("عياله احنه البو محمد")
    		await ac.set_chat_username(ch,username6)
    		await app.send_message("حسن", f"تم صيد {username}")
    		
@app.on_message(filters.command("aabbb - ①","a"))
async def ks(app, msg):
    	await app.send_message(msg.chat.id, "DonE , aaabbb - ①")
    	ia = random.choices(a)
    	ds = random.choices(b)
    	ik = random.choices(e)
    	f =  [ia[0], ia[0], ia[0], ik[0], ik[0], ik[0]]
    	username = ''.join(f)
    	random.shuffle(f)
    	try: 
            await ac(GetPeerDialogsRequest(peers=[(username)])) 
            if "tgme_username_link" in username:
            	await app.send_message(msg.chat.id, f"متاح . @{username}\n وقت البوت هو . {now}")
    	except Exception as e:
    		print(e)
    		ch = await ac.create_channel("عياله احنه البو محمد")
    		await ac.set_chat_username(ch,username6)
    		await app.send_message("حسن", f"تم صيد {username}")

@app.on_message(filters.command(" Add User in list ①","–"))
async def ksk(app, msg):
    	user = await app.ask(msg.chat.id, "SeNd The UsEr..")
    	m = user.text
    	if "@" in user:
    		f = open("list.txt","a")
    		m = m.replace("@","")
    		if(not ex_id(str(m))):
    			f.write(f"{m}")
    			f.close()
    			await app.send_message(msg.chat.id, f"user : @{m}\nhas been Added to List !")
    		else:
    			f = open("list.txt","a")
    		if(not ex_id(str(m))):
    			f.write(f"{m}")
    			f.close()
    			await app.send_message(msg.chat.id,f"user : @{m}\nhas been Added to List !")
    		else:
    			await app.send_message(msg.chat.id, "The user is already pined !")
    			return 
    	
@app.on_message(filters.command(" DeLeTe ①","–"))
async def ks(app, msg):
    d = open("list.txt","r")
    cs = d.read()
    if cs != "\n":
    	afg = await app.ask(msg.chat.id, "Send The User \ndont @")
    	m = afg.text
    	if "@" in m:
    		m = m.replace("@","")
    	with open("list.txt", "r") as f:
    		lines = f.readlines()
    	with open("list.txt", "w") as f:
    		for line in lines:
    			if line.strip("\n") != f"{m}":
    				f.write(line)
    				await app.send_message(msg.chat.id,f"user : {m}\nhas been removed from pin !")
    			else:
    				with open("list.txt", "r") as f:
    					lines = f.readlines()
    				with open("list.txt", "w") as f:
    				        for line in lines:
    				        	if line.strip("\n") != f"{m}":
    				        		f.write(line)
    				        		await app.send_message(msg.chat.id, f"user : {m}\nhas been removed from pin !")
    				        	else:
    				        		await app.send_message(msg.chat.id, "there is no users pinned")
    				        		return
    	
    	    
@app.on_message(filters.command(" UserName Last SeeN ①","–"))
async def ks(app, msg):
    	await app.send_message(msg.chat.id, "oky now Locate....", reply_markup=ReplyKeyboardMarkup(
    [[
  	"ادخال وفحص - ①", "تخمين عشوائي - ①"
    ]]
  ))
@app.on_message(filters.command("خمين عشوائي - ①","ت"))
async def ks(app, msg):
    await app.send_message(msg.chat.id, "حدد النوع...", reply_markup=ReplyKeyboardMarkup(
    [[
  	"vip028 - ①.", "aaaae - ①."
	],[
	  "ak111 - ①."
    ]]
  ))
  
@app.on_message(filters.command("ip028 - ①.","v"))
async def ks(app, msg):
    	bbk = "1234567890"
    	km = "vip"
    	bh = random.choices(bbk)
    	bhton = [km[0], bh[0], bh[0], bh[0]]
    	userbam = "".join(bhton)
    	kmbe = await ac.get_users(userbam)
    	if "UserStatus.LONG_AGO" in kmbe:
    		await app.send_message(msg.chat.id, "جار تخمين يوزر جديد يرجى الانتضار لمده 3 ثواني")
    		while True :
    			
    			await asyncio.sleep(1)
    			msg.edit("①")
    			await asyncio.sleep(1)
    			msg.edit("②")
    			await asyncio.sleep(1)
    			msg.edit("③")
    			await app.send_message(msg.chat.id, f"@{bhton}\n{kmbe.next_offline_date}")
    			
@app.on_message(filters.command("aaae - ①.","a"))
async def ks(app, msg):
    	turb = random.choices(a)
    	bh = random.choices(a)
    	bhton1 = [turb[0], bh[0], bh[0], bh[0], bh[0]]
    	useram = "".join(bhton1)
    	kmbe = await ac.get_users(useram)
    	if "UserStatus.LONG_AGO" in kmbe:
    		await app.send_message(msg.chat.id, "جار تخمين يوزر جديد يرجى الانتضار لمده 3 ثواني")
    		while True :
    			await asyncio.sleep(1)
    			msg.edit("①")
    			await asyncio.sleep(1)
    			msg.edit("②")
    			await asyncio.sleep(1)
    			msg.edit("③")
    			await app.send_message(msg.chat.id, f"@{bhton1}\n{kmbe.next_offline_date}")
   
@app.on_message(filters.command("b111 - ①.","a"))
async def ks(app, msg):
    	cq = random.choices(a)
    	dq = random.choices(b)
    	sq = random.choices(e)
    	f =  [cq[0], sq[0], dq[0], dq[0], dq[0]]
    	username4 = ''.join(f)
    	random.shuffle(f)
    	kmbe = await ac.get_users(username4)
    	if "UserStatus.LONG_AGO" in kmbe:
    		await app.send_message(msg.chat.id, "جار تخمين يوزر جديد يرجى الانتضار لمده 3 ثواني")
    		while True :
    			await asyncio.sleep(1)
    			msg.edit("①")
    			await asyncio.sleep(1)
    			msg.edit("②")
    			await asyncio.sleep(1)
    			msg.edit("③")
    			await app.send_message(msg.chat.id, f"username:. @{username4}\n{kmbe.next_offline_date}")


@app.on_message(filters.command(" دخال وفحص - ①","ا"))
async def Bskk(app,msg):
	k = await app.ask(msg.chat.id, "SENd UserName")
	kh = k.text
	kn = await ac.get_users(kh)
	await app.send_message(msg.chat.id, f"User: @{kh}\n{kn.next_offline_date}")
	
@app.on_message(filters.command(" BotF ①","–"))
async def em(app,msg):
	    	btna1 = await app.ask(msg.chat.id, "send UsErs Now")
	    	Us = btna1.text
	    	await app.send_message(msg.chat.id, f"Done Start users")
	    	sed.clear()
	    	sed.append("run")
	    	await ac.send_message("botfather", "/newbot")
	    	

	    	for i in range(10000000000000000):
	    		break
	    	with open("list.txt","r+") as f :
	    		f.write(f"{Us}\n")
	    	try:
	    		k = open("list.txt","a")
	    		user = k.write(f"{Us}")
	    		
	    		await ac(GetPeerDialogsRequest(peers=[(user)])) 
	    	except Exception as e:
    			print(e)
	    	if "tgme_username_link" in Us:
    			try:
    				await ac.send_message("BotFather", f"{Us}")
    				await app.send_message(msg.chat.id, f"تم الصيد .! @{btna}")
    			except:
    				await app.send_message(msg.chat.id, f"حدث خطا مع {user}")
    				
@app.on_message(filters.command(" CH ①","–"))
async def m(app,msg):
	   	btna = await app.ask(msg.chat.id, "**||Send UsErS in LiSt**||\nEx: bbbfb\njjjij\nkkkk1\nvip89**||")
	   	ui = btna
	   	sed.clear()
	   	sed.append("run")
	   	with open("list.txt","r+") as f :
	   		f.write(f"{ui}\n")
	   	try:
	    		k = open("list.txt","a")
	    		user = k.write(f"{ui}")
	    		
	    		await ac(GetPeerDialogsRequest(peers=[(user)])) 
	   	except Exception as e:
    			print(e)
	   		
	   	if "tgme_username_link" in ui:
	   		try:
	   			ch = await ac.create_channel("A.b 🇮🇶")
	   			await ac.set_chat_username(ch, ui)
	   			msu = await ac.get_me(phone)
	   			await app.send_message(msg.chat.id, f"نحن الاقوى . 🐊\n المعرف : @{ui}\nالرقم : {msu}+")
	   		except:
	   			await app.send_message(msg.chat.id, f"حدث خطا مع {ui}")
	   		with open("list.txt", "a") as f:
	   			f.write(f"\n@{username}")
	   			sed.clear()
	   			sed.append("run")
	   			return
	



app.run()
print("شغال")
