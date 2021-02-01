import os
import shutil
from distutils.dir_util import copy_tree

from setuptools import find_packages, setup

# global variables
board = os.environ['BOARD']
nb_dir = os.environ['PYNQ_JUPYTER_NOTEBOOKS']
package_name = 'rfsoc_studio'
package_list = ['rfsoc_sam', 'rfsoc_qpsk', 'rfsoc_ofdm', 'pystrath_sdr']
hw_files = []

# check whether board is supported
def check_env():
    if not os.path.isdir(f'boards/{board}'):
        raise ValueError("Board {} is not supported.".format(board))
    if not os.path.isdir(nb_dir):
        raise ValueError(
            "Directory {} does not exist.".format(nb_dir))
    if os.path.exists(os.path.join(nb_dir, 'strathclyde')):
        shutil.rmtree(os.path.join(nb_dir, 'strathclyde'))

# copy unique notebooks to jupyter home
def copy_unique_notebooks():
    src_dir = os.path.join(f'boards/{board}/notebooks')
    dst_dir = os.path.join(nb_dir, package_name, 'board_notebooks')
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    copy_tree(src_dir, dst_dir)

# copy notebooks to jupyter home
def copy_common_notebooks():
    src_dir = os.path.join(f'notebooks')
    dst_dir = os.path.join(nb_dir, 'strathclyde', package_name, 'common_notebooks')
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    copy_tree(src_dir, dst_dir)

# copy notebooks from installed packages
def copy_package_notebooks():
    for package in package_list:
        src_dir = os.path.join(nb_dir, package)
        dst_dir = os.path.join(nb_dir, 'strathclyde', package_name, 'package_notebooks')
        if os.path.exists(src_dir):
            copy_tree(src_dir, dst_dir)
            shutil.rmtree(src_dir)

check_env()
copy_unique_notebooks()
copy_common_notebooks()
copy_package_notebooks()

setup(
    name=package_name,
    version='1.0',
    install_requires=[
        'pynq==2.6',
        'plotly==4.5.2',
        'rfsoc-sam @ git+https://github.com/strath-sdr/rfsoc_sam_private',
        'rfsoc-ofdm @ git+https://github.com/strath-sdr/rfsoc_ofdm@refactor_project',
        'rfsoc-qpsk @ git+https://github.com/strath-sdr/rfsoc_qpsk_private',
        'pystrath-sdr @ git+https://github.com/strath-sdr/sdr_course@refactor'
    ],
    author="David Northcote",
    packages=find_packages(),
    package_data={
        '': hw_files,
    },
    description="University of Strathclyde RFSoC Studio.")