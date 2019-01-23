#!/usr/bin/env python3

import sys
import re

fileToRead=''
debug=0

#fwlog = open("/path/to/file/to/read","r")
args=sys.argv
fwlog = open(str(args[1]),"r")
if (debug>=3): print(str(args[1]))

for line in fwlog:
	y=line.rstrip('\r\n')
	if (debug>=1): print(y)
	#type
	try:
		type = re.search(r'type="(.*?)"',line).group(1)
	except:
		type = ''	
		
	if (type != 'traffic'): continue
	
	#date
	try:
#		date = re.search(r'date=(\d\d\d\d-\d\d-\d\d)',line).group(1)
		date = re.search(r'date=(\S*?)\s',line).group(1)
	except:
		date = ''
	
	
	#time
	try:
#		time = re.search(r'time=(\d\d:\d\d:\d\d)',line).group(1)
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
	
	
	#appcat
	try:
		appcat = re.search(r'appcat="(.*?)"',line).group(1)
	except:
		appcat = ''
	
	
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
		
	#policyname
	try:
		policyname = re.search(r'policyname=(\S*?)\s',line).group(1)
	except:
		policyname = ''
	
	myList=[date,time,devname,devid,level,eventtime,vd,type,subtype,action,srcintfrole,srcintf,srcip,srcport,srccountry,dstintfrole,dstintf,dstip,dstport,dstcountry,service,trandisp,transip,transport,tranip,tranport,policytype,policyid,policyname,logid,appcat,crscore,craction,crlevel,duration,sentbyte,rcvdbyte,sentpkt,]
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
		print('appcat:',appcat)
		print('crscore:',crscore)
		print('craction:',craction)
		print('crleve:',crlevel)
		print('tranip:',tranip)
		print('tranport:',tranport)
		print('transip:',transip)
		print('transport:',transport)
		print(myList)

	print(csvString)

	
	
print("END")

#example for groups
#email_address = 'Please contact us at: support@datacamp.com'
#match = re.search(r'([\w\.-]+)@([\w\.-]+)', email_address)
#if match:
#  print(match.group()) # The whole matched text
#  print(match.group(1)) # The username (group 1)
#  print(match.group(2)) # The host (group 2)