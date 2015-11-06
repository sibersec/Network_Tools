
from scapy.all import * 


print "-" * 50
print " This is an ArpScanner that you would find all of IP address consider of arp on network. "
print "-" * 50


b = raw_input("please insert network address as like 'x.x.x.x/x' \n")
	
print  "Network is %s"%b
ArpSend = srp1(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=b),timeout=1,inter=0.5,verbose=0)
if ArpSend:
	print "IP: " + ArpSend.psrc + " MAC : " + ArpSend.hwsrc 
