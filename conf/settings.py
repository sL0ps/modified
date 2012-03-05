#!/usr/bin/python
import os, re, sys, time, smtplib, datetime
from subprocess import Popen, PIPE
#Time in Seconds to wait till next Check
TIME_TO_CHECK = 60
####################################################
dbmain     = '/opt/modified/db/maindb.db'
dbfolder   = '/opt/modified/db/'
dblog     = '/opt/modified/db/logdb.db'
###################################################
#Files to monitor
monfiles   = ['/var/www/index.html', '/etc/shadow']
#Folders to monitor
monfolders = ['/var/www', '/var/log']

###########################

#Email To
emailto	   ='YOUREMAIL@SITE.com'
#your Email address (Gmail Only)
emailfrm   ='YOUREMAIL@gmail.com'
passwd     ='YOURPASSWORD'
#Gmail Username
username   ='YOUREMAIL_USERNAME'
gmail      ='smtp.gmail.com:587'
header     ='To:'+emailto+'\n'+'From:'+emailfrm+'\n'
subjct     ='Subject:File Integrity Monitor Alerted!\n'
emsg       ='\nFile Integrity Monitoring Alerted! Please Investigate!\n\n'
red        = '\033[31m'
green      = '\033[32m'
yellow     = '\033[33m'
blue 	   = '\033[34m'
end 	   = '\033[0m'

