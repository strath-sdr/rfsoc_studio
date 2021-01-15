import os
import xrfclk

import pynq
import pynq.lib

# import rfstrath

__author__ = "David Northcote"
__organisation__ = "The University of Strathclyde"

class RFStrathOverlay(pynq.Overlay):
    """RF Strath overlay for the board.

    The RF Strath overlay description goes here.

    """
    def __init__(self, *args, **kwargs):
        """Initialise the RF Strath overlay.

        """
        super.()__init__(*args, **kwargs)
        if self.is_loaded():
            pass

        self.i2c_initialised = False
        self.rfclks_initialised = False

    def init_i2c(self):
        """Initialize the I2C control drivers on RFSoC2x2.
        This should happen after a bitstream is loaded since I2C reset
        is connected to PL pins. The I2C-related drivers are made loadable
        modules so they can be removed or inserted.

        """
        module_list = ['i2c_dev', 'i2c_mux_pca954x', 'i2c_mux']
        for module in module_list:
            cmd = "if lsmod | grep {0}; then rmmod {0}; fi".format(module)
            ret = os.system(cmd)
            if ret:
                raise RuntimeError(
                    'Removing kernel module {} failed.'.format(module))

        module_list.reverse()
        for module in module_list:
            cmd = "modprobe {}".format(module)
            ret = os.system(cmd)
            if ret:
                raise RuntimeError(
                    'Inserting kernel module {} failed.'.format(module))

    def init_rf_clks(self, lmk_freq=122.88, lmx_freq=409.6):
        """Initialise the LMK and LMX clocks for the radio hierarchy.
        
        """
        if not self.rfclks_initialised:
            if not self.i2c_initialised:
                self.init_i2c()
            xrfclk.set_ref_clks(lmk_freq=lmk_freq, lmx_freq=lmx_freq)
            self.rfclks_initialised = True