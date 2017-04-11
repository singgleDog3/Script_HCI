#-*- utf-8 --*-
import sys
import struct
import os
import string
import array
from HCI_cmdevent import *


# HCI command format
# op_code(2 octets) + length(1 octets) + param

# HCI ACL data packet
# Handle(12 bits) + PB FLAG(2 bits) + BC flag(2 bits) + length (2 octets) + data

# HCI synchronous data packets
# conn_handle(12 bits) + packetStatusFlag(2 bits) + reserved(2 bits) + length(1 octets)+ data

# HCI event packet
# event_code(1 octets) + length(1 octets) + param 

class HCI_Command:
    def __init__(self, str = []):
        self.hci_flag = []
        self.ocf      = []
        self.ogf      = []
        self.length   = []
        self.param    = []
        self.str = str[0:]
        self.HCICMD_init()
        
        
    def HCICMD_init(self):
        self.hci_flag = self.str[0]
        self.ocf      = (self.str[1] & 0xc0 ) << 8 | ((self.str[1] << 2 ) | self.str[2] >> 6)
        self.ogf      = self.str[2] & 0x3f
        self.length   = self.str[3]
        self.param[0:]   = self.str[4:]
        
        
    def HEX_print(self):
        for ch in self.str:
            print hex(ch),
        
    def  HCI_print(self):
        self.HEX_print()
        print "\n|- flag # %02x"%(self.hci_flag),
        print "|- ocf # %03x"%(self.ocf),
        print "|- ogf # %02x"%(self.ogf),
        print "|- len # %d"%(self.length),
        print "|- param # ",self.param 
        print "\n\n"
        
class HCI_Event:
    def __init__(self, str = []):
        self.str = str[0:]
        self.EventCode = []
        self.Length    = []
        self.param     = []
        
        self.HCIEvent_Init()
        self.HCIEvent_print()
    
    def HCIEvent_Init(self):
        pass
        
        
    def HCI_print(self):
        print "HCIEvent "

def Analyze(filename):
    file_ops = open(filename, 'ab+')
    file_size =  os.path.getsize(filename)
    file_content = file_ops.read(file_size)
    file_content = map(lambda x:ord(x) , file_content)
    temp_num = []
    curent_num  = 0
    
    cmd_no = 0

    while(curent_num < file_size):
        if(file_content[curent_num] == 0x01):
            length = file_content[curent_num + 3]
            temp_num = file_content[curent_num:curent_num+length+4]
            cmd = HCI_Command(temp_num)
            print "No: %d "%(cmd_no) ,
            cmd.HCI_print()
            
            curent_num += length + 4
            cmd_no += 1
            
        elif (file_content[curent_num] == 0x02):
            length = file_content[curent_num + 4] <<8 +  file_content[curent_num + 5]
            curent_num += length
            
        elif (file_content[curent_num] == 0x03):
            length = file_content[curent_num + 4];
            curent_num += length
            
        elif (file_content[curent_num] == 0x04):
            length = file_content[curent_num + 2] 
            curent_num += length
            temp_num = file_content[curent_num:curent_num+length+4]
            HCI_Event(temp_num)
            
        else:
            return False
        
    return False
            
if __name__ == "__main__":
    filename = sys.argv[1]
    print filename
    Analyze(filename)

    
