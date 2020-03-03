#!/usr/bin/env python3

# IMPORTS
import sys
import re
import gzip

# VARIABLE INITIALIZATION

debug=0
printLines=0

# Define Functions
def Date():
	try:
		#date = re.search(r'date=(\d\d\d\d-\d\d-\d\d)',line).group(1)
		return re.search(r'date=(\S*?)\s',line).group(1)
	except:
		return ''

def Time():
	try:
		#time = re.search(r'time=(\d\d:\d\d:\d\d)',line).group(1)
		return re.search(r'time=(\S*?)\s',line).group(1)
	except:
		return ''

def Devname():
	try:
		return re.search(r'devname="(.*?)"',line).group(1)
	except:
		return ''

def Devid():
	try:
		return re.search(r'devid="(.*?)"',line).group(1)
	except:
		return ''

def Logid():
	try:
		return re.search(r'logid="(.*?)"',line).group(1)
	except:
		return ''

def Type():
	try:
		return re.search(r'type="(.*?)"',line).group(1)
	except:
		return ''	

def Subtype():
	try:
		return re.search(r'subtype="(.*?)"',line).group(1)
	except:
		return ''

def Level():
	try:
		return re.search(r'level="(.*?)"',line).group(1)
	except:
		return ''

def Vd():
	try:
		return re.search(r'vd="(.*?)"',line).group(1)
	except:
		return ''

def Eventtime():
	try:
		return re.search(r'eventtime=(\S*?)\s',line).group(1)
	except:
		return ''

def Srcip():
	try:
		return re.search(r'srcip=(\S*?)\s',line).group(1)
	except:
		return ''
		
def Srcport():
	try:
		return re.search(r'srcport=(\S*?)\s',line).group(1)
	except:
		return ''

def Srcintf():
	try:
		return re.search(r'srcintf="(.*?)"',line).group(1)
	except:
		return ''

def Srcintfrole():
	try:
		return re.search(r'srcintfrole="(.*?)"',line).group(1)
	except:
		return ''

def Dstip():
	try:
		return re.search(r'dstip=(\S*?)\s',line).group(1)
	except:
		return ''

def Dstport():
	try:
		return re.search(r'dstport=(\S*?)\s',line).group(1)
	except:
		return ''

def Dstintf():
	try:
		return re.search(r'dstintf="(.*?)"',line).group(1)
	except:
		return ''

def Dstintfrole():
	try:
		return re.search(r'dstintfrole="(.*?)"',line).group(1)
	except:
		return ''

def Sessionid():
	try:
		return re.search(r'sessionid=(\S*?)\s',line).group(1)
	except:
		return ''

def Proto():
	try:
		return re.search(r'proto=(\S*?)\s',line).group(1)
	except:
		return ''

def Prototranslated():
	if (proto != ''):
		if (proto == "1"):
			return "ICMP"
		if (proto == "6"):
			return "TCP"
		if (proto == "17"):
			return "UDP"
		else: return ""

def Action():
	try:
		return re.search(r'action="(.*?)"',line).group(1)
	except:
		return ''

def Policyid():
	try:
		return re.search(r'policyid=(\S*?)\s',line).group(1)
	except:
		return ''

def Policytype():
	try:
		return re.search(r'policytype="(.*?)"',line).group(1)
	except:
		return ''

def Policyname():
	try:
		return re.search(r'policyname="(.*?)"',line).group(1)
	except:
		return ''

def Poluuid():
	try:
		return re.search('poluuid="(.*?)"\s',line).group(1)
	except:
		return ''

def Service():
	try:
		return re.search(r'service="(.*?)"',line).group(1)
	except:
		return ''

def Dstcountry():
	try:
		return re.search(r'dstcountry="(.*?)"',line).group(1)
	except:
		return ''

def Srccountry():
	try:
		return re.search(r'srccountry="(.*?)"',line).group(1)
	except:
		return ''

def Trandisp():
	try:
		return re.search(r'trandisp="(.*?)"',line).group(1)
	except:
		return ''

def Duration():
	try:
		return re.search(r'duration=(\S*?)\s',line).group(1)
	except:
		return ''

def Sentbyte():
	try:
		return re.search(r'sentbyte=(\S*?)\s',line).group(1)
	except:
		return ''

def Rcvdbyte():
	try:
		return re.search(r'rcvdbyte=(\S*?)\s',line).group(1)
	except:
		return ''

def Sentpkt():
	try:
		return re.search(r'sentpkt=(\S*?)\s',line).group(1)
	except:
		return ''

def Rcvdpkt():
	try:
		return re.search(r'rcvdpkt=(\S*?)\s',line).group(1)
	except:
		return ''

def Sentdelta():
	try:
		return re.search(r'sentdelta=(\S*?)\s',line).group(1)
	except:
		return ''

def Rcvddelta():
	try:
		return re.search(r'rcvddelta=(\S*?)\s',line).group(1)
	except:
		return ''

def Wanin():
	try:
		return re.search(r'wanin=(\S*?)\s',line).group(1)
	except:
		return ''

def Wanout():
	try:
		return re.search(r'wanout=(\S*?)\s',line).group(1)
	except:
		return ''

def Lanin():
	try:
		return re.search(r'lanin=(\S*?)\s',line).group(1)
	except:
		return ''

def Lanout():
	try:
		return re.search(r'lanout=(\S*?)\s',line).group(1)
	except:
		return ''

def App():
	try:
		return re.search(r'app="(.*?)"',line).group(1)
	except:
		return ''

def Appcat():
	try:
		return re.search(r'appcat="(.*?)"',line).group(1)
	except:
		return ''

def Applist():
	try:
		return re.search(r'applist="(.*?)"',line).group(1)
	except:
		return ''

def Apprisk():
	try:
		return re.search(r'apprisk="(.*?)"',line).group(1)
	except:
		return ''

def Countapp():
	try:
		return re.search(r'countapp=(.*?)',line).group(1)
	except:
		return ''

def Appid():
	try:
		return re.search(r'appid=(\S*?)\s',line).group(1)
	except:
		return ''

def Crscore():
	try:
		return re.search(r'crscore=(\S*?)\s',line).group(1)
	except:
		return ''

def Craction():
	try:
		return re.search(r'craction=(\S*?)\s',line).group(1)
	except:
		return ''

def Crlevel():
	try:
		return re.search(r'crlevel="(.*?)"',line).group(1)
	except:
		return ''

def Tranip():
	try:
		return re.search(r'tranip=(\S*?)\s',line).group(1)
	except:
		return ''

def Tranport():
	try:
		return re.search(r'tranport=(\S*?)\s',line).group(1)
	except:
		return ''

def Transip():
	try:
		return re.search(r'transip=(\S*?)\s',line).group(1)
	except:
		return ''

def Transport():
	try:
		return re.search(r'transport=(\S*?)\s',line).group(1)
	except:
		return ''

def Utmaction():
	try:
		return re.search(r'utmaction=(\S*?)\s',line).group(1)
	except:
		return ''

def Direction():
	try:
		return re.search(r'direction="(.*?)"',line).group(1)
	except:
		return ''

def Hostname():
	try:
		return re.search(r'hostname="(.*?)"',line).group(1)
	except:
		return ''

def Incidentserailno():
	try:
		return re.search(r'incidentserialno=(\S*?)\s',line).group(1)
	except:
		return ''

def Url():
	try:
		return re.search(r'url="(.*?)"',line).group(1)
	except:
		return ''

def Msg():
	try:
		return re.search(r'msg="(.*?)"',line).group(1)
	except:
		return ''

def Scertcname():
	try:
		return re.search(r'scertcname="(.*?)"',line).group(1)
	except:
		return ''

def Eventtype():
	try:
		return re.search(r'eventtype="(.*?)"',line).group(1)
	except:
		return ''

def Logdesc():
	try:
		return re.search(r'logdesc="(.*?)"',line).group(1)
	except:
		return ''

def Saddr():
	try:
		return re.search(r'saddr="(.*?)"',line).group(1)
	except:
		return ''

def Nat():
	try:
		return re.search(r'nat=(\S*?)\s',line).group(1)
	except:
		return ''

def Portbegin():
	try:
		return re.search(r'portbegin=(\S*?)\s',line).group(1)
	except:
		return ''

def Portend():
	try:
		return re.search(r'portend=(\S*?)\s',line).group(1)
	except:
		return ''

def Poolname():
	try:
		return re.search(r'poolname="(.*?)"',line).group(1)
	except:
		return ''

def Cpu():
	try:
		return re.search(r'cpu=(\S*?)\s',line).group(1)
	except:
		return ''

def Mem():
	try:
		return re.search(r'mem=(\S*?)\s',line).group(1)
	except:
		return ''

def Totalsession():
	try:
		return re.search(r'totalsession=(\S*?)\s',line).group(1)
	except:
		return ''

def Disk():
	try:
		return re.search(r'disk=(\S*?)\s',line).group(1)
	except:
		return ''

def Setuprate():
	try:
		return re.search(r'setuprate=(\S*?)\s',line).group(1)
	except:
		return ''

def Disklograte():
	try:
		return re.search(r'disklograte=(\S*?)\s',line).group(1)
	except:
		return ''

def Fazlograte():
	try:
		return re.search(r'fazlograte=(\S*?)\s',line).group(1)
	except:
		return ''

def Bandwidth():
	try:
		return re.search(r'bandwidth="(.*?)"',line).group(1)
	except:
		return ''
	
def Username():
	try:
		return re.search(r'user="(.*?)"',line).group(1)
	except:
		return ''

def Usergroup():
	try:
		return re.search(r'group="(.*?)"',line).group(1)
	except:
		return ''
	
def Authserver():
	try:
		return re.search(r'authserver="(.*?)"',line).group(1)
	except:
		return ''
	
def Tunneltype():
	try:
		return re.search(r'tunneltype="(.*?)"',line).group(1)
	except:
		return ''
	
def Tunnelid():
	try:
		return re.search(r'tunnelid=(\S*?)\s',line).group(1)
	except:
		return ''
	
def Remip():
	try:
		return re.search(r'remip=(\S*?)\s',line).group(1)
	except:
		return ''
	
def Dst_host():
	try:
		return re.search(r'dst_host="(.*?)"',line).group(1)
	except:
		return ''
	
def Reason():
	try:
		return re.search(r'reason="(.*?)"',line).group(1)
	except:
		return ''
	
def Status():
	try:
		return re.search(r'status="(.*?)"',line).group(1)
	except:
		return ''
	
def Devtype():
	try:
		return re.search(r'devtype="(.*?)"',line).group(1)
	except:
		return ''
	
def Devcategory():
	try:
		return re.search(r'devcategory="(.?*)"',line).group(1)
	except:
		return ''
	
def Mastersrcmac():
	try:
		return re.search(r'mastersrcmac="(.*?)"',line).group(1)
	except:
		return ''
	
def Srcmac():
	try:
		return re.search(r'srcmac="(.*?)"',line).group(1)
	except:
		return ''
	
def Srcserver():
	try:
		return re.search(r'srcserver=(\S*?)\s',line).group(1)
	except:
		return ''



if (debug>=1): print("DEBUG LEVEL:",debug)

#OPEN LOGFILE
#fwlog = open("/path/to/file/to/read","r")
args=sys.argv
try:
	filestring = str(args[1])
except:
	filestring=''
try:
	gzDirectory = str(args[2])
except:
	gzDirectory = '.'
filedatetime = str(re.search(r'.?(\d{12})',filestring).group(1))
#fwlog = open(str(args[1]),"r")
#Kept having errors about UTF-8 decodes, found this online https://stackoverflow.com/questions/42339876/error-unicodedecodeerror-utf-8-codec-cant-decode-byte-0xff-in-position-0-in
fwlog = open(filestring,"r",encoding="utf8", errors='ignore')


#OPEN FILES TO WRITE - if writing files
trafficFile = "traffic-" + filedatetime + ".csv" + ".gz"
trafficPath = gzDirectory + "/" + trafficFile
utmFile = "utm-" + filedatetime + ".csv" + ".gz"
utmPath = gzDirectory + "/" + utmFile
eventFile = "event-" + filedatetime + ".csv" + ".gz"
eventPath = gzDirectory + "/" + eventFile

#trafficGZ = gzip.open(trafficPath,'wb',9)
trafficGZ = gzip.open(trafficPath,'wt',9)
utmGZ = gzip.open(utmPath,'wt',9)
eventGZ = gzip.open(eventPath,'wt',9)

# IF DEBUG - print the filename being read
if (debug>=3): 
	print(str(args[1]))
	print(filestring)
	print(filedatetime)
	print(trafficFile)
	print(gzDirectory)
	print(trafficPath)

#exit()
# start of loop
for line in fwlog:
	# strip the line of any CR characters
	y=line.rstrip('\r\n')
	# print the line being processed if debug is on
	if (debug>=4): print(y)
	# need to determine the type before proceeding
	type=Type()
	date=Date()
	time=Time()
	devname=Devname()
	devid=Devid()
	logid=Logid()
	subtype=Subtype()
	level=Level()
	vd=Vd()
	eventtime=Eventtime()


	if (type == 'traffic'): #process TRAFFIC
		srcip=Srcip()
		srcport=Srcport()
		srcintf=Srcintf()
		srcintfrole=Srcintfrole()
		dstip=Dstip()
		dstport=Dstport()
		dstintf=Dstintf()
		dstintfrole=Dstintfrole()
		sessionid=Sessionid()
		proto=Proto()
		prototranslated=Prototranslated()
		action=Action()
		policyid=Policyid()
		policytype=Policytype()
		policyname=Policyname()
		poluuid=Poluuid()
		service=Service()
		dstcountry=Dstcountry()
		srccountry=Srccountry()
		trandisp=Trandisp()
		duration=Duration()
		sentbyte=Sentbyte()
		rcvdbyte=Rcvdbyte()
		sentpkt=Sentpkt()
		rcvdpkt=Rcvdpkt()
		sentdelta=Sentdelta()
		rcvddelta=Rcvddelta()
		wanin=Wanin()
		wanout=Wanout()
		lanin=Lanin()
		lanout=Lanout()
		app=App()
		appid=Appid()
		appcat=Appcat()
		apprisk=Apprisk()
		applist=Applist()
		countapp=Countapp()
		crscore=Crscore()
		craction=Craction()
		crlevel=Crlevel()
		tranip=Tranip()
		tranport=Tranport()
		transip=Transip()
		transport=Transport()
		utmaction=Utmaction()
		username=Username()
		usergroup=Usergroup()
		authserver=Authserver()
		devtype=Devtype()
		devcategory=Devcategory()
		mastersrcmac=Mastersrcmac()
		srcmac=Srcmac()
		srcserver=Srcserver()
		
		myList=[date,time,devname,devid,level,eventtime,type,subtype,vd,action,srcintfrole,srcintf,srcip,srcport,srccountry,dstintfrole,dstintf,dstip,dstport,prototranslated,proto,dstcountry,service,trandisp,transip,transport,tranip,tranport,policytype,policyid,policyname,app,appid,appcat,apprisk,applist,logid,countapp,crscore,craction,crlevel,duration,sentbyte,rcvdbyte,sentpkt,rcvdpkt,wanin,wanout,lanin,lanout,sentdelta,rcvddelta,utmaction,poluuid,sessionid,username,usergroup,authserver,devtype,devcategory,mastersrcmac,srcmac,srcserver]
		csvString=','.join(map(str, myList))
		if (debug>=2):
			print('date:',date)
			print('time:',time)
			print('devname:',devname)
			print('devid:',devid)
			print('logid:',logid)
			print('type:',type)
			print('subtype:',subtype)
			print('level:',level)
			print('vd:',vd)
			print('eventtime:',eventtime)
			print('srcip:',srcip)
			print('srcport:',srcport)
			print('srcintf:',srcintf)
			print('srcintfrole:',srcintfrole)
			print('dstip:',dstip)
			print('dstport:',dstport)
			print('dstintf:',dstintf)
			print('dstintfrole:',dstintfrole)
			print('sessionid:',sessionid)
			print('proto:',proto)
			print('action:',action)
			print('policyname:',policyname)
			print('policyid:',policyid)
			print('poliyctype:',policytype)
			print('service:',service)
			print('dstcountry:',dstcountry)
			print('srccountry:',srccountry)
			print('trandisp:',trandisp)
			print('duration:',duration)
			print('sentbyte:',sentbyte)
			print('rcvdbyte:',rcvdbyte)
			print('sentpkt:',sentpkt)
			print('rcvdpkt:',rcvdpkt)
			print('sentdelta:',sentdelta)
			print('rcvddelta:',rcvddelta)
			print('wanin:',wanin)
			print('wanout:',wanout)
			print('lanin:',lanin)
			print('lanout:',lanout)
			print('app:',app)
			print('appid:',appid)
			print('appcat:',appcat)
			print('apprisk:',apprisk)
			print('applist:',applist)
			print('countapp:',countapp)
			print('crscore:',crscore)
			print('craction:',craction)
			print('crlevel:',crlevel)
			print('tranip:',tranip)
			print('tranport:',tranport)
			print('transip:',transip)
			print('transport:',transport)
			print('poluuid:',poluuid)
			print('user:',username)
			print('group:',usergroup)
			print('authserver:',authserver)
			print('devtype:',devtype)
			print('devcategory:',devcategory)
			print('mastersrcmac:',mastersrcmac)
			print('srcmac:',srcmac)
			print('srcserver:',srcserver)
			print(myList)

		if (printLines > 0): print(csvString)
		#trafficGZ.write(csvString.encode()+"\n".encode())
		trafficGZ.write(csvString + "\n")

		
	if (type == 'utm'): #process UTM
		srcip=Srcip()
		srcport=Srcport()
		srcintf=Srcintf()
		srcintfrole=Srcintfrole()
		dstip=Dstip()
		dstport=Dstport()
		dstintf=Dstintf()
		dstintfrole=Dstintfrole()
		sessionid=Sessionid()
		proto=Proto()
		prototranslated=Prototranslated()
		action=Action()
		policyid=Policyid()
		service=Service()
		app=App()
		appid=Appid()
		appcat=Appcat()
		apprisk=Apprisk()
		applist=Applist()
		direction=Direction()
		hostname=Hostname()
		incidentserialno=Incidentserailno()
		url=Url()
		msg=Msg()
		scertcname=Scertcname()
		eventtype=Eventtype()
		username=Username()
		usergroup=Usergroup()
		authserver=Authserver()
		
		myList=[date,time,devname,devid,level,eventtime,type,subtype,vd,action,srcintfrole,srcintf,srcip,srcport,dstintfrole,dstintf,dstip,dstport,prototranslated,proto,service,direction,policyid,app,appid,appcat,apprisk,applist,logid,hostname,url,scertcname,incidentserialno,eventtype,sessionid,msg,username,usergroup,authserver]
		csvString=','.join(map(str, myList))
		if (debug>=2):
			print('date:',date)
			print('time:',time)
			print('devname:',devname)
			print('devid:',devid)
			print('logid:',logid)
			print('type:',type)
			print('subtype:',subtype)
			print('level:',level)
			print('vd:',vd)
			print('eventtime:',eventtime)
			print('eventtype:',eventtype)
			print('srcip:',srcip)
			print('srcport:',srcport)
			print('srcintf:',srcintf)
			print('srcintfrole:',srcintfrole)
			print('dstip:',dstip)
			print('dstport:',dstport)
			print('dstintf:',dstintf)
			print('dstintfrole:',dstintfrole)
			print('sessionid:',sessionid)
			print('proto:',proto)
			print('prototranslated:',prototranslated)
			print('action:',action)
			print('policyid:',policyid)
			print('service:',service)
			print('app:',app)
			print('appcat:',appcat)
			print('appid:',appid)
			print('applist:',applist)
			print('apprisk:',apprisk)
			print('direction:',direction)
			print('hostname:',hostname)
			print('url:',url)
			print('scertcname:',scertcname)
			print('eventtype:',eventtype)
			print('incidentserialno:',incidentserialno)
			print('msg:',msg)
			print('user:',username)
			print('group:',usergroup)
			print('authserver:',authserver)		

			print(myList)

		if (printLines > 0): print(csvString)
		#utmGZ.write(csvString.encode()+"\n".encode())
		utmGZ.write(csvString + "\n")
		
	if (type == 'event'): #process event logs
		logdesc=Logdesc()
		action=Action()
		saddr=Saddr()
		nat=Nat()
		portbegin=Portbegin()
		portend=Portend()
		poolname=Poolname()
		duration=Duration()
		msg=Msg()
		cpu=Cpu()
		mem=Mem()
		totalsession=Totalsession()
		disk=Disk()
		bandwidth=Bandwidth()
		setuprate=Setuprate()
		disklograte=Disklograte()
		fazlograte=Fazlograte()
		username=Username()
		usergroup=Usergroup()
		authserver=Authserver()
		tunneltype=Tunneltype()
		tunnelid=Tunnelid()
		remip=Remip()
		dst_host=Dst_host()
		reason=Reason()
		status=Status()		
		
		
		myList=[date,time,devname,devid,level,eventtime,type,subtype,vd,action,logdesc,saddr,nat,portbegin,portend,poolname,duration,cpu,mem,disk,totalsession,bandwidth,setuprate,disklograte,fazlograte,logid,msg,username,usergroup,authserver,tunneltype,tunnelid,remip,dst_host,reason,status]
		csvString=','.join(map(str, myList))
		if (debug>=2):
			print('date:',date)
			print('time:',time)
			print('devname:',devname)
			print('devid:',devid)
			print('level:',level)
			print('eventtime:',eventtime)
			print('type:',type)
			print('subtype:',subtype)
			print('vd:',vd)
			print('action:',action)
			print('logdesc:',logdesc)
			print('saddr:',saddr)
			print('nat:',nat)
			print('portbegin:',portbegin)
			print('portend:',portend)
			print('poolname:',poolname)
			print('duration:',duration)
			print('cpu:',cpu)
			print('mem:',mem)
			print('disk:',disk)
			print('totalsession:',totalsession)
			print('bandwidth:',bandwidth)
			print('setuprate:',setuprate)
			print('disklograte:',disklograte)
			print('fazlograte:',fazlograte)
			print('logid:',logid)
			print('msg:',msg)
			print('user:',username)
			print('group:',groupname)
			print('authserver:',authserver)
			print('tunneltype:',tunneltype)
			print('tunnelid:',tunnelid)
			print('remip:',remip)
			print('dst_host:',dst_host)
			print('reason:',reason)
			print('status:',status)

			print(myList)

		if (printLines > 0): print(csvString)
		#eventGZ.write(csvString.encode()+"\n".encode())
		eventGZ.write(csvString + "\n")		
		
	
	
trafficGZ.close()	
utmGZ.close()
eventGZ.close()
if (printLines > 0): print("END")

#example for groups
#email_address = 'Please contact us at: support@datacamp.com'
#match = re.search(r'([\w\.-]+)@([\w\.-]+)', email_address)
#if match:
#  print(match.group()) # The whole matched text
#  print(match.group(1)) # The username (group 1)
#  print(match.group(2)) # The host (group 2)
