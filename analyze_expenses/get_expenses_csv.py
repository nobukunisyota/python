#!/usr/bin/env python

import os
from time import sleep
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

def click_login_button():
    element = DRIVER.find_element_by_link_text("Login")
    element.click()

def logout():
    DRIVER.quit()

@click.command()
def cmd():
    login()
    sleep(5)
    click_login_button()
    sleep(5)
    logout()

def main():
    cmd()

if __name__ == '__main__':
    main()