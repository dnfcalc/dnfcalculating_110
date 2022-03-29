import json
import sys
import os

os.chdir(sys.path[0])


def get_equipment_info():
    equipment_info = {}
    with open("../configFiles/eq-base-data.json", encoding='utf-8') as fp:
        equipment_info = json.load(fp)
    return equipment_info