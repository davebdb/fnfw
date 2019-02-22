#!/usr/bin/env python3

# IMPORTS
import os
import datetime
import sys
import re
#import time

if __name__ == '__main__':
	# get time in YYYYMMDDHH format
	args = sys.argv
	if (len(args) < 3):
		print("Usage:",args[0]," PATH_TO_LOG PATH_TO_GZ_DIRECTORY")
		exit()	
	parseToGZpath = "/home/programs/fnfw/parseToCSV-GZ.py"
	logDir = str(args[1])
	gzDir = str(args[2])
	currentDT = datetime.datetime.now().strftime("%Y%m%d%H")
	#print(currentDT, logDir, gzDir)
	logList = os.listdir(path=logDir)
	#print(logList)
	for logFile in logList:
#		if (re.search(currentDT,logFile)): print("GOTCHA")
		if (re.search(currentDT,logFile)): continue
		zipTimeStart = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
		print("Start",zipTimeStart)
		logPath = logDir+logFile
		print(logPath)
		commandToRun = parseToGZpath + " " + logPath + " " + gzDir
#		time.sleep(1)
		print(commandToRun)
		os.system(commandToRun)
		os.unlink(logPath)
		zipTimeEnd = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
		print("End",zipTimeEnd)
		

