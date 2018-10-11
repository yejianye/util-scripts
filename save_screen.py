#!/usr/bin/env python

import argparse
import subprocess
import tempfile
import os

from PIL import Image

def _save_screenshot(filename):
    subprocess.call(['pngpaste', filename])

def save_screenshot(filename, scale=1.0):
    if scale == 1.0:
        _save_screenshot(filename)
    else:
        tmpfile = tempfile.mktemp(suffix='.png')
        _save_screenshot(tmpfile)
        img = Image.open(tmpfile)
        width, height = int(img.size[0] * scale), int(img.size[1] * scale)
        img.thumbnail((width, height), Image.ANTIALIAS)
        img.save(filename, "PNG")
        os.unlink(tmpfile)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Save screen shot to image file')
    parser.add_argument("--filename", default='screenshot.png', help='File path for saving the screen shot')
    parser.add_argument("--scale", type=float, default=1.0, help='Scale screenshot when saving it')
    args = parser.parse_args()
    save_screenshot(args.filename, args.scale)
