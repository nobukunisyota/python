#!/usr/bin/env python3
# coding=utf-8

import os
import argparse
import subprocess


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename")
    return parser.parse_args()


def files_grep_extention(filename, extention):
    return [_ for _ in os.listdir(filename) if _.endswith(extention)]


def do_decompress(filepath):
    try:
        subprocess.run(["gzip", "-dvkf", filepath], check=True)
    except subprocess.CalledProcessError:
        print(f"error occur at {filepath}")


def output(filepath):
    try:
        subprocess.run(["tar", "-zxOf", filepath], check=True)
    except subprocess.CalledProcessError:
        print(f"error occur at {filepath}")


def paslog(args):
    # decompose paslog from tar.gz to tar
    for file in files_grep_extention(args.filename, r".tar.gz"):
        do_decompress(os.path.join(args.filename, file))

    # grep paslog keyword
    for file in files_grep_extention(args.filename, r".tar"):
        output(os.path.join(args.filename, file))


def main():
    args = get_args()
    paslog(args)


if __name__ == "__main__":
    main()
