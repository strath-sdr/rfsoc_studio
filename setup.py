import os
import shutil
from distutils.dir_util import copy_tree

from setuptools import find_packages, setup

# global variables
board = os.environ['BOARD']
nb_dir = os.environ['PYNQ_JUPYTER_NOTEBOOKS']
package_name = 'rfsoc_studio'
pip_name = 'rfsoc-studio'
package_list = ['rfsoc_sam', 'rfsoc_qpsk', 'rfsoc_ofdm', 'pystrath_sdr']
pip_list = ['rfsoc-sam', 'rfsoc-qpsk', 'rfsoc-ofdm', 'pystrath-sdr']
hw_files = []

# check whether board is supported
def check_env():
    if not os.path.isdir(f'boards/{board}'):
        raise ValueError("Board {} is not supported.".format(board))
    if not os.path.isdir(nb_dir):
        raise ValueError(
            "Directory {} does not exist.".format(nb_dir))

# copy unique notebooks to jupyter home
def copy_unique_notebooks():
    src_dir = os.path.join(f'boards/{board}/notebooks')
    dst_dir = os.path.join(nb_dir, 'strath-sdr', pip_name, 'board_notebooks')
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    copy_tree(src_dir, dst_dir)

# copy notebooks to jupyter home
def copy_common_notebooks():
    src_dir = os.path.join(f'notebooks')
    dst_dir = os.path.join(nb_dir, 'strath-sdr', pip_name, 'common_notebooks')
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    copy_tree(src_dir, dst_dir)

check_env()
copy_unique_notebooks()
copy_common_notebooks()

setup(
    name=package_name,
    version='1.0',
    install_requires=[
        'plotly==4.5.2',
        'pynq==2.6',
        'pystrath-sdr @ git+https://github.com/strath-sdr/sdr_course@refactor',
        'rfsoc-ofdm @ git+https://github.com/strath-sdr/rfsoc_ofdm',
        'rfsoc-qpsk==1.2 @ git+https://github.com/strath-sdr/rfsoc_qpsk_private',
        'rfsoc-sam==0.2 @ git+https://github.com/strath-sdr/rfsoc_sam_private'
    ],
    author="David Northcote",
    packages=find_packages(),
    package_data={
        '': hw_files,
    },
    description="University of Strathclyde RFSoC Studio.")
