import json
import sys
import os

import requests

os.chdir(sys.path[0])


def get_equipment_info():
    equipment_info = {}
    with open("../configFiles/eq-base-data.json", encoding='utf-8') as fp:
        equipment_info = json.load(fp)
    return equipment_info

def get_equipment_detail_info(equID):
  equipment_detail_info = {}
  try:
    equipment_detail_info = requests.get(
    "https://www.skycity.top:8019/api/equipment/"+equID+"?simple=false",
    timeout=2).json()["data"]
  except:
    pass
  return equipment_detail_info