#!/usr/bin/env python3

# IMPORTS
import os
import datetime
import sys
import re

if __name__ == '__main__':
	# get time in YYYYMMDDHH format
	args = sys.argv
	if (len(args) < 3):
		print("Usage:",args[0]," PATH_TO_LOG PATH_TO_GZ_DIRECTORY")
		exit()	
	logDir = str(args[1])
	gzDir = str(args[2])
	currentDT = datetime.datetime.now().strftime("%Y%m%d%H")
	print(currentDT, logDir, gzDir)
	logList = os.listdir(path=logDir)
	print(logList)
	for logFile in logList:
		if (re.search(currentDT,logFile)): print("GOTCHA") 
#		if (re.search(currentDT,logFile)): continue
		logPath = logDir+logFile
		print(logPath)

