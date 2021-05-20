#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/5/13 13:27
# @Author : 詹荣瑞
# @File : section.py
# @desc : 本代码未经授权禁止商用
from bonerator import Section
from .base import CommandBase


class CommandSection(CommandBase):

    def __init__(self, app, level=0):
        super().__init__(app)
        self.level = level
        self.current = None

    def __call__(self, title: str):
        self.current = Section(title, self.level)
        self.app.currents[-1].append(
            self.current
        )
        return self

    def __enter__(self):
        self.level += 1
        self.app.currents.append(self.current)
        return self.current

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1
        self.app.currents.pop()
