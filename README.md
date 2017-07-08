## Python hack for changing colors in SteelSeries The SIMs 4 Gaming Headset 51161

### Description
SteelSeries Engine has no support for linux. This is a python implementation based on [HIDapi](https://github.com/gbishop/cython-hidapi) for [these headphones](http://www.amazon.in/SteelSeries-SIMs-Gaming-Headset-51161/dp/B00LIW8I2Q).

This can only change colors persistently for now. Writing the config for other options is not supported. Tested on Ubuntu 16.04 but should support other linux and Windows. ** Its a hack. Use at your own risk. Totally on IDGAF License**  

### Dependencies
 On Ubuntu
 ```bash
 $ sudo apt-get install libusb-1.0-0-dev libudev-dev
 ```
should do the job.

### Installation
Clone this repo. Its better if you work in a virtualenv.
```bash
$ pip install cython tkcolorpicker
$ cd cython-hidapi
$ python setup.py build
$ python setup.py install
$ cd ../
$ python color_changer.py
```
Choose your color and done!
