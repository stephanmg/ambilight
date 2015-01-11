#!/usr/bin/env python

import array
from ola.ClientWrapper import ClientWrapper

def DmxSent(state):
  wrapper.Stop()

universe = 1
data = array.array('B')
for i in range(0, 50):
	data.append(21)
	data.append(132)
	data.append(123)

wrapper = ClientWrapper()
client = wrapper.Client()
client.SendDmx(universe, data, DmxSent)
wrapper.Run()
