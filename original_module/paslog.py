#!/usr/bin/env python3
# coding=utf-8

import os
import argparse
import subprocess


class Paslog:
    """
    module for paslog analyze
    """

    def __init__(self, filename=None):
        self.filename = filename

    def files_grep_extention(self, extention):
        return [_ for _ in os.listdir(self.filename) if _.endswith(extention)]

    @classmethod
    def do_decompress(cls, filepath):
        try:
            subprocess.run(["gzip", "-dvkf", filepath], check=True)
        except subprocess.CalledProcessError:
            print(f"error occur at {filepath}")

    @classmethod
    def output(cls, filepath):
        try:
            subprocess.run(["tar", "-zxOf", filepath], check=True)
        except subprocess.CalledProcessError:
            print(f"error occur at {filepath}")

    def to_text(self):
        # decompose paslog from tar.gz to tar
        for file in self.files_grep_extention(self.filename, r".tar.gz"):
            self.do_decompress(os.path.join(self.filename, file))

        # grep paslog keyword
        for file in self.files_grep_extention(self.filename, r".tar"):
            self.output(os.path.join(self.filename, file))


# local debug !!
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename")
    parser.add_argument("-m", "--mode")
    return parser.parse_args()


def main():
    args = get_args()
    paslog_obj = Paslog(args.filename)
    paslog_obj.to_text()


if __name__ == "__main__":
    main()
