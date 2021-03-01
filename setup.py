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
    version='0.1',
    install_requires=[
        'rfsoc-sam==0.2.2',
    ],
    dependency_links=[
        'git+https://github.com/strath-sdr/rfsoc_sam@v0.2.2#egg=rfsoc-sam-0.2.2'
    ],
    author="David Northcote",
    packages=find_packages(),
    package_data={
        '': data_files,
    },
    description="University of Strathclyde RFSoC Studio.")
