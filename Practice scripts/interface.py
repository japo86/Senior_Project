#!/usr/bin/python3
from tkinter import *
from Attacks_script import *

root = Tk()
frame = Frame(root)
frame.pack(side =TOP)
frame.pack()

#works fine
title_text = Label(frame, text="Welcome to the DoS Stress Tester Ultra", padx=5, pady=5)
title_text.pack(padx=10, pady=10)

#All Modules
topframe = Frame(root, bd=5)
topframe.pack(side = TOP)

middleframe0 = Frame(root)
middleframe0.pack()

middleframe1 = Frame(root)
middleframe1.pack()

middleframe2 = Frame(root)
middleframe2.pack()

bottomframe = Frame(root, bd=5)
bottomframe.pack( side = BOTTOM )


#Retieve target IP address
target_var = StringVar()
target =" default value"

target_ip_label=Label( topframe, text="Please Enter Target IP:")
target_ip_label.pack(side= LEFT)

target_ip = Entry(topframe, textvariable=target_var )
target_ip.pack(side= LEFT)

#target_var.get()

# def get_target():
    
#     print(target) 

# collect= Button(topframe, text="Submit", width=5, command = get_target)
# collect.pack(side=RIGHT)

#call scan function in attacks_script
def run_scan():
    target = target_var.get()
    port_scan(target)
    print("run scan " + target)

perform_scan=Button(middleframe0, text="Perform Port Scan", command= run_scan)
perform_scan.pack(side = LEFT)


#attack type buttons

ICMP_flood = Checkbutton(middleframe1, text="IMCP Flood", fg="black")
ICMP_flood.pack( side = LEFT)

syn_flood = Checkbutton(middleframe1, text="SYN Flood", fg="black")
syn_flood.pack( side = LEFT )

shrew_attack = Checkbutton(middleframe1, text="Shrew Attack", fg="black")
shrew_attack.pack( side = LEFT )

P_O_D = Checkbutton(middleframe1, text="Ping Of Death", fg="black")
P_O_D.pack( side = LEFT )

teardrop_attack = Checkbutton(middleframe2, text="Tear Drop", fg="black")
teardrop_attack.pack( side = LEFT )



root.mainloop()