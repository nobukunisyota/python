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


    """
    Filter files by extension
    """
    def files_grep_extention(self, extention):
        return [_ for _ in os.listdir(self.filename) if _.endswith(extention)]

    
    """
    do decompose
    """
    @classmethod
    def do_decompress(cls, filepath):
        try:
            subprocess.run(["gzip", "-dvkf", filepath], check=True)
        except subprocess.CalledProcessError:
            print(f"error occur at {filepath}")


    """
    decompose context in text
    """
    @classmethod
    def output(cls, filepath):
        try:
            subprocess.run(["tar", "-zxOf", filepath], check=True)
        except subprocess.CalledProcessError:
            print(f"error occur at {filepath}")


    """
    main method
    """
    def to_text(self):
        # decompose paslog from tar.gz to tar
        for file in self.files_grep_extention(self.filename, r".tar.gz"):
            self.do_decompress(os.path.join(self.filename, file))

        # grep paslog keyword
        for file in self.files_grep_extention(self.filename, r".tar"):
            self.output(os.path.join(self.filename, file))

