#!/usr/bin/env python

import os
import click
from selenium import webdriver
from dotenv import load_dotenv

# 環境変数読み込み
load_dotenv()
DRIVER_PATH = os.getenv('DRIVER_PATH')
URL = os.getenv('URL')

# driver 読み込み
DRIVER = webdriver.Chrome(DRIVER_PATH)

def login():
    DRIVER.get(URL)

@click.command()
def cmd():
    login()

def main():
    cmd()

if __name__ == '__main__':
    main()