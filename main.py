import nmap_port_scanner
import Attacks_script
import multiprocessing
#


def do_icmp(tar, pls):
    i = Attacks_script.IcmpAttack(tar, pls)
    i.start_attack()


def do_scan(tar, lower, upper):
    #print("testing")
    tar = tar # "192.168.5.155"
    p = nmap_port_scanner.Port_Scan(tar, lower, upper)
    p.scanner()
    p.print_results()


def main():
    do_icmp("192.168.5.155", 1440)
    #do_scan("192.168.5.155", "0", "80")

if __name__ == "__main__":
    main()
