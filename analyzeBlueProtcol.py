#-*- utf-8 --*-
import sys
import struct
import os
import string
import array


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
        self.HEX_Show()
        
        self.HCI_print()


    def HCIEvent_Init(self):
        self.EventCode = self.str[0]
        self.Length = self.str[1]
        self.param[0:] = self.str[2:]
        
    def HEX_Show(self):
        for num in self.str:
            print '0x%02x'%(num) ,

    def HCI_print(self):
        print '\n#- F -| %d'%(self.EventCode),
        print '#- Len: %d'%(self.Length),
        print '#- param: ' , self.param,
        print '\n\n'

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
            # length = file_content[curent_num + 3]  +  file_content[curent_num + 4] << 8

            length = file_content[curent_num + 3]
            print "H:%d L:%d"%(file_content[curent_num + 3], file_content[curent_num + 4] << 8) 
            print "curent: %d  length: %d"%(curent_num, length)

            temp_num = file_content[curent_num:curent_num + length + 4]
            for num in temp_num:
                print "0x%02x"%(num),
            
            curent_num += length + 4 
            # print 'curent: %d'%(curent_num)

        elif (file_content[curent_num] == 0x03):
            length = file_content[curent_num + 4];
            curent_num += length
            
        elif (file_content[curent_num] == 0x04):
            length = file_content[curent_num + 2] 
           
            temp_num = file_content[curent_num:curent_num+length + 3]
            curent_num += length + 3
            print "No: %d ### "%(cmd_no) , 
            cmd_no += 1
            
            HCI_Event(temp_num)
            
        else:
            return False
        
    return True 
            
if __name__ == "__main__":
    filename = sys.argv[1]
    print filename
    if(Analyze(filename) == False ):
        print "\nAnalyze Failed ..... \n"
    else:
        print "\nAnalyze Success ...... \n"

    
