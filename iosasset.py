#!/usr/bin/env python
from PIL import Image
from argh import arg, dispatch_command
import os
 
def gen_assets(source, force=False):
    if os.path.isdir(source):
        for root, dirs, files in os.walk(source):
            for d in dirs:
                gen_assets(os.path.join(root, d), force=force)
            for f in files:
                gen_assets(os.path.join(root, f), force=force)
    else:
        if source.endswith('@2x.png') and not source.endswith('-568h@2x.png'):
            dest = source.replace('@2x.png', '.png')
            if os.path.exists(dest) and os.path.getmtime(dest) > os.path.getmtime(source) and not force:
                return
            print '%s -> %s' % (source, dest)
            img = Image.open(source)
            width, height = img.size
            img.thumbnail((width/2, height/2), Image.ANTIALIAS)
            img.save(dest, "PNG")
 
@dispatch_command
@arg('FILE', default='.', help='File name or directory for searching assets')
@arg('--force', '-f', default=False, help='Force generating assets. Will overwrite existing files.')
def main(args):
    gen_assets(args.FILE, force=args.force)
