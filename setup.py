import os
import shutil
from distutils.dir_util import copy_tree

from setuptools import find_packages, setup

# global variables
board = os.environ['BOARD']
repo_board_folder = f'boards/{board}'
repo_notebook_folder = f'boards/{board}/notebooks'
board_notebooks_dir = os.environ['PYNQ_JUPYTER_NOTEBOOKS']
package_name = 'rfstrath'
hw_data_files = []

# check whether board is supported
def check_env():
    if not os.path.isdir(repo_board_folder):
        raise ValueError("Board {} is not supported.".format(board))
    if not os.path.isdir(board_notebooks_dir):
        raise ValueError(
            "Directory {} does not exist.".format(board_notebooks_dir))

# copy overlays to python package
def copy_overlay():
    src_ol_dir = os.path.join(repo_board_folder, package_name, 'overlay')
    dst_ol_dir = os.path.join(package_name)
    copy_tree(src_ol_dir, dst_ol_dir)
    hw_data_files.extend(
        [os.path.join("..", dst_ol_dir, f) for f in os.listdir(dst_ol_dir)])

# copy notebooks to jupyter home
def copy_notebooks():
    src_nb_dir = os.path.join(repo_notebook_folder)
    dst_nb_dir = os.path.join(board_notebooks_dir, package_name)
    if os.path.exists(dst_nb_dir):
        shutil.rmtree(dst_nb_dir)
    copy_tree(src_nb_dir, dst_nb_dir)

check_env()
copy_overlay()
copy_notebooks()

setup(
    name=package_name,
    version='1.0',
    install_requires=[
        'pynq>=2.6',
        'plotly==4.5.2',
    ],
    author="David Northcote",
    packages=find_packages(),
    package_data={
        '': hw_data_files,
    },
    description="PYNQ RFSoC Strathclyde Template.")