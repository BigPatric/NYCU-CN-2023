from scapy.config import conf
conf.ipv6_enabled = False
from scapy.all import *
import sys

# get path of pcap file
INPUTPATH_TCP_h3 = sys.argv[1]
INPUTPATH_TCP_h4 = sys.argv[2]
INPUTPATH_UDP_h3 = sys.argv[3]
INPUTPATH_UDP_h4 = sys.argv[4]
# read pcap
packets_TCP_h3 = rdpcap(INPUTPATH_TCP_h3)
packets_TCP_h4 = rdpcap(INPUTPATH_TCP_h4)
packets_UDP_h3 = rdpcap(INPUTPATH_UDP_h3)
packets_UDP_h4 = rdpcap(INPUTPATH_UDP_h4)
#start_time = packets[0].time
#end_time = packets[-1].time

total_TCP_h3_1 = 0
total_TCP_h3_2 = 0
for packet in packets_TCP_h3[TCP]:
    if packet[0][2].dport==8889 or packet[0][2].sport==8889:
        total_TCP_h3_1+=len(packet)
    elif packet[0][2].dport==7777 or packet[0][2].sport==7777:
        total_TCP_h3_2+=len(packet)
total_TCP_h3_1*=8
total_TCP_h3_2*=8
time_TCP_h3=packets_TCP_h3[TCP][-1].time-packets_TCP_h3[TCP][0].time
## different TCP flow but spend same time

total_TCP_h4 = 0
for packet in packets_TCP_h4[TCP]:
    if packet[0][2].dport==7777 or packet[0][2].sport==7777:
        total_TCP_h4 += len(packet)
total_TCP_h4*=8
time_TCP_h4=packets_TCP_h4[TCP][-1].time-packets_TCP_h4[TCP][0].time


total_UDP_h3_1 = 0
total_UDP_h3_2 = 0
for packet in packets_UDP_h3[UDP]:
    if packet[0][2].dport==8889 or packet[0][2].sport==8889:
        total_UDP_h3_1+=len(packet)
    elif packet[0][2].dport==7777 or packet[0][2].sport==7777:
        total_UDP_h3_2+=len(packet)
total_UDP_h3_1 *=8
total_UDP_h3_2 *=8
time_UDP_h3=packets_UDP_h3[UDP][-1].time-packets_UDP_h3[UDP][0].time

# UDP_h4 will have other (e.g)MDNS
#=>wrong answer
# count how many udp
allP = 0
for packet in packets_UDP_h4[UDP]:
    allP+=1
## MDNS is form back
## counting from back, when we find first UDP(the last time spot)
end = 0
for i in range(allP-1,0,-1):
    if packets_UDP_h4[UDP][i].dport == 7777 or packets_UDP_h4[UDP][i].sport == 7777:
        end = i
        break
    
total_UDP_h4 = 0
for packet in packets_UDP_h4[UDP]:
    total_UDP_h4 += len(packet)
total_UDP_h4 *=8
time_UDP_h4=packets_UDP_h4[UDP][end].time-packets_UDP_h4[UDP][0].time

        
print("--- TCP ---")
print(f"Flow1(h1->h3):{(total_TCP_h3_1/time_TCP_h3)/1000000}       Mbps")#8889
print(f"Flow2(h1->h3):{(total_TCP_h3_2/time_TCP_h3)/1000000}       Mbps")#7777
print(f"Flow3(h2->h4):{(total_TCP_h4/time_TCP_h4)/1000000}       Mbps")#7777

print("--- UDP ---")
print(f"Flow1(h1->h3):{(total_UDP_h3_1/time_UDP_h3)/1000000}       Mbps")#8889
print(f"Flow2(h1->h3):{(total_UDP_h3_2/time_UDP_h3)/1000000}       Mbps")#7777
print(f"Flow3(h2->h4):{(total_UDP_h4/time_UDP_h4)/1000000}       Mbps")#7777

print("--- TIMES ---")
print(f"TCP_h3:{time_TCP_h3}")
print(f"TCP_h4:{time_TCP_h4}")
print(f"UDP_h3:{time_UDP_h3}")## only difference
print(f"UDP_h4:{time_UDP_h4}")