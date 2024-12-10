#!/usr/bin/env python
## we print same output as previous but in tables usinf 'verbose'


from asyncio import timeout
import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)   ### requests for the ip over the network " who has this ? "
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  #### broadcasts it over the network
                      ### replaces ff:ff:... with a specifc mac address to send the request
                        # to a particular device and not entire network
    ## scapy.ls(scapy.Ether())
    ## print(broadcast.summary()

    ##  now we combine both into one packet( request+ broadcast)

    arp_request_broadcast = broadcast/arp_request


    ##print(arp_request_broadcast.summary())
    ###arp_request_broadcast.show()

    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=4,verbose=False) ##send over netwokr and recieve response
    ### it receivees 2 packets so we stored it in 2 variables
    # timeout =1 , wait only  1 sec for response , if didnt receive move on ,else will bes  tuck in infinite looop

    ####we added "verbose = flase " to remove addtional info and just print imporatnt ie ip and mac


    print("IP\t\t\tMAC Address\n_______________________________________")
    client_list =[]
    for element in answered_list:
        ##print(element)  ##to display everything
        ##print(element[0].show())   ## to display details
        print(element[0].psrc +"\t\t"+ element[0].hwsrc)


        ###The answered_list contains tuples of two elements: the request packet (element[0]) and the response packet (element[1]).
         ####The IP (psrc) and MAC (hwsrc) addresses of the response come from element[1] (the response packet), not element[0].



scan("192.168.29.1/24")

###we need to make sure the request is sent to all
##devices over the network so we use ethernet framework

##summary:

