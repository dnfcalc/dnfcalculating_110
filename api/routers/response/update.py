import os
import sys
from typing import List
from utils import zipfile

try:
    from lanzou.api import LanZouCloud
    from lanzou.api.types import *
    lzy = LanZouCloud()
except:
    pass


def check_update(version: str):
    if os.path.exists("./__ZFJtemp"):
        os.system('RMDIR /Q /S "{}"'.format('./__ZFJtemp'))
        os.remove("./elevate.exe.del")
        os.remove("./dnfcalc-api.exe.del")
    folder_info = lzy.get_folder_info_by_url(
        'https://wwn.lanzout.com/s/dcalc')
    if folder_info.code != LanZouCloud.SUCCESS:
        return False
    for file in folder_info.files:
        if file.name.startswith("DNF计算器"):
            print(file.name.split("_")[1].replace(".exe", ""), version)
            if file.name.split("_")[1].replace(".exe", "") == version:
                return False
            else:
                return True


def auto_update():
    folder_info = lzy.get_folder_info_by_url(
        'https://wwn.lanzout.com/s/dcalc-update')
    if folder_info.code != LanZouCloud.SUCCESS:
        return
    url = ""
    for file in folder_info.files:
        if file.name == "resources.zip":
            url = file.url
    lzy.down_file_by_url(url,
                         '',
                         './__ZFJtemp',
                         downloaded_handler=after_downloaded)
    # folder_info = lzy.get_folder_info_by_url(
    #     'https://wwn.lanzout.com/s/dcalc', '17173')
    # if folder_info.code != LanZouCloud.SUCCESS:
    #     return False
    # for file in folder_info.files:
    #     if file.name.startswith("DNF计算器"):
    #         if file.name.split("_")[1] == version:
    #             return False
    #         else:
    #             return True


def after_downloaded(file_path):
    try:
        os.rename("./dnfcalc-api.exe", "./dnfcalc-api.exe.del")
        os.rename("./elevate.exe", "./elevate.exe.del")
    except:
        pass
    zip_file = zipfile.ZipFile(file_path)
    zip_list = zip_file.namelist()  # 得到压缩包里所有文件
    for f in zip_list:
        # if not f.endswith('desktop.ini'):
        zip_file.extract(f, os.path.dirname("../"))
        # extracted_path.rename(newName)
        # 循环解压文件到指定目录
    zip_file.close()
