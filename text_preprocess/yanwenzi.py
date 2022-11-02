# -*- coding: utf-8 -*-
# @Time    : 11/2/22 12:02 PM
# @Author  : LIANYONGXING
# @FileName: yanwenzi.py
# @Software: PyCharm
# @Repo    : https://github.com/lianyongxing/

import json

if __name__ == '__main__':

    json_data = open("../resources/yanwenzi/yanwenzi.json", "r", encoding="utf-8").read()
    json_data = eval(json_data)
    print(json_data)
    # ywz = yanwenzi(json_data)