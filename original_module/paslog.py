#!/usr/bin/env python
# coding=utf-8

import os
import re
import argparse
import subprocess


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename")
    return parser.parse_args()


def files(filename):
    return os.listdir(filename)


def decompress(filepath):
    try:
        subprocess.run(["tar", "-zxvf", filepath], check=True)
    except subprocess.CalledProcessError:
        print("error occur")


def main():
    args = get_args()
    for file in files(args.filename):
        m = re.match('.*tar.gz$', file)
        if not m:
            continue
        decompress(os.path.join(os.getcwd(), file))


if __name__ == "__main__":
    main()
