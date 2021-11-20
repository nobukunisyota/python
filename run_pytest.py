#!/usr/bin/env python3
# coding=utf-8

import os
from original_module import paslog


def test_paslog_module():
    # paslog module pytest
    obj = paslog.Paslog(os.getcwd())
    obj_ret = obj.to_text()
    assert True == obj_ret
    return True


if __name__ == "__main__":
    if(test_paslog_module()):
        print("Succuss test_paslog_module !!")
