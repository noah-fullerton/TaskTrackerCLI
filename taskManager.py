import json
from pathlib import Path


filename = Path("tasks.json")

# need to determine how to structure this

# make a manager function

# each of the task functions first needs to get infro from file
# then based on its funciton it either adds, removes, updates, the python dictionary taskList
# then it updates the file with the new content (except for list which just lists the tasks)
# need to make sure setTaskList is called at the end of any functions that modify
# gettasklist and settasklist are only called in the other functions

def getTaskList():
    """helper function to get the task list from the json file"""
    # make sure file exists
    if not filename.exists():
        filename.touch()

    # get info from file
    with open(filename, 'r') as json_file:
        taskList = json.load(json_file)
    return taskList

def setTaskList(taskList):
    """helper function to set the task list in the json file"""
    # make sure file exists
    if not filename.exists():
        filename.touch()

    # update file with new info
    with open(filename, "w") as json_file:
        json.dump(taskList, json_file, indent=4)

def addTask(description):
    """add new tasks to the list"""
    # get tasklist from file
    # append new task to end of tasklist with new description
    # rewrite file with new tasklist
    pass

def updateTask(id, newDescription):
    """update a task description by its ID"""
    # get tasklist from file
    # update task based off of taskID
    # rewrite file with new tasklist
    pass

def deleteTask(id):
    """remove a task by its ID"""
    # get tasklist from file
    # delete task based off taskID
    # rewrite file with new tasklist
    pass

def changeTaskStatus(id, status):
    """changes status of task"""
    # get tasklist from file
    # change task status to new status using id and given status
    # rewrite file with new tasklist
    pass

def listTasks():
    """list all tasks"""
    # get tasklist from file
    # return tasklist
    pass
    

if __name__ == '__main__':
    # this will be used for testing, not needed in final product
    pass