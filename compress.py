#!/usr/bin/python
import os
from sys import argv
from PIL import Image

script, rootdir = argv

COLOR_WHITE = "\033[1;37m{0}\033[00m"
COLOR_BLUE = "\033[1;36m{0}\033[00m"


folder_size = 0
for (path, dirs, files) in os.walk(rootdir):
    for file in files:
        filename = os.path.join(path, file)
        folder_size += os.path.getsize(filename)

pre_size = "%0.1f MB" % (folder_size/(1024*1024.0))

i = 0
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        image = os.path.join(subdir, file)
        if image.endswith('.jpg'):
            i = i + 1
            print COLOR_WHITE.format('Compressing: \t %s' % image)
            im = Image.open(image)
            im.save(image, quality=30)

print '\n'
print COLOR_BLUE.format('Compresson completed.')

print COLOR_BLUE.format('Compressed %s images' % i)

folder_size = 0
for (path, dirs, files) in os.walk(rootdir):
    for file in files:
        filename = os.path.join(path, file)
        folder_size += os.path.getsize(filename)

after_size = "%0.1f MB" % (folder_size/(1024*1024.0))

print COLOR_BLUE.format('Size of folder went from %s to %s' % (pre_size, after_size))
