#!/usr/bin/python
# Open DMX -> WS2801, including backup/recorded playback
# Copyright (c) 2012 Jeffrey Nappi <jeff@jeffnappi.com>
#
# This work is licensed under the Creative Commons
# Attribution-NonCommercial-ShareAlike 3.0 Unported License.
# To view a copy of this license, visit 
# http://creativecommons.org/licenses/by-nc-sa/3.0/ or send
# a letter to Creative Commons, 444 Castro Street, Suite 900,
# Mountain View, California, 94041, USA.

import sys
import time
import random
import argparse
from ola.ClientWrapper import ClientWrapper

NUM_PIXELS = 50
PIXEL_SIZE = 1 
SPI_DEVICE = "/dev/spidev0.0";
BACKUP_FILE = "save.out"
GAMMA = bytearray(500)
for i in range(256): GAMMA[i] = int(pow(float(i) / 255.0, 2.5) * 255.0)

def Display(data):
  spidev.flush()
  pixel_values = bytearray(NUM_PIXELS * PIXEL_SIZE)
  for i in xrange(0,NUM_PIXELS * PIXEL_SIZE):
    pixel_values[i] = GAMMA[data[i]]
  spidev.write(pixel_values)

def Receive(data):
  global time_last
  time_last = time.time()

  if backup_mode:
    if sum(data) == 0:
      print "Done saving."
      quit()
    backup.write(data[:NUM_PIXELS * PIXEL_SIZE])

  if sum(data) == 0:
    Display(GetBackup())
  else:
    Display(data)

def GetBackup():
  global backup_pos
  backup_pos += NUM_PIXELS * PIXEL_SIZE
  if backup_pos + NUM_PIXELS * PIXEL_SIZE >= backup_end: backup_pos = 0
  return backup_data[backup_pos:backup_pos + NUM_PIXELS * PIXEL_SIZE]

# check to see if we are receiving data. if not play backup
def CheckAlive():
  global time_last, wrapper
  if time.time() - time_last > 5:
    empty_pixels = bytearray(NUM_PIXELS * PIXEL_SIZE)
    Display(GetBackup())
    wrapper.AddEvent(10, CheckAlive)
  else:
    wrapper.AddEvent(1000, CheckAlive)


backup_mode = True if len(sys.argv) > 1 and sys.argv[1] == "-b" else False

time_last = time.time()

if backup_mode:
  backup = open(BACKUP_FILE,'wb')
  backup_data = bytearray()
else:
  backup = open(BACKUP_FILE,'r')
  backup_data = bytearray(backup.read())

backup_pos = 0
backup_end = len(backup_data)

spidev = file(SPI_DEVICE, "wb")
universe = 1
wrapper = ClientWrapper()
client = wrapper.Client()
client.RegisterUniverse(universe, client.REGISTER, Receive)
if not backup_mode: wrapper.AddEvent(1000, CheckAlive)
wrapper.Run()
