#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/5/13 13:53
# @Author : 詹荣瑞
# @File : render.py
# @desc : 本代码未经授权禁止商用
from bonerator import Section
from typing import Tuple
from bonelate import render
from .base import CommandBase


class CommandRender(CommandBase):

    def __call__(self, template: str, data: dict = None):
        if data is None:
            data = self.app.data
        content = render(template, data)
        self.app.currents[-1].append(
            content
        )

    def __getitem__(self, item: Tuple[str, dict]):
        name, data = item
        self(self.app.blocks[name], data)
