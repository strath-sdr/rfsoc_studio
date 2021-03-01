import os
import shutil
import subprocess
import sys
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

def install(package, version):
    sys.stdout.write("Install rfsoc-sam at v0.2.2\r\n")
    #subprocess.check_call(["pip3", "install", "git+https://github.com/strath-sdr/rfsoc_sam@v0.2.2"])

check_env()
install("rfsoc_sam", "v0.2.2")

setup(
    name=package_name,
    version='0.1',
    author="David Northcote",
    packages=find_packages(),
    package_data={
        '': data_files,
    },
    description="University of Strathclyde RFSoC Studio.")
