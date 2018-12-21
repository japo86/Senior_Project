#!/usr/bin/python3
from queue import *

import threading
from scapy.all import *

print_lock = threading.Lock()
q = Queue()
ip_list = []


def scanner(dst_ip, sport_num, dport_num):
    print("#####################################################################################################")

    p = IP(src=RandIP(), dst=dst_ip) / TCP(sport=sport_num, dport=dport_num, flags="S") / ""

    try:
        with print_lock:
            send(p)
            print("loop done???????????????????????????????????????????????????")
    except:
        pass


def threader():
    while True:
        # gets an worker from the queue
        worker = q.get()
        # Run the example job with the avail worker in queue (thread)
        scanner("192.168.5.155", worker, 80)
        # completed with the job
        q.task_done()
        print('threader')


for x in range(10):
    t = threading.Thread(target=threader)

    t.daemon = True  # classifying as a daemon, so they will die when the main dies

    t.start()  # begins, must come after daemon definition


def main():
    port_range_bottom = 1022
    port_range_top = 65535
    # scanner('192.168.0.210', 1, 32405)
    for worker in range(port_range_bottom, port_range_top):
        q.put(worker)
    # wait until the thread terminates.
    q.join()

    for i in ip_list:
        print(i)


if __name__ == "__main__":
    main()

    # pkt=sr1(IP(dst='192.168.0.5')/TCP(sport=44433, dport=80, flags='S'))
