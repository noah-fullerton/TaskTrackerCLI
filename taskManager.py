import json
from pathlib import Path


filename = Path("tasks.json")
taskList = {}

def updateTasks():
    """add new tasks to the list"""
    pass

def updateFile():
    """updates the json file with the new taskList"""
    if not filename.exists():
        filename.touch()
    with open(filename, "w") as json_file:
        json.dump(taskList, json_file, indent=4)
    


if __name__ == '__main__':
    updateFile()