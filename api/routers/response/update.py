import os
import sys
from typing import List

from core.store import store
from utils import zipfile

try:
    from lanzou.api import LanZouCloud
    from lanzou.api.types import *
    lzy = LanZouCloud()
except:
    pass


def safeRm(path: str):
    if os.path.exists(path):
        os.remove(path)


def check_update(version: str):
    if os.path.exists("./__ZFJtemp"):
        os.system('RMDIR /Q /S "{}"'.format('./__ZFJtemp'))
        safeRm("./elevate.exe.del")
        safeRm("./dnfcalc-api.exe.del")
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


def update_progress(filename: str, total: int, current: int):
    store.set("/app/update/progress", current)
    store.set("/app/update/total", total)
    print("{}/{}".format(current, total))
    pass


def get_progress():
    current = store.get("/app/update/progress")
    total = store.get("/app/update/total")
    return current, total


def clear_progress():
    store.set("/app/update/progress", 0)
    store.set("/app/update/total", 0)
    pass


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
                         callback=update_progress,
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
    safeRm("./app/renderer")
    zip_file = zipfile.ZipFile(file_path)
    zip_list = zip_file.namelist()  # 得到压缩包里所有文件
    for f in zip_list:
        # if not f.endswith('desktop.ini'):
        zip_file.extract(f, os.path.dirname("../"))
        # extracted_path.rename(newName)
        # 循环解压文件到指定目录
    zip_file.close()
