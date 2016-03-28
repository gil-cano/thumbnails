# -*- coding: utf-8 -*-

from PIL import Image

import glob


thumb_size = 98, 98
padding = 8
paths = ['investigadores', 'tecnicos-academicos', 'posdoc', 'catedras-conacyt']


def makecollage(sede='CU', cols=10):
    """Create an image from small images."""
    path = 'cuadrados/investigadores'
    # path2 = 'cuadrados/2015/tecnicos-academicos'
    path2 = 'cuadrados/2015/posdoc'
    # path2 = 'cuadrados/catedras-conacyt'
    inv = glob.glob('{p}/{s}/*.png'.format(p=path, s=sede))
    tec = glob.glob('{p}/{s}/*.png'.format(p=path2, s=sede))
    n = len(inv) + len(tec)
    rows = int(n / cols) + (n % cols > 0)
    w = cols * thumb_size[0] + (cols + 1) * padding
    h = rows * thumb_size[1] + (rows + 1) * padding
    collage = Image.new('RGBA', (w, h))
    x = y = 0
    for i, filename in enumerate(inv + tec):
        im = Image.open(filename)
        x = (padding * (i + 1) + im.size[0] * i) % (w - padding)
        y = padding * int(i / cols + 1) + im.size[1] * int(i / cols)
        collage.paste(im, (x, y))
    collage.save('{s}.png'.format(s=sede))


if __name__ == '__main__':
    # investigadores
    # makecollage()
    # makecollage(sede='Cuernavaca', cols=8)
    # makecollage(sede='Juriquilla', cols=3)
    # makecollage(sede='Oaxaca', cols=3)

    # tecnicos
    # makecollage(cols=4)
    # makecollage(sede='Cuernavaca', cols=5)

    # posdoc
    makecollage(cols=3)
    makecollage(sede='Cuernavaca', cols=1)
    makecollage(sede='Juriquilla', cols=1)
    makecollage(sede='Oaxaca', cols=2)
