#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/5/12 14:31
# @Author : 詹荣瑞
# @File : app.py
# @desc : 本代码未经授权禁止商用
import os
from typing import Tuple
from bonetex.utils import save_file
from bonetex.command import CommandSection, CommandRender, CommandInclude, CommandBase
from bonelate import render
from bonerator import Document, Section, ContentList


def create_document_by_dict(source: dict, level=0) -> Document:
    if level == 0:
        contents = Document()
    else:
        contents = ContentList()
    for child_key, value in source.items():
        if isinstance(value, str):
            sec = Section(child_key, level).append(
                value
            )
        else:
            sec = Section(child_key, level).append(
                create_document_by_dict(value, level + 1)
            )
        contents.append(sec)
    return contents


class App(object):

    def __init__(self, template: dict = None, data: dict = None):
        self.document = create_document_by_dict(template or {})
        self.currents = [self.document]
        self.blocks = {}
        self.data = data or {}

    def command(self, func, name="Command"):

        class Command(CommandBase):
            __name__ = name

            def __call__(self, *args, **kwargs):
                return func(*args, **kwargs)

        return Command(self)

    def create_command(self):
        return CommandSection(self), CommandRender(self), CommandInclude(self)

    def generate(self):
        temp_path = "./resources"
        if not os.path.exists(temp_path):
            os.mkdir(temp_path)
        save_file(f"{temp_path}/document.tex", render(self.document.latex(), self.data))
        return
