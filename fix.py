#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from glob import glob
import itertools
import os
import sys

def run(folder):
    for file in glob(folder + "/*"):
        filename, file_extension = os.path.splitext(file)
        with open(file, "rb") as fp:
            data = fp.read()
            # if this line prints "file, 1, 2, 1" everything should be fine..
            # if this line prints "file, 1, 0, 0" it is probably corrupted by ftp 
            print(file, data.count(b"\n"), data.count(b"\r\n"), data.count(b"\r"))
        if data.count(b"\r\n") > 0:
            data = data.split(b"\r\n")
        else:
            data = data.split(b"\n")
        c = 0
        for join in itertools.product((b"\n", b"\r", b"\r\n"), repeat = len(data) - 1):
            c+=1
            print("%03d %s"%(c, str(b":".join(join))[2:-1]))
            new_data = data[0]
            for idx, j_str in enumerate(join):
                new_data += j_str + data[idx+1]
            with open("%s_%03d%s" % (filename, c, file_extension), "wb") as fp:
                fp.write(new_data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./fix.py foldername")
    run(sys.argv[1])
