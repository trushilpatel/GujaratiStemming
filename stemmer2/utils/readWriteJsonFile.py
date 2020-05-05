import json


def writeJsonFile(data, file_name):
    json_file = open(file_name, 'w', encoding='utf-8')
    json.dump(data, json_file)
    json_file.close()


def readJsonFile(file_name):
    json_file = open(file_name, 'r', encoding='utf-8')
    data = json.load(json_file)
    return data
