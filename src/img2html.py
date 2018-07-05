#!/bin/env python3
import sys
from os.path import basename, realpath

from PIL import Image

def GetPixels(path):
    img = Image.open(path)
    pixs, col, line = ([], 1, [])
    print('Getting Pixels from:', realpath(path))
    for x in list(img.getdata()):
        if col == img.size[0]:
            print(end='.', flush=True)
            pixs.append(line)
            col, line = (1, [])
            continue
        col = col + 1
        line.append('#'+('%02x' * len(x)) % x)
    print()
    return pixs

def GenHTML(o, pixs):
    o = realpath('{}.html'.format(o))
    with open(o, 'w') as f:
        print('Write to file:', o)
        f.write('<div>')
        for l in pixs:
            f.write('<div>')
            for color in l:
                f.write('<span style="display:inline-block;background:{};width:1px;height:1px;"></span>'.format(color))
            f.write('</div>')
            print(end='.', flush=True)
        f.write('</div>')
    print('\nDone:', o)
    pass

def main(imgs):
    for i in imgs:
        pixs = GetPixels(i)
        GenHTML(basename(i), pixs)
    pass

if __name__ == '__main__':
    main(sys.argv[1:])