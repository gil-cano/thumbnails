# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageOps
from PIL import ImageDraw

import glob
import os

size = (160, 160)
mask = Image.new('L', size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0) + size, fill=255)

thumb_size = 98, 98
padding = 8
paths = ['investigadores', 'tecnicos-academicos', 'posdoc', 'catedras-conacyt']


def thumbnails(path):
    for root, subdirs, files in os.walk(path):
        if '.DS_Store' in files:
            files.remove('.DS_Store')
        for fname in files:
            im = Image.open(os.path.join(root, fname))
            w, h = im.size
            # output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
            # output.putalpha(mask)
            output = ImageOps.fit(im, (w, w), centering=(0.5, 0.25))
            output.thumbnail(thumb_size, Image.ANTIALIAS)
            name = fname.split('.')[0]
            directory = 'cuadrados/{path}'.format(path=root)
            if not os.path.exists(directory):
                os.makedirs(directory)
            output.save('{path}/98x98-{name}.png'.format(
                path=directory, name=name))


def makeCollage(sede='C.U.', cols=10):
    path = 'cuadrados/investigadores'
    path2 = 'cuadrados/tecnicos-academicos'
    # path2 = 'cuadrados/posdoc'
    # path2 = 'cuadrados/catedras-conacyt'
    inv = glob.glob('{p}/{s}/*.png'.format(p=path, s=sede))
    tec = glob.glob('{p}/{s}/*.png'.format(p=path2, s=sede))
    n = len(inv) + len(tec)
    rows = n/cols + (n % cols > 0)
    w = cols * thumb_size[0] + (cols + 1) * padding
    h = rows * thumb_size[1] + (rows + 1) * padding
    collage = Image.new('RGBA', (w, h))
    x = y = 0
    for i, filename in enumerate(inv + tec):
        im = Image.open(filename)
        x = (padding*(i+1) + im.size[0]*i) % (w - padding)
        y = padding*int(i/cols + 1) + im.size[1] * int(i/cols)
        collage.paste(im, (x, y))
    collage.save('{s}.png'.format(s=sede))


if __name__ == '__main__':
    for path in paths:
        thumbnails(path)
    makeCollage(cols=9)
    makeCollage(sede='Cuernavaca', cols=8)
    makeCollage(sede='Juriquilla', cols=3)
    makeCollage(sede='Oaxaca', cols=3)
    # makeCollage(cols=5)
    # makeCollage(sede='Cuernavaca', cols=5)
    # makeCollage(sede='Juriquilla', cols=3)
