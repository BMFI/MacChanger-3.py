#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m","--mac", dest="new_mac", help="new MAC address")

parser.parse_args()

interface = input(" interface > ")
new_mac = input(" new Mac >")

print("[+] Changing Mac address for " + interface + " to " + new_mac)

# Less secure
#subprocess.call("ifconfig" + interface + "down", shell=True)
#subprocess.call("ifconfig" + interface + " hw ether " + new_mac, shell=True)
#subprocess.call("ifconfig" + interface + " up ", shell=True)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface,"hw", "ether", new_mac])
subprocess.call(["ifconfig", interface,"up"])