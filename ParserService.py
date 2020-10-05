import signal
import os
import time
import json
import socket
import sys
UDP_IP = "localhost"
UDP_PORT = 10000
File = "config.txt"

#Control de senales

def signal_handler(signum,stack):
    print("Recived_signal:",signum,"stack",stack)
    exit(0)
    

#Parser

class Parser:
    
    # constructor 
    def __init__(self,namefile=File):
        self.namefile=namefile
    
    # apertura y lectura de datos de archivo txt
    def open_and_read_file_txt(self):
        with open(self.namefile,'r') as f:
            read_line_file_txt= f.readline()
        return read_line_file_txt
            
    # apertura y lectura de datos ade archivo csv
    def open_and_read_file_csv(self,read_file_csv):
        with open(read_file_csv,'r') as f:
            index_read_line_file_csv=next(f)
            read_line_file_csv=f.readlines()
            return read_line_file_csv
    # manejo de datos en formato json
    def json_parser(self,datalist):
        auxlist=[]
        
        for x in datalist:
            data_format=x.split(",")
            dic={"id":int(data_format[0]),"name":str(data_format[1]),"value1":float(data_format[2]),"value2":float(data_format[3])}
            print(dic)
            auxlist.append(dic)
        json_format = json.dumps(auxlist)
        return json_format
    
    
    # manejador de senales 
signal.signal(signal.SIGINT,signal_handler)
    
    
    #creacion de socket 
s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
def main():
    parser=Parser()
    path = parser.open_and_read_file_txt()
    path = path.rstrip("\n")
    while(True):
        datalist = parser.open_and_read_file_csv(path)
        parseo= parser.json_parser(datalist)
        s.sendto(parseo.encode(),(UDP_IP,UDP_PORT))
        shipping_time=30
        time.sleep(shipping_time)
            
            
main()
