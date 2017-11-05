# image_compressor

### About

Compress size of jpg images reducing overall size with [PIL](http://www.pythonware.com/products/pil/). Included with two folders with images for testing purpose.

### Screenshot

![Screenshot](http://i.imgur.com/xPVcVIo.png)


### Usage

```
python compress.py /path/to/the/root/folder
```

Script will iterate over all sub folders in root directory and catch every image that ends with ```'.jpg'``` and compress it.

### Requirements

image_compressor uses just PIL. You can install it with:

```
sudo apt-get install libjpeg libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev
pip install PIL
```

### Installation and Running

```
https://github.com/Lazar-T/image_compressor
cd image_compressor
python compress /path/to/the/root/folder
```
