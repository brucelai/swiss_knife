#!/usr/bin/env python
"""
Spliting single image into multiple sub-images.
"""
#import numpy as np
from PIL import Image

def split_images(
        dfile,
):
    im = Image.open(dfile)
    width, height = im.size
	
    for i in range(3):
        for j in range(3):
            left = i * width/2
            top = j * height/2
            box = (left, top, left+width/2, top+height/2)
            roi = im.crop(box)
            roi.save(dfile + '_' + str(i) + '_' + str(j) + '.jpg')
		
    return 0

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument("--dfile", help="picture filename.")
    args = parser.parse_args()

    split_images(args.dfile)
