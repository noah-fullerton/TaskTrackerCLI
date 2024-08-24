import json
from pathlib import Path
from datetime import datetime


filename = Path("tasklist.json")

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
        with open(filename, "w") as json_file:
            json.dump({}, json_file, indent=4)

    # get info from file
    with open(filename, 'r') as json_file:
        taskList = json.load(json_file)
    return taskList

def setTaskList(taskList):
    """helper function to set the task list in the json file"""
    # update file with new info
    with open(filename, "w") as json_file:
        json.dump(taskList, json_file, indent=4)

def addTask(description):
    """add new tasks to the list"""
    taskList = getTaskList()

    # new id is id of last task + 1
    id = list(taskList.keys())[-1] + 1

    dt = datetime.now().isoformat()

    taskList[id] = {"description": description, "status": "to-do", "createdAt": dt, "updatedAt": dt}
    setTaskList(taskList)

def updateTask(id, newDescription):
    """update a task description by its ID"""
    taskList = getTaskList()
    taskList[str(id)]["description"] = newDescription
    setTaskList(taskList)

def deleteTask(id):
    """remove a task by its ID"""
    taskList = getTaskList()
    del taskList[str(id)]
    setTaskList(taskList)

def changeTaskStatus(id, status):
    """changes status of task"""
    taskList = getTaskList()
    taskList[str(id)]["status"] = status
    setTaskList(taskList)


def listTasks(status=None):
    """list all tasks"""
    taskList = getTaskList()
    if status is not None:
        conditionalTaskList = {}
        for x in taskList:
            if taskList[x]["status"] == status:
                conditionalTaskList[x] = taskList[x]
        return conditionalTaskList
                
    return taskList
    

if __name__ == '__main__':
    print(listTasks("done"))