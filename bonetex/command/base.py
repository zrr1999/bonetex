#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/5/13 13:26
# @Author : 詹荣瑞
# @File : base.py
# @desc : 本代码未经授权禁止商用
class CommandBase(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, *args, **kwargs):
        raise NotImplementedError

    def __getitem__(self, item):
        return self(item)

