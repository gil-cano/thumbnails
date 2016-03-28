# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageOps
from PIL import ImageDraw

import os

size = (160, 160)
mask = Image.new('L', size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0) + size, fill=255)

thumb_size = 98, 98
padding = 8
paths = ['investigadores', 'tecnicos-academicos', 'posdoc', 'catedras-conacyt']


def thumbnails(path):
    """Make square versions of images in path."""
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


if __name__ == '__main__':
    for path in paths:
        thumbnails('/'.join(['2015', path]))
