#!/usr/bin/env python

'''
Bugs: 
Routerda debug açık olursa onları da alıyor. 
* ile başlayan satırları sed ile fitrele
'''

from telnetlib import Telnet
import time
import subprocess
import sqlite3
import shutil
import os



routerPortList = {}

def writeConfigFilesToDB(newDB, pathToFolder,cfgText) :
    
    conn = sqlite3.connect(newDB)   
    cursor = conn.cursor()
    
    cursor.execute('''delete from configs''')
    
    from os import walk
    
    pathToFolder = '../outputFiles/' + pathToFolder
    for filename in next(walk(pathToFolder))[2] :
        if (filename[0] != '.' ) :
            port, fext  = filename.split('.')
            cfgid = int(port) - 2000 
            devicename = routerPortList[port]           
            f = open(pathToFolder + '/' + filename, 'r', encoding='utf-8')
            cfgconfig = f.read()
            cfgname = cfgText + ' - ' + devicename
            cursor.execute('''INSERT INTO configs(cfg_id, cfg_name, cfg_config)
                  VALUES(?,?,?)''', (cfgid,cfgname, cfgconfig))
    
    labname = cfgText
    labdescription = cfgText + ' Topology'
    
    cursor.execute('''UPDATE labs set lab_name = ?, lab_description = ? where lab_id = 1''', (labname,labdescription))
        
    conn.commit()
    
    conn.close()
        
    



def main():
    
    ''' sed -i".bak" -E '/#|>|Building|Last|Current|^\s*$|^$|^[[:space:]]*$/d' *.txt '''

    host = '192.168.72.101'
    port = 2001
    
    while (port < 2021): 
        tn = Telnet()
        tn.open(host, port, timeout=2)
        
        
        text = tn.read_very_eager()
        
        # tn.sock.sendall(IAC + WILL + ECHO)
        
        line = b"\r\nenable\r\nterminal length 0\r\n"
        tn.write(line)
        time.sleep(0.5)
        
        text = tn.read_very_eager()
        line = b"\r\nshow run\r\n"
        tn.write(line)
        time.sleep(3)
        text = tn.read_very_eager()
        
        with open('../outputFiles/' + str(port) + '.txt', 'w', encoding='utf_8') as f: 
            f.writelines(text.decode('utf_8'))
    
        
        for line in text.split(b"\r\n"):
            print(line)
        
        tn.close()
        port += 1
    
    # Remove unnecessary lines from configs
    subprocess.call(['sh', 'removeGarbage.sh'])
        

    routerPortList.update({ '2001':'P1'})
    routerPortList.update({ '2002':'P2'})
    routerPortList.update({ '2003':'P3'})
    routerPortList.update({ '2004':'P4'})
    routerPortList.update({ '2005':'PE1'})
    routerPortList.update({ '2006':'PE2'})
    routerPortList.update({ '2007':'PE3'})
    routerPortList.update({ '2008':'PE4'})
    routerPortList.update({ '2009':'RR1'})
    routerPortList.update({ '2010':'RR2'})
    routerPortList.update({ '2011':'CE11'})
    routerPortList.update({ '2012':'CE12'})
    routerPortList.update({ '2013':'CE21'})
    routerPortList.update({ '2014':'CE22'})
    routerPortList.update({ '2015':'CE31'})
    routerPortList.update({ '2016':'CE32'})
    routerPortList.update({ '2017':'CE41'})
    routerPortList.update({ '2018':'CE42'})
    routerPortList.update({ '2019':'HQ1'})
    routerPortList.update({ '2020':'HQ2'})



    

    
    baseDB ='../databases/iou-web-btegitim-MPLS.db'
    
   
    
    cfgText = 'MulticastDay2Final'
    cfgFolder = ''    
    newDB = '../databases/iou-web-btegitim-' + cfgText + '.db'
    
    
    shutil.copyfile(baseDB,newDB)
    
    writeConfigFilesToDB(newDB, cfgFolder, cfgText)
   
    
    os.system('rm ' + newDB + '.gz')
    os.system('gzip ' + newDB)

    

    
if __name__ == "__main__": main()

