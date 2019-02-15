#!/usr/bin/env python3

# IMPORTS
import sys
import re
import gzip


# VARIABLE INITIALIZATION


debug=0
printLines=0

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
fwlog = open(filestring,"r")


#OPEN FILES TO WRITE - if writing files
trafficFile = "traffic-" + filedatetime + ".csv" + ".gz"
trafficPath = gzDirectory + "/" + trafficFile
utmFile = "utm-" + filedatetime + ".csv" + ".gz"
utmPath = gzDirectory + "/" + utmFile

#trafficGZ = gzip.open(trafficPath,'wb',9)
trafficGZ = gzip.open(trafficPath,'wt',9)
utmGZ = gzip.open(utmPath,'wt',9)

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
	if (debug>=1): print(y)
	# need to determine the type before proceeding
	#type
	try:
		type = re.search(r'type="(.*?)"',line).group(1)
	except:
		type = ''	

	#date
	try:
		#date = re.search(r'date=(\d\d\d\d-\d\d-\d\d)',line).group(1)
		date = re.search(r'date=(\S*?)\s',line).group(1)
	except:
		date = ''
	
	
	#time
	try:
		#time = re.search(r'time=(\d\d:\d\d:\d\d)',line).group(1)
		time = re.search(r'time=(\S*?)\s',line).group(1)
	except:
		time = ''

		
	#devname
	try:
		devname = re.search(r'devname="(.*?)"',line).group(1)
	except:
		devname = ''
	
	
	#devid
	try:
		devid = re.search(r'devid="(.*?)"',line).group(1)
	except:
		devid = ''
	
	
	#logid
	try:
		logid = re.search(r'logid="(.*?)"',line).group(1)
	except:
		logid = ''
	

	#subtype
	try:
		subtype = re.search(r'subtype="(.*?)"',line).group(1)
	except:
		subtype = ''
	
	
	#level
	try:
		level = re.search(r'level="(.*?)"',line).group(1)
	except:
		level = ''

	#vd
	try:
		vd = re.search(r'vd="(.*?)"',line).group(1)
	except:
		vd = ''		
	
	#eventtime
	try:
		eventtime = re.search(r'eventtime=(\S*?)\s',line).group(1)
	except:
		eventtime = ''
		
			
#	if False:	
	if (type == 'traffic'): #process TRAFFIC
		
		#vd
		try:
			vd = re.search(r'vd="(.*?)"',line).group(1)
		except:
			vd = ''
		
		
		#eventtime
		try:
			eventtime = re.search(r'eventtime=(\S*?)\s',line).group(1)
		except:
			eventtime = ''
		
		
		#srcip
		try:
			srcip = re.search(r'srcip=(\S*?)\s',line).group(1)
		except:
			srcip = ''
		
		
		#srcport
		try:
			srcport = re.search(r'srcport=(\S*?)\s',line).group(1)
		except:
			srcport = ''
		
		
		#srcintf
		try:
			srcintf = re.search(r'srcintf="(.*?)"',line).group(1)
		except:
			srcintf = ''
		
		
		#srcintfrole
		try:
			srcintfrole = re.search(r'srcintfrole="(.*?)"',line).group(1)
		except:
			srcintfrole = ''
		
		
		#dstip
		try:
			dstip = re.search(r'dstip=(\S*?)\s',line).group(1)
		except:
			dstip = ''
		
		
		#dstport
		try:
			dstport = re.search(r'dstport=(\S*?)\s',line).group(1)
		except:
			dstport = ''
		
		
		#dstintf
		try:
			dstintf = re.search(r'dstintf="(.*?)"',line).group(1)
		except:
			dstintf = ''
		
		
		#dstintfrole
		try:
			dstintfrole = re.search(r'dstintfrole="(.*?)"',line).group(1)
		except:
			dstintfrole = ''
		
		
		#sessionid
		try:
			sessionid = re.search(r'sessionid=(\S*?)\s',line).group(1)
		except:
			sessionid = ''
		
		
		#proto
		try:
			proto = re.search(r'proto=(\S*?)\s',line).group(1)
		except:
			proto = ''
		if (proto != ''):
			if (proto == "1"):
				prototranslated = "ICMP"
			if (proto == "6"):
				prototranslated = "TCP"
			if (proto == "17"):
				prototranslated = "UDP"
			else: prototranslated = ""
		
		#action
		try:
			action = re.search(r'action="(.*?)"',line).group(1)
		except:
			action = ''
		
		
		#policyid
		try:
			policyid = re.search(r'policyid=(\S*?)\s',line).group(1)
		except:
			policyid = ''
		
		
		#policytype
		try:
			policytype = re.search(r'policytype="(.*?)"',line).group(1)
		except:
			policytype = ''
		
		#policyname
		try:
			policyname = re.search(r'policyname="(.*?)"',line).group(1)
		except:
			policyname = ''
			
		#poluuid
		try:
			poluuid = re.search('poluuid="(.*?)"\s',line).group(1)
		except:
			poluuid = ''
		
		#service
		try:
			service = re.search(r'service="(.*?)"',line).group(1)
		except:
			service = ''
		
		
		#dstcountry
		try:
			dstcountry = re.search(r'dstcountry="(.*?)"',line).group(1)
		except:
			dstcountry = ''
		
		
		#srccountry
		try:
			srccountry = re.search(r'srccountry="(.*?)"',line).group(1)
		except:
			srccountry = ''
		
		
		#trandisp
		try:
			trandisp = re.search(r'trandisp="(.*?)"',line).group(1)
		except:
			trandisp = ''
		
		
		#duration
		try:
			duration = re.search(r'duration=(\S*?)\s',line).group(1)
		except:
			duration = ''
		
		
		#sentbyte
		try:
			sentbyte = re.search(r'sentbyte=(\S*?)\s',line).group(1)
		except:
			sentbyte = ''
		
		
		#rcvdbyte
		try:
			rcvdbyte = re.search(r'rcvdbyte=(\S*?)\s',line).group(1)
		except:
			rcvdbyte = ''
		
		
		#sentpkt
		try:
			sentpkt = re.search(r'sentpkt=(\S*?)\s',line).group(1)
		except:
			sentpkt = ''

		#rcvdpkt
		try:
			rcvdpkt = re.search(r'rcvdpkt=(\S*?)\s',line).group(1)
		except:
			rcvdpkt = ''

		#sentdelta
		try:
			sentdelta = re.search(r'sentdelta=(\S*?)\s',line).group(1)
		except:
			sentdelta = ''

		#rcvddelta
		try:
			rcvddelta = re.search(r'rcvddelta=(\S*?)\s',line).group(1)
		except:
			rcvddelta = ''			

		#wanin
		try:
			wanin = re.search(r'wanin=(\S*?)\s',line).group(1)
		except:
			wanin = ''

		#wanout
		try:
			wanout = re.search(r'wanout=(\S*?)\s',line).group(1)
		except:
			wanout = ''	
			
		#lanin
		try:
			lanin = re.search(r'lanin=(\S*?)\s',line).group(1)
		except:
			lanin = ''

		#lanout
		try:
			lanout = re.search(r'lanout=(\S*?)\s',line).group(1)
		except:
			lanout = ''			

		#app
		try:
			app = re.search(r'app="(.*?)"',line).group(1)
		except:
			app = ''
		
			
		#appcat
		try:
			appcat = re.search(r'appcat="(.*?)"',line).group(1)
		except:
			appcat = ''
		
		#applist
		try:
			applist = re.search(r'applist="(.*?)"',line).group(1)
		except:
			applist = ''

		#apprisk
		try:
			apprisk = re.search(r'apprisk="(.*?)"',line).group(1)
		except:
			apprisk = ''		

		#countapp
		try:
			countapp = re.search(r'countapp=(.*?)',line).group(1)
		except:
			countapp = ''			
			
		#appid
		try:
			appid = re.search(r'appid=(\S*?)\s',line).group(1)
		except:
			appid = ''
			
		#crscore
		try:
			crscore = re.search(r'crscore=(\S*?)\s',line).group(1)
		except:
			crscore = ''
		
		
		#craction
		try:
			craction = re.search(r'craction=(\S*?)\s',line).group(1)
		except:
			craction = ''
		
		
		#crlevel
		try:
			crlevel = re.search(r'crlevel="(.*?)"',line).group(1)
		except:
			crlevel = ''
		
		
		#tranip
		try:
			tranip = re.search(r'tranip=(\S*?)\s',line).group(1)
		except:
			tranip = ''
		
		
		#tranport
		try:
			tranport = re.search(r'tranport=(\S*?)\s',line).group(1)
		except:
			tranport = ''

		#transip
		try:
			transip = re.search(r'transip=(\S*?)\s',line).group(1)
		except:
			transip = ''
		
		
		#transport
		try:
			transport = re.search(r'transport=(\S*?)\s',line).group(1)
		except:
			transport = ''		
			
		#utmaction
		try:
			utmaction = re.search(r'utmaction=(\S*?)\s',line).group(1)
		except:
			utmaction = ''		
		
			
		
		myList=[date,time,devname,devid,level,eventtime,type,subtype,vd,action,srcintfrole,srcintf,srcip,srcport,srccountry,dstintfrole,dstintf,dstip,dstport,prototranslated,proto,dstcountry,service,trandisp,transip,transport,tranip,tranport,policytype,policyid,policyname,app,appid,appcat,apprisk,applist,logid,countapp,crscore,craction,crlevel,duration,sentbyte,rcvdbyte,sentpkt,rcvdpkt,wanin,wanout,lanin,lanout,sentdelta,rcvddelta,utmaction,poluuid]
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
			print(myList)

		if (printLines > 0): print(csvString)
		#trafficGZ.write(csvString.encode()+"\n".encode())
		trafficGZ.write(csvString + "\n")

		
	if (type == 'utm'): #process UTM
		

		
		

		#srcip
		try:
			srcip = re.search(r'srcip=(\S*?)\s',line).group(1)
		except:
			srcip = ''
		
		
		#srcport
		try:
			srcport = re.search(r'srcport=(\S*?)\s',line).group(1)
		except:
			srcport = ''
		
		
		#srcintf
		try:
			srcintf = re.search(r'srcintf="(.*?)"',line).group(1)
		except:
			srcintf = ''
		
		
		#srcintfrole
		try:
			srcintfrole = re.search(r'srcintfrole="(.*?)"',line).group(1)
		except:
			srcintfrole = ''
		
		
		#dstip
		try:
			dstip = re.search(r'dstip=(\S*?)\s',line).group(1)
		except:
			dstip = ''
		
		
		#dstport
		try:
			dstport = re.search(r'dstport=(\S*?)\s',line).group(1)
		except:
			dstport = ''
		
		
		#dstintf
		try:
			dstintf = re.search(r'dstintf="(.*?)"',line).group(1)
		except:
			dstintf = ''
		
		
		#dstintfrole
		try:
			dstintfrole = re.search(r'dstintfrole="(.*?)"',line).group(1)
		except:
			dstintfrole = ''
		
		
		#sessionid
		try:
			sessionid = re.search(r'sessionid=(\S*?)\s',line).group(1)
		except:
			sessionid = ''
		
		
		#proto
		try:
			proto = re.search(r'proto=(\S*?)\s',line).group(1)
		except:
			proto = ''
		if (proto != ''):
			if (proto == "1"):
				prototranslated = "ICMP"
			elif (proto == "6"):
				prototranslated = "TCP"
			elif (proto == "17"):
				prototranslated = "UDP"
			else: prototranslated = ""
		
		#action
		try:
			action = re.search(r'action="(.*?)"',line).group(1)
		except:
			action = ''
		
		
		#policyid
		try:
			policyid = re.search(r'policyid=(\S*?)\s',line).group(1)
		except:
			policyid = ''
		
		
		#service
		try:
			service = re.search(r'service="(.*?)"',line).group(1)
		except:
			service = ''

			
		#appcat
		try:
			appcat = re.search(r'appcat="(.*?)"',line).group(1)
		except:
			appcat = ''
		
		#appid
		try:
			appid = re.search(r'appid=(\S*?)\s',line).group(1)
		except:
			appid = ''	

		#direction
		try:
			direction = re.search(r'direction="(.*?)"',line).group(1)
		except:
			direction = ''			
			
		#applist
		try:
			applist = re.search(r'applist="(.*?)"',line).group(1)
		except:
			applist = ''		

		#app
		try:
			app = re.search(r'app="(.*?)"',line).group(1)
		except:
			app = ''				

		#apprisk
		try:
			apprisk = re.search(r'apprisk="(.*?)"',line).group(1)
		except:
			apprisk = ''			
			
		#hostname
		try:
			hostname = re.search(r'hostname="(.*?)"',line).group(1)
		except:
			hostname = ''
			
		#incidentserialno
		try:
			incidentserialno = re.search(r'incidentserialno=(\S*?)\s',line).group(1)
		except:
			incidentserialno = ''	
			
		#url
		try:
			url = re.search(r'url="(.*?)"',line).group(1)
		except:
			url = ''

		#msg
		try:
			msg = re.search(r'msg="(.*?)"',line).group(1)
		except:
			msg = ''
			
			
		#scertcname
		try:
			scertcname = re.search(r'scertcname="(.*?)"',line).group(1)
		except:
			scertcname = ''	
			
			
		#eventtype
		try:
			eventtype = re.search(r'eventtype="(.*?)"',line).group(1)
		except:
			eventtype = ''	
			
		myList=[date,time,devname,devid,level,eventtime,type,subtype,vd,action,srcintfrole,srcintf,srcip,srcport,dstintfrole,dstintf,dstip,dstport,prototranslated,proto,service,direction,policyid,app,appid,appcat,apprisk,applist,logid,hostname,url,scertcname,incidentserialno,eventtype,sessionid,msg]
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
		

			print(myList)

		if (printLines > 0): print(csvString)
		#utmGZ.write(csvString.encode()+"\n".encode())
		utmGZ.write(csvString + "\n")
	
	
trafficGZ.close()	
utmGZ.close()
print("END")

#example for groups
#email_address = 'Please contact us at: support@datacamp.com'
#match = re.search(r'([\w\.-]+)@([\w\.-]+)', email_address)
#if match:
#  print(match.group()) # The whole matched text
#  print(match.group(1)) # The username (group 1)
#  print(match.group(2)) # The host (group 2)