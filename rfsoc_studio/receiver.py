__author__ = "David Northcote"
__organisation__ = "The Univeristy of Strathclyde"
__support__ = "https://github.com/strath-sdr/rfsoc_studio"

from pynq import DefaultIP
from pynq import allocate
import numpy as np


class AxisPacketGenerator(DefaultIP):
    
    def __init__(self, description):
        super().__init__(description)
        
    bindto = ['xilinx.com:ip:AxisPacketGenerator:1.0']
    
_packet_generator_props = [("packet_size",   0x100),
                           ("transfer",    0x104)]

def _create_mmio_property(addr):
    def _get(self):
        return self.read(addr)
    
    def _set(self, value):
        self.write(addr, value)
        
    return property(_get, _set)

for (name, addr) in _packet_generator_props:
    setattr(AxisPacketGenerator, name, _create_mmio_property(addr))