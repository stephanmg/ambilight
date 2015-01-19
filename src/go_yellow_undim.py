#!/usr/bin/env python
# -*- coding: utf-8 -*-
## author: stephan 
## date: 30th of December 2014

# necessary imports for OLA on RPI
import array
from ola.ClientWrapper import ClientWrapper
import datetime
import time

# number of LEDs we have in the string
NUM_PIXELS =  50

# color for all LEDs
RED        = 0
GREEN      = 0
BLUE       = 0

# timestep width (in seconds [s])
TIMESTEP = 1

# dim?
bDimming = True

# send and stop the DMX send process
def DmxSent(state):
  wrapper.Stop()

# which LED string? we only have 1 WS2801 
universe = 1

# increment
INCREMENT = 1

while bDimming:
  # sleep for timestep
  time.sleep(TIMESTEP)

  # dim color value
  GREEN = GREEN + INCREMENT
  RED = RED + INCREMENT 

  if (GREEN > 250 and RED > 250): 
    bDimming = False
    continue

  # populate data array
  data = array.array('B')
  for i in range(0, NUM_PIXELS):
     data.append(RED)
     data.append(GREEN)
     data.append(BLUE)

  # send constant DMX code and quit
  wrapper = ClientWrapper()
  client = wrapper.Client()
  client.SendDmx(universe, data, DmxSent)
  wrapper.Run()

