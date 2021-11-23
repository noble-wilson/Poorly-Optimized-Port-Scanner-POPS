import sys
import socket
import validators
import pyfiglet
from datetime import datetime
from pyfiglet import Figlet

#To add a specific port, add it to light_list and select 1 for the intensity
light_list = [20, 21, 22, 25, 53, 80, 123, 179, 443, 500, 3389]

#This is the banner
custom_fig = Figlet(font='banner3')
print(custom_fig.renderText('POPS'))
print("-"*50)
print("Welcome to Poorly Optimized Port Scanner!")
print("REMEMBER THAT ACTIVE SCANNING SHOULD ONLY BE DONE WITH PERMISSION")
print("Please identify your target.")

target = input("I support IPv4 (8.8.8.8) and domain notation (google.com): ")

#This validates that the IP address or domain is a possible address
if validators.ip_address.ipv4(target):
  print("Target has been validated.")
elif validators.domain(target):
  print("Target has been validated.")
else:
  print("nope")
  sys.exit("Host connection couldn't be established.")

print("Please decide what level of scan intensity you want.")
print("Level 1 is very light scan that can evade detection, while ")
print("Level 3 is a strong scan that is very noticeable.")
print("Level 2 is a middle ground, but is still quite obvious.")

intensity = int(input("1, 2, or 3: "))

#Begins scans based upon what insensity is selected
if intensity == 1:
  print("-" * 50)
  print("Scanning Target: " + target)
  print("Scanning started at: " + str(datetime.now()))
  print("-" * 50)
  print("This could take a minute, why not enjoy a break")
  for port in light_list:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target,port))
    if result == 0:
      print("Port {} is open".format(port))
      print("Scan Complete and Connection Terminated")
      s.close()
elif intensity == 2:
  print("-" * 50)
  print("Scanning Target: " + target)
  print("Scanning started at: " + str(datetime.now()))
  print("-" * 50)
  print("This could take a minute, why not enjoy a break")
  for port in range(1,500):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target,port))
    if result == 0:
      print("Port {} is open".format(port))
      print("Scan Complete and Connection Terminated")
      s.close()
elif intensity == 3:
  print("-" * 50)
  print("Scanning Target: " + target)
  print("Scanning started at: " + str(datetime.now()))
  print("-" * 50)
  print("This could take a minute, why not enjoy a break")
  for port in range(1,1023):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target,port))
    if result == 0:
      print("Port {} is open".format(port))
      print("Scan Complete and Connection Terminated")
      s.close()
else:
  print("Program failed due to unrecognized intensity level.")
  sys.exit()