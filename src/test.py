import array
from ola.ClientWrapper import ClientWrapper

wrapper = None
loop_count = 0
TICK_INTERVAL = 0.00000000000000000000000000000000000000001  # in ms
TICK_INTERVAL = 25

def DmxSent(state):
  if not state.Succeeded():
    wrapper.Stop()

def SendDMXFrame():
  # schdule a function call in 100ms
  # we do this first in case the frame computation takes a long time.
  wrapper.AddEvent(TICK_INTERVAL, SendDMXFrame)

  # compute frame here
  data = array.array('B')
  global loop_count
  for i in range(0,50):
	data.append(233)
	data.append(11)
	data.append(241)
  loop_count += 1

  # send
  wrapper.Client().SendDmx(1, data, DmxSent)
                                                                                                                        

wrapper = ClientWrapper()
wrapper.AddEvent(TICK_INTERVAL, SendDMXFrame)
wrapper.Run()
