#!/usr/bin/python
from conf.settings import *
import hashlib

class checker:
    """Check to see if DB is all ready Created if its not then creat it."""
    def __init__(self, dbfolder, dblog, dbmain):
        self.dbfolder = dbfolder
        self.dblog = dblog                   
        self.dbmain = dbmain
        chck = os.path.isdir(dbfolder)
        if chck == True:
            pass                                        
        elif chck != True: 
            os.mkdir(dbfolder)
        chck2 = os.path.isfile(dblog)
       	if chck2 == True:
       	    pass                                            
        elif chck2 != True:
       	    
       	    dbfle=open(dblog , 'a+b')
       	    dbfle.close()
       	    
        chck3 = os.path.isfile(dbmain)
        if chck3 == True:
            pass                                              
        elif chck3 != True:
            
            dbfl=open(dbmain , 'a+b')
            for line in monfiles:
                
                hsfi=os.stat(line).st_mtime
                hsfii=os.stat(line).st_atime
                hash1=hashlib.sha512(str(hsfi)).hexdigest()
                hash2=hashlib.sha512(str(hsfii)).hexdigest()
                dbfl.write(str(line)+':' + str(hash1) + '\n')
                dbfl.write(str(line)+':' + str(hash2) + '\n')
            for line in monfolders:
                
                hsme=os.stat(line).st_mtime
                hsmee=os.stat(line).st_atime
                hash3=hashlib.sha512(str(hsme)).hexdigest()
                hash4=hashlib.sha512(str(hsmee)).hexdigest()
                dbfl.write(str(line) + ':' + str(hash3) + '\n')
                dbfl.write(str(line) + ':' + str(hash4) + '\n')
            dbfl.close()
            time.sleep(0.5)
class fly:
    def __init__(self, monfiles, monfolders):
        self.monfiles = monfiles
        self.monfolders = monfolders
        qw=open(dbmain, 'rb')
        ddd=qw.readlines()
        for line in monfiles:
            cr=os.stat(line).st_mtime
            crr=os.stat(line).st_atime
            da=hashlib.sha512(str(cr)).hexdigest()
            daa=hashlib.sha512(str(crr)).hexdigest()
            x=str(line) + ':' + str(da) + '\n'
            xx=str(line) + ':' + str(daa) + '\n'
            if x in ddd[:]:
                pass
            elif x not in ddd[:]:
                dateNN=str(datetime.datetime.now())
                dateNNw='\n'+dateNN+'\n\n'
                email(emailfrm, emailto, header+subjct+dateNNw+' ::Files Modified Access Time Hash:: '+str(x)+emsg)
            if xx in ddd[:]:
                pass
            elif xx not in ddd[:]:
                dateNN=str(datetime.datetime.now())
                dateNNw='\n'+dateNN+'\n\n'
                email(emailfrm, emailto, header+subjct+dateNNw+' ::Files Last Access Time Hash:: '+str(xx)+emsg)
        for line in monfolders:
            crn=os.stat(line).st_mtime
            crnn=os.stat(line).st_atime
            da1=hashlib.sha512(str(crn)).hexdigest()
            da2=hashlib.sha512(str(crnn)).hexdigest()
            c=str(line) + ':' + str(da1) + '\n'
            cc=str(line) + ':' + str(da2) + '\n'
            if c in ddd[:]:
                pass
            elif c not in ddd[:]:
                
                dateN=str(datetime.datetime.now())
                dateNw='\n'+dateN+'\n\n'
                email(emailfrm, emailto, header+subjct+dateNw+' ::Folders Modified Access Time Hash:: '+str(c)+emsg)
            if cc in ddd[:]:
                pass
            elif cc not in ddd[:]:
                dateN=str(datetime.datetime.now())
                dateNw='\n'+dateN+'\n\n'
                email(emailfrm, emailto, header+subjct+dateNw+' ::Folders Last Access Time Hash:: '+str(cc)+emsg)

class email:
    def __init__(self, emailfrm, emailto, emsg):
        self.emailfrm = emailfrm
        self.emailto = emailto
        self.emsg = emsg
        server = smtplib.SMTP(gmail)
        server.starttls()
        server.login(username, passwd)
        server.sendmail(emailfrm, emailto, emsg)
        server.quit()
        

def main():
    try:
        checker(dbfolder, dblog, dbmain)
        while 1:  
            fly(monfiles, monfolders)
            time.sleep(TIME_TO_CHECK)
    except KeyboardInterrupt:
        sys.exit()
if __name__ == '__main__':
    main()
