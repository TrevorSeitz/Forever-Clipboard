from audioop import add
import sys
import pyperclip
import json

def save_items(filepath, data):
    with open(filepath, "w"):
        json.dump(data. f)

def load_items(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
        return data

if len(sys.argv) == 2:
    command = sys.argv[1]
    
    if command == "save":
        print("Save")
        save_items("clipboard.json", )
    elif command == "load":
        print("Load")
    elif command == "list":
        print("List")
    else:
        print("Unknown command")
    
else:
    print("Please include only one command!")
