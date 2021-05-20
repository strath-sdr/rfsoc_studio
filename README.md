<img src="strathsdr_banner.png" />

# The Strathclyde RFSoC Studio
This repository is only compatible with [PYNQ images v2.6](https://github.com/Xilinx/PYNQ/releases) for the [ZCU111](https://www.xilinx.com/products/boards-and-kits/zcu111.html) and [RFSoC2x2](http://rfsoc-pynq.io/).

## Introduction
This repository contains the RFSoC Studio installer, which will install several demonstrations and notebooks onto your RFSoC development board.

<table border="0" align="center">
    <tr>
        <td align="center" width="43.5%" border="0">
            <img src="demo_spectrum_analyser.gif" alt="oscthumb" style="width: 100%" border="0"/>
        </td>
        <td align="center" width="50%" border="0">
            <img src="demo_ofdm.gif" alt="oscthumb" style="width: 100%" border="0"/>
        </td>
    </tr>
</table>

<br>

RFSoC Tools and SDR demonstrations include:
* [RFSoC Spectrum Analyser](https://github.com/strath-sdr/rfsoc_sam)
* [RFSoC Frequency Planner](https://github.com/strath-sdr/rfsoc_frequency_planner)
* [OFDM Demonstrator](https://github.com/strath-sdr/rfsoc_ofdm)
* [QPSK Demonstrator](https://github.com/strath-sdr/rfsoc_qpsk)
* [BPSK Demonstrator](https://github.com/strath-sdr/rfsoc_radio)
* [PYNQ Automatic Gain Control](https://github.com/strath-sdr/pynq_agc)

Educational notebooks:
* [DSP Notebooks for Wireless Communications](https://github.com/strath-sdr/dsp_notebooks)
* [RFSoC Introductory Notebooks](https://github.com/strath-sdr/rfsoc_notebooks)

## Quick Start
Follow the instructions below to install the RFSoC Studio on your development board. **You will need to give your board access to the internet**.
* Power on your RFSoC2x2 or ZCU111 development board with an SD Card containing a fresh PYNQ v2.6 image.
* Navigate to Jupyter Labs by opening a browser (preferably Chrome) and connecting to `http://<board_ip_address>:9090/lab`.
* We need to open a terminal in Jupyter Lab. Firstly, open a launcher window as shown in the figure below:

<p align="center">
  <img src="open_jupyter_launcher.jpg" width="50%" height="50%" />
<p/>

* Now open a terminal in Jupyter as illustrated below:

<p align="center">
  <img src="open_terminal_window.jpg" width="50%" height="50%" />
<p/>

* Firstly, ensure all packages are uninstalled.

```sh
pip3 uninstall -y rfsoc-sam rfsoc-freqplan rfsoc-ofdm rfsoc-qpsk rfsoc-radio pynq-agc pystrath-dsp pystrath-rfsoc rfsoc-studio
```

* We can now install the RFSoC Studio. This will install all of the above projects and notebooks, and will also add a few additional notebooks.

```sh
pip3 install git+https://github.com/strath-sdr/rfsoc_studio
```

Once the installation has complete, your Jupyter home workspace will be populated with several folders installed by each package. You can access the `rfsoc-studio` folder and open the getting started notebook to begin using all of the demonstrations and educational resources.

Please complete installation by following the board specific instructions below.

## RFSoC2x2 Setup
The RFSoC2x2 does not require any additional setup.

## ZCU111 Setup
The ZCU111 requires an xrfdc patch and xrfclk patch. An optional Voila installation is required if you would like to use voila-dashboards. Please follow the instructions below.

### The xrfdc Patch
It is absolutely essential that the xrfdc package is patched. This procedure will overwrite the xrfdc's `__init__.py`. You will not lose any current xrfdc functionality. You will gain thresholding capabilities and fabric read and write register configurations for the RF Data Converters.

In the terminal window, run the following script:
```sh
mkdir /home/xilinx/GitHub
cd /home/xilinx/GitHub/
git clone https://github.com/dnorthcote/ZCU111-PYNQ
cd /home/xilinx/GitHub/ZCU111-PYNQ
cp /home/xilinx/GitHub/ZCU111-PYNQ/ZCU111/packages/xrfdc/pkg/xrfdc/__init__.py /usr/local/lib/python3.6/dist-packages/xrfdc/__init__.py
```

### The xrfclk Patch
We need to add a 384 MHz clock to the xrfclk package. We can simply overwrite __init__.py, with the changes.

In the terminal window, run the following script:
```sh
mkdir /home/xilinx/GitHub
cd /home/xilinx/GitHub/
git clone https://github.com/dnorthcote/ZCU111-PYNQ
cd /home/xilinx/GitHub/ZCU111-PYNQ
cp /home/xilinx/GitHub/ZCU111-PYNQ/ZCU111/packages/xrfclk/pkg/xrfclk/__init__.py /usr/local/lib/python3.6/dist-packages/xrfclk/__init__.py
```

### Voila Installation (Optional)
Many of the strath-sdr projects use Voila to create simple web applications using Jupyter notebooks. If you would like to use Voila on your ZCU111 development board, simply follow the instructions outlined in this [blog post](https://strath-sdr.github.io/pynq/linux/zynq/fpga/voila/2021/02/22/install-voila-on-pynq-v2-6.html). This is optional and not required to use the demonstrators.

## Troubleshooting
Please see below for support on installation issues and problems.

### The Installer Crashed During Download

>_Issue_ <br>
The installer crashed during package download. Jupyter Lab disconnects. A connected serial terminal reports kernel panic.

> _Resolution_ <br>
Ensure you are not using a SanDisk Extreme Pro SD Card and follow the installation instructions again.
Otherwise, install each of the packages individually following the [individual installation instructions](#individual_install).

### The Installer Crashed During Installation

> _Issue_ <br>
The installer crashed during package installation. Jupyter Lab disconnects. No report on the serial terminal.

> _Resolution_ <br>
Install each of the packages individually following the [individual installation instructions](#individual_install).

### Individual Installer BadZipFile

> _Issue_ <br>
You are using the individual installer workflow and encountered the message `zipfile.BadZipFile: File is not a zip file`. Installation will not proceed, even after executing the installation command again, due to pip cache.

> _Resolution_ <br>
Simply add `--no-cache-dir` at the end of the installation command. For example: <br>
`pip3 install https://github.com/strath-sdr/pynq_agc/releases/download/v0.3/pynq_agc.tar.gz --no-cache-dir`

## Individual Package Installation <a class="anchor" id="individual_install"></a>
If you have a problem using the RFSoC-Studio installer, please run the following in your Jupyter Terminal.

* Firstly, ensure all packages are uninstalled.

```sh
pip3 uninstall -y rfsoc-sam rfsoc-freqplan rfsoc-ofdm rfsoc-qpsk rfsoc-radio pynq-agc pystrath-dsp pystrath-rfsoc rfsoc-studio
```

* Then run individual installation for each package.

```sh
pip3 install https://github.com/strath-sdr/rfsoc_sam/archive/v0.2.2.tar.gz
pip3 install https://github.com/strath-sdr/rfsoc_frequency_planner/archive/v0.1.0.tar.gz
pip3 install https://github.com/strath-sdr/rfsoc_ofdm/archive/v0.2.0.tar.gz
pip3 install https://github.com/strath-sdr/rfsoc_qpsk/archive/v1.3.0.tar.gz
pip3 install https://github.com/strath-sdr/rfsoc_radio/archive/v0.1.0.tar.gz
pip3 install https://github.com/strath-sdr/dsp_notebooks/archive/v0.1.0.tar.gz
pip3 install https://github.com/strath-sdr/rfsoc_notebooks/archive/v0.1.0.tar.gz
pip3 install https://github.com/strath-sdr/pynq_agc/releases/download/v0.3/pynq_agc.tar.gz
```

* Finally run the rfsoc-studio installer again to complete setup.

```sh
pip3 install git+https://github.com/strath-sdr/rfsoc_studio
```

All required packages should now be installed.

## License
[BSD 3-Clause](/LICENSE)
