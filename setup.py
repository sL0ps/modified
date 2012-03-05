#!/usr/bin/python
import os, time

os.mkdir('/opt/modified/')
time.sleep(1)
os.system('/bin/cp -R ../modified /opt/')
time.sleep(1)
os.system('/bin/rm /opt/modified/setup.py')
time.sleep(1)
os.system('/bin/cp /opt/modified/modified /etc/init.d/')
time.sleep(1)
os.system('/bin/rm /opt/modified/modified')
print "Files installed to /opt/modified"
print "Run: /etc/init.d/modified start|status|stop|restart"

