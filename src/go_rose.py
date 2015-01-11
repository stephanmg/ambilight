#!/usr/bin/env python

import array
from ola.ClientWrapper import ClientWrapper

def DmxSent(state):
  wrapper.Stop()

universe = 1
data = array.array('B')
for i in range(0, 50):
	data.append(248)
	data.append(0)
	data.append(248)

wrapper = ClientWrapper()
client = wrapper.Client()
client.SendDmx(universe, data, DmxSent)
wrapper.Run()
