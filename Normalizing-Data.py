from glob import glob
import os.path
import json

for filepath in glob("original/*.json"):

    with open(filepath, "r", encoding="utf8") as openfile:
        json_object = json.load(openfile)

    for line in range(len(json_object)):
        json_object[line]["content"] = ' '.join(json_object[line]["content"])

    json_modified = json.dumps(json_object);

    with open("modified.txt w", encoding = 'utf8') as json_ModifiedFile:
        json.dump(json_modified, json_ModifiedFile)