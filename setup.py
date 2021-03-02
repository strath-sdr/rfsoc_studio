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

# copy notebooks into jupyter home
def copy_notebooks():
    src_nb_dir = os.path.join('notebooks')
    dst_nb_dir = os.path.join(nb_dir, pip_name)
    if os.path.exists(dst_nb_dir):
        shutil.rmtree(dst_nb_dir)
    copy_tree(src_nb_dir, dst_nb_dir)

check_env()
copy_notebooks()

setup(
    name=package_name,
    version='0.1.0',
    install_requires=[
        'plotly==4.5.2',
        'pynq==2.6',
        'rfsoc-sam @ https://github.com/strath-sdr/rfsoc_sam/archive/v0.2.2.tar.gz',
        'rfsoc-freqplan @ https://github.com/strath-sdr/rfsoc_frequency_planner/archive/v0.1.0.tar.gz',
        'rfsoc-ofdm @ https://github.com/strath-sdr/rfsoc_ofdm/archive/v0.2.0.tar.gz',
        'rfsoc-qpsk @ https://github.com/strath-sdr/rfsoc_qpsk/archive/v1.3.0.tar.gz',
        'rfsoc-radio @ https://github.com/strath-sdr/rfsoc_radio/archive/v0.1.0.tar.gz',
        'pystrath-dsp @ https://github.com/strath-sdr/dsp_notebooks/archive/v0.1.0.tar.gz',
        'pystrath-rfsoc @ https://github.com/strath-sdr/rfsoc_notebooks/archive/v0.1.0.tar.gz'
    ],
    author="David Northcote",
    packages=find_packages(),
    package_data={
        '': data_files,
    },
    description="University of Strathclyde RFSoC Studio.")

# 'pynq-agc @ https://github.com/strath-sdr/pynq_agc/releases/download/v0.3/pynq_agc.tar.gz',
