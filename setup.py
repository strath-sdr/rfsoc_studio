import os
import shutil
from distutils.dir_util import copy_tree

from setuptools import find_packages, setup

# global variables
board = os.environ['BOARD']
nb_dir = os.environ['PYNQ_JUPYTER_NOTEBOOKS']
hw_files = []

# check whether board is supported
def check_env():
    if not os.path.isdir(f'boards/{board}'):
        raise ValueError("Board {} is not supported.".format(board))
    if not os.path.isdir(nb_dir):
        raise ValueError(
            "Directory {} does not exist.".format(nb_dir))

# copy overlays to python package
def copy_overlay():
    src_dir = os.path.join(f'boards/{board}', 'rfstudio', 'overlay')
    dst_dir = os.path.join('rfstudio')
    copy_tree(src_dir, dst_dir)
    hw_files.extend(
        [os.path.join("..", dst_dir, f) for f in os.listdir(dst_dir)])

# copy unique notebooks to jupyter home
def copy_unique_notebooks():
    src_dir = os.path.join(f'boards/{board}/notebooks')
    dst_dir = os.path.join(nb_dir, 'rfstudio', 'board_notebooks')
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    copy_tree(src_dir, dst_dir)

# copy notebooks to jupyter home
def copy_notebooks():
    src_dir = os.path.join(f'notebooks')
    dst_dir = os.path.join(nb_dir, 'rfstudio', 'common_notebooks')
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    copy_tree(src_dir, dst_dir)

check_env()
#copy_overlay()
copy_unique_notebooks()
copy_notebooks()

setup(
    name='rfstudio',
    version='1.0',
    install_requires=[
        'pynq==2.6',
        'plotly==4.5.2',
        'rfsoc-sam==1.0',
    ],
    dependency_links=[
        'git+ssh://git@github.com/dnorthcote/rfsoc_sam_private',
    ],
    author="David Northcote",
    packages=find_packages(),
    package_data={
        '': hw_files,
    },
    description="University of Strathclyde RFSoC Studio.")
