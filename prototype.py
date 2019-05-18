from selenium import webdriver
import time

import requests
import json
import shutil
from random import randint
import os.path


TODAY_MONTH_DAY = 9 # current day
MONTH = 3  # current month
YEAR = 2019


def format(number):
    if number < 10:
        return '0' + str(number)
    else:
        return str(number)


def save_image_to_file(image, dirname, suffix):
    with open('{dirname}/{suffix}.jpg'.format(dirname=dirname, suffix=suffix), 'wb') as out_file:
        shutil.copyfileobj(image.raw, out_file)


def parse():
    month = format(MONTH)
    year = str(YEAR)
    for day in range(1, TODAY_MONTH_DAY + 1):
        day_formatted = format(day)
        day = str(day)
        for cam in range(6, 8):
            cam = str(cam)
            for hours in range(0, 24):
                hours = format(hours)
                for mins in range(0, 60, 5):
                    mins = format(mins)
                    for sec in range(3, 10):
                        sec = format(sec)
                        filename = 'cam_' + cam + '__' + year + '_' + month + '_' + day + '__' + hours + '_' + mins + '_' + sec
                        if (os.path.isfile('cam/' + filename + '.jpg')):
                            print("file exists.. skiping")
                            break
                        else:
                            url = 'https://sonatina.traxelektronik.pl/images/2019/4/' + day + '/922/cam0087_119_220' + cam + '_2019_' + month + '_' + day_formatted + '_' + hours + '_' + mins + '_' + sec + '.jpg'
                            browser.get(url)
                            if len(browser.title) > 0:
                                response = requests.get(url, stream=True)
                                save_image_to_file(response, "output", filename)
                                time.sleep(randint(1, 6))
                                print(url)


chrome_options = webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values.notifications': 2}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument("--start-maximized")

browser = webdriver.Chrome()
parse()
