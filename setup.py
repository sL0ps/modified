#!/usr/bin/python
import os, time
ck=os.path.isdir('/opt/modified')
if ck == True:
    os.system('rm -rf /opt/modified')
elif ck != True:
    os.mkdir('/opt/modified/')
    time.sleep(1)
    crdir=os.getcwd()
    os.system('cp -R '+str(crdir)+' /opt/')
    time.sleep(1)
    os.system('/bin/rm /opt/modified/setup.py')
    time.sleep(1)
    os.system('/bin/cp /opt/modified/modified /etc/init.d/')
    time.sleep(1)
    os.system('/bin/rm /opt/modified/modified')
print "Files installed to /opt/modified"
print "Run: /etc/init.d/modified start|status|stop|restart"

