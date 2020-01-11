import simplejson as json
import os

if os.path.isfile("./PythonMisc/ages.json") and os.stat("./PythonMisc/ages.json").st_size != 0:
    old_file = open("./PythonMisc/ages.json", "r+")
    data = json.loads(old_file.read())
    print("Current age is", data["age"], "-- adding a year.")
    data["age"] = data["age"] + 1
    print("New age is", data["age"])
else:
    old_file = open("./PythonMisc/ages.json", "w+")
    data = {"name:": "Sweep", "age": 24}
    print("No file found, setting default age to", data["age"])

old_file.seek(0)
old_file.write(json.dumps(data))
