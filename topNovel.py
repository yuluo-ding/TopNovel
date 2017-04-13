#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

url = "http://www.lkong.net/book/top/"


def write_list(info):
    with open('bookList.txt', 'a') as f:
        f.write(info + '\n')


def check_content(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'lxml')
    for content in soup.find_all("div", class_='one_box'):
        rank = content.div.string
        name = content.h3.string
        author = content.span.string
        info = rank + '  ' + name + '  ' + author
        write_list(info)


def get_all_url():
    url_list = ['1', '2', '3', '4']
    for ul in url_list:
        current_url = url + ul
        check_content(current_url)


if __name__ == '__main__':
    get_all_url()
