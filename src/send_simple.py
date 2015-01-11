import array
from ola.ClientWrapper import ClientWrapper

def DmxSent(state):
    wrapper.Stop()

universe = 1
data = array.array('B')
data.append(233)
data.append(11)
data.append(241)
wrapper = ClientWrapper()
client = wrapper.Client()
client.SendDmx(universe, data, DmxSent)
wrapper.Run()
