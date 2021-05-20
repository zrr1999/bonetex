#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/5/12 14:32
# @Author : 詹荣瑞
# @File : utils.py
# @desc : 本代码未经授权禁止商用
import os


def include(src: str):
    path, ext = os.path.splitext(src)
    if ext == ".tex":
        with open(src, encoding="utf-8") as file:
            return file.read()
    elif ext == ".json":
        import json
        with open(src, encoding="utf-8") as file:
            return json.load(file)
    # return {
    #     "src": content,
    #     "type": ext
    # }


def read_file(path: str, mode="str"):
    with open(path, encoding="utf-8") as file:
        if mode == "str":
            output = file.read()
        elif mode == "json":
            import json
            output = json.load(file)
        else:
            output = ""
    return output


def save_file(path: str, content: str):
    with open(path, mode="w", encoding="utf-8") as file:
        file.write(content)
