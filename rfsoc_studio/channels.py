__author__ = "David Northcote"
__organisation__ = "The Univeristy of Strathclyde"
__support__ = "https://github.com/strath-sdr/rfsoc_studio"

from pynq import DefaultHierarchy
from pynq import allocate
from .receiver import AxisPacketGenerator
from .transmitter import AxisController


class AdcChannel(DefaultHierarchy):

    @staticmethod
    def checkhierarchy(description):
        return ('axis_packet_generator' in description['ip'] and
        'axi_dma_real' in description['ip'] and
        'axi_dma_imag' in description['ip'] and
        description['fullpath'].split('/')[-2] == 'receiver')    
    
    def __init__(self, description, tile=None, block=None):
        super().__init__(description)
        self._tile = tile
        self._block = block

    def transfer(self, packet_size):
        size = int(np.ceil(packet_size/8))
        self.axis_packet_generator = size
        real_buffer = allocate(shape=(size*8,), dtype=np.int16)
        imag_buffer = allocate(shape=(size*8,), dtype=np.int16)
        self.axi_dma_real.recvchannel.transfer(real_buffer)
        self.axi_dma_imag.recvchannel.transfer(imag_buffer)
        self.axis_packet_generator.transfer = 1
        self.axi_dma_real.recvchannel.wait()
        self.axi_dma_imag.recvchannel.wait()
        self.axis_packet_generator.transfer = 0
        real_data = np.array(real_buffer)
        imag_data = np.array(imag_buffer)
        real_buffer.freebuffer()
        imag_buffer.freebuffer()
        c_data = (real_data.astype('single') + 1j * imag_data.astype('single')) * 2**-15
        return c_data[0:packet_size]

    def _initialise_channel(self):
        pass
        
class DacChannel(DefaultHierarchy):
    
    @staticmethod
    def checkhierarchy(description):
        controller = None
                
        for ip, details in description['ip'].items():
            if details['driver'] == AxisController:
                controller = ip
                
        return (controller is not None)
    
    
    def __init__(self, description, tile=None, block=None):
        super().__init__(description)
        self._tile = tile
        self._block = block

    def _initialise_channel(self):
        pass