#!/usr/bin/python3
import nmap
import sys


class Port_Scan:

    def __init__(self, target, lower_port, upper_port):
        self.target = target
        self.port_range = lower_port + '-' + upper_port
        try:
            self.nm = nmap.PortScanner()         # instantiate nmap.PortScanner object
        except nmap.PortScannerError:
            print('Nmap not found', sys.exc_info()[0])
            sys.exit(1)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            sys.exit(1)

    def scanner(self):
        self.nm.scan(self.target, self.port_range)

    def print_results(self) -> object:
        for host in self.nm.all_hosts():
            print('----------------------------------------------------')
            print('Host : %s (%s)' % (host, self.nm[host].hostname()))
            print('State : %s' % self.nm[host].state())
            for proto in self.nm[host].all_protocols():
                print('----------')
                print('Protocol : %s' % proto)

                lport = self.nm[host][proto].keys()
                # lport.sorted()
                for port in lport:
                    print('port : %s\tState: %s\t Service: %s\t Version: %s %s'
                           % (port, self.nm[host][proto][port]['state'],
                              self.nm[host][proto][port]['product'],
                              self.nm[host][proto][port]['version'],
                              self.nm[host][proto][port]['name']))
