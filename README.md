<img src="strathsdr_banner.png" />

# The Strathclyde RFSoC Studio
This repository is only compatible with [PYNQ images v2.7](https://github.com/Xilinx/PYNQ/releases) for the [ZCU111](https://www.xilinx.com/products/boards-and-kits/zcu111.html) and [RFSoC2x2](http://rfsoc-pynq.io/).

## Introduction
This repository contains the RFSoC Studio installer, which will install several demonstrations and notebooks onto your RFSoC development board.

<table border="0" align="center">
    <tr border="0">
        <td align="center" width="43.5%" border="0">
            <img src="notebooks/images/gif/rfsoc_sam.gif" alt="oscthumb" style="width: 100%" border="0"/>
        </td>
        <td align="center" width="50%" border="0">
            <img src="notebooks/images/gif/rfsoc_ofdm.gif" alt="oscthumb" style="width: 100%" border="0"/>
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

## Quick Start
Follow the instructions below to install the RFSoC Studio on your development board. **You will need to give your board access to the internet**.
* Power on your RFSoC2x2 or ZCU111 development board with an SD Card containing a fresh PYNQ v2.7 image.
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
pip3 install git+https://github.com/strath-sdr/rfsoc_studio@v0.3.0
```

Once the installation has complete, your Jupyter home workspace will be populated with several folders installed by each package. You can access the `rfsoc-studio` folder and open the getting started notebook to begin using all of the demonstrations and educational resources.

## Individual Package Installation <a class="anchor" id="individual_install"></a>
If you have a problem using the RFSoC-Studio installer, please run the following in your Jupyter Terminal.

* Firstly, ensure all packages are uninstalled.

```sh
pip3 uninstall -y rfsoc-sam rfsoc-freqplan rfsoc-ofdm rfsoc-qpsk rfsoc-radio pynq-agc pystrath-dsp rfsoc-studio
```

* Then run individual installation for each package.

```sh
pip3 install https://github.com/strath-sdr/rfsoc_sam/archive/v0.4.1.tar.gz
pip3 install https://github.com/strath-sdr/rfsoc_frequency_planner/archive/v0.3.1.tar.gz
pip3 install https://github.com/strath-sdr/rfsoc_ofdm/archive/v0.3.2.tar.gz
pip3 install https://github.com/strath-sdr/rfsoc_qpsk/archive/v1.4.2.tar.gz
pip3 install https://github.com/strath-sdr/rfsoc_radio/archive/v0.2.2.tar.gz
pip3 install https://github.com/strath-sdr/dsp_notebooks/archive/v0.1.3.tar.gz
pip3 install https://github.com/strath-sdr/pynq_agc/releases/download/v0.3.3/pynq_agc.tar.gz
```

* Finally run the rfsoc-studio installer again to complete setup.

```sh
pip3 install git+https://github.com/strath-sdr/rfsoc_studio
```

All required packages should now be installed.

## License
[BSD 3-Clause](/LICENSE)
