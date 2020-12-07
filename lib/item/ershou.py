#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 此代码仅供学习与交流，请勿用于商业用途。
# 二手房信息的数据结构


class ErShou(object):
    def __init__(self, district, area, name, price, desc, pic, href):
        self.district = district.replace(',', '-')
        self.area = area.replace(',', '-')
        self.price = price.replace(',', '-')
        self.name = name.replace(',', '-')
        self.desc = desc.replace(',', '-')
        self.pic = pic.replace(',', '-')
        self.href = href.replace(',', '-')

    @staticmethod
    def header():
        return 'district,area,name,price,desc,href'

    def text(self):
        return self.district + "," + \
                self.area + "," + \
                self.name + "," + \
                self.price + "," + \
                self.desc + "," + \
                self.href
