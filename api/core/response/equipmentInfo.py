import json
import sys
import os

import requests

os.chdir(sys.path[0])
equ_details = dict()

def get_equipment_info():
    equipment_info = {
      "equipment_Lv110" : {},
      "equipment_myth" : {},
      "equipment_weapon" : {},
    }
    with open("../configFiles/eq-base-data.json", encoding='utf-8') as fp:
        equipment_info["equipment_Lv110"] = json.load(fp)
    with open("../configFiles/eq-myth-base-data.json", encoding='utf-8') as fp:
        equipment_info["equipment_myth"] = json.load(fp)
    with open("../configFiles/arm-base-data.json", encoding='utf-8') as fp:
        equipment_info["equipment_weapon"]= json.load(fp)
    return equipment_info

def get_equipment_detail_info(equID):
  equipment_detail_info = {}
  global equ_details
  if len(equ_details)==0:
    with open("../configFiles/eq-info-data.json", encoding='utf-8') as fp:
      equ_details = dict()
      for item in json.load(fp):
        equ_details[str(item["id"])] = item
  try:
    equipment_detail_info = equ_details[str(equID)]
  except:
    equipment_detail_info = requests.get(
        "https://www.skycity.top:8019/api/equipment/"+equID+"?simple=false",
        timeout=2).json()["data"]
  return equipment_detail_info