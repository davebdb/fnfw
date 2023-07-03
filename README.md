Creating a parsing program to parse a logfile from a fortigate FW into a CSV file.
Steps also to complate, GZIP the content.

For automated parsing and zipping use the gzPreviousHours.py program.  It takes 2 arguments.  logDir gzDir
logPath is where the logs originate from
gzPath is where the gzip files will be created

gzPreviousHours.py LOG_DIR GZ_DIR

this will run this command against all hours that are not equal to the current hour when executed in the LOG_DIRECTORY. 

Standard output application
parseToCSV-stdout.py logPath searchType
searchType may be of values: traffic utm event

