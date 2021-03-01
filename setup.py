import os
import shutil
from distutils.dir_util import copy_tree

from setuptools import find_packages, setup

# global variables
board = os.environ['BOARD']
nb_dir = os.environ['PYNQ_JUPYTER_NOTEBOOKS']
package_name = 'rfsoc_studio'
pip_name = 'rfsoc-studio'

data_files = []

# check whether board is supported
def check_env():
    if board not in ['RFSoC2x2', 'ZCU111']:
        raise ValueError("Board {} is not supported.".format(board))

check_env()

setup(
    name=package_name,
    version='0.1.0',
    install_requires=[
        'plotly==4.5.2',
        'pynq==2.6',
        'rfsoc-sam @ git+https://github.com/strath-sdr/rfsoc_sam@v0.2.2',
        'rfsoc-freqplan @ git+https://github.com/strath-sdr/rfsoc_frequency_planner@v0.1.0',
        'rfsoc-ofdm @ git+https://github.com/strath-sdr/rfsoc_ofdm@v0.2.0',
        'rfsoc-qpsk @ git+https://github.com/strath-sdr/rfsoc_qpsk@v1.3.0',
        'rfsoc-radio @ git+https://github.com/strath-sdr/rfsoc_radio@v0.1.0',
        'pynq-agc @ https://github.com/strath-sdr/pynq_agc/releases/download/v0.3/pynq_agc.tar.gz',
        'pystrath-dsp @ git+https://github.com/strath-sdr/dsp_notebooks@v0.1.0',
        'pystrath-rfsoc @ git+https://github.com/strath-sdr/rfsoc_notebooks@v0.1.0'
    ],
    author="David Northcote",
    packages=find_packages(),
    package_data={
        '': data_files,
    },
    description="University of Strathclyde RFSoC Studio.")
