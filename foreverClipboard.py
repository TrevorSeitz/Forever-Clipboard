import sys
import pyperclip
import json

if len(sys.argv) == 2:
    command = sys.argv[1]
    
    if command == "save":
        print("Save")
    elif command == "load":
        print("Load")
    elif command == "list":
        print("List")
    else:
        print("Unknown command")
    
else:
    print("Please include only one command!")
