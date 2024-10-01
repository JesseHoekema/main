import random
import time
import main

state = online.main, offline.main
online.main = False

def getstate():
  online = main.getfilestate(online.main)
  offline = main.getfilestate(offline.main)
  if online = True:
    online.main = True
  else: 
    online.main = False

def online():
  print("Online On Discord")

def offline():
  print("Offline On Discord")

if online.main = True:
  online()
else:
  offline()

print("Getting State Of User")
getstate()
  
