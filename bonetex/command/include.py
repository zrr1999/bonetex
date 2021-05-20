#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/5/13 17:33
# @Author : 詹荣瑞
# @File : include.py
# @desc : 本代码未经授权禁止商用
from .base import CommandBase


class CommandInclude(CommandBase):

    def __call__(self, path: str):
        raise NotImplementedError

    def __getitem__(self, path: str):
        self(path)
