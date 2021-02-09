import os
import shutil
from distutils.dir_util import copy_tree

from setuptools import find_packages, setup

# global variables
board = os.environ['BOARD']
nb_dir = os.environ['PYNQ_JUPYTER_NOTEBOOKS']
package_name = 'rfsoc_studio'
pip_name = 'rfsoc-studio'

repo_board_folder = f'boards/{board}/{package_name}'
package_list = ['rfsoc_sam', 'rfsoc_qpsk', 'rfsoc_ofdm', 'pystrath_sdr', 'pynq_agc']
pip_list = ['rfsoc-sam', 'rfsoc-qpsk', 'rfsoc-ofdm', 'pystrath-sdr', 'pynq-agc']
data_files = []

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
    dst_dir = os.path.join(nb_dir, 'strath-sdr', pip_name, 'notebooks', 'board')
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    copy_tree(src_dir, dst_dir)

# copy notebooks to jupyter home
def copy_common_notebooks():
    src_dir = os.path.join(f'notebooks')
    dst_dir = os.path.join(nb_dir, 'strath-sdr', pip_name, 'notebooks', 'common')
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    copy_tree(src_dir, dst_dir)

# copy getting started notebooks
def copy_package_notebooks():
    src_dir = os.path.join(f'boards/{board}/getting_started')
    dst_dir = os.path.join(nb_dir, 'strath-sdr')
    copy_tree(src_dir, dst_dir)

# copy board specific drivers
def copy_drivers():
    src_dr_dir = os.path.join(repo_board_folder, 'drivers')
    dst_dr_dir = os.path.join(package_name)
    copy_tree(src_dr_dir, dst_dr_dir)
    data_files.extend(
        [os.path.join("..", dst_dr_dir, f) for f in os.listdir(dst_dr_dir)])
    
# copy overlays to python package
def copy_overlays():
    src_ol_dir = os.path.join(repo_board_folder, 'bitstream')
    dst_ol_dir = os.path.join(package_name, 'bitstream')
    copy_tree(src_ol_dir, dst_ol_dir)
    data_files.extend(
        [os.path.join("..", dst_ol_dir, f) for f in os.listdir(dst_ol_dir)])

check_env()
copy_unique_notebooks()
copy_common_notebooks()
copy_package_notebooks()
copy_drivers()
copy_overlays()

setup(
    name=package_name,
    version='1.0',
    install_requires=[
        'plotly==4.5.2',
        'pynq==2.6',
        'pystrath-sdr @ git+https://github.com/strath-sdr/sdr_course',
        'rfsoc-ofdm @ git+https://github.com/strath-sdr/rfsoc_ofdm',
        'rfsoc-qpsk @ git+https://github.com/strath-sdr/rfsoc_qpsk_private',
        'rfsoc-sam @ git+https://github.com/strath-sdr/rfsoc_sam_private',
        'pynq_agc @ https://cramsay.co.uk/content/images/2021/02/pynq_agc.tar.gz'
    ],
    author="David Northcote",
    packages=find_packages(),
    package_data={
        '': data_files,
    },
    description="University of Strathclyde RFSoC Studio.")
