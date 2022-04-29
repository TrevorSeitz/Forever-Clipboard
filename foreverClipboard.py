from audioop import add
import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, "r") as file:
            data = json.load(file)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    
    if command == "save":
        key = input("enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("(", data[key], ")", " has been saved.")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("(", data[key], ")", " has been loaded")
    elif command == "list":
        keys = data.keys()
        for i in keys:
            print(i, ": ", data[i])
         #print(i)
        #print(keys[1])
    else:
        print("Unknown command")
    
else:
    print("Please include only one command!")

