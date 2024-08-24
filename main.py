import typer
import taskManager

app = typer.Typer()

@app.command()
def add(description: str):
    """add task to the list"""
    taskManager.addTask(description)
    print(f"Task '{description}' added to the list")


@app.command()
def update(id: int, description: str):
    """update a task by its ID"""
    taskManager.updateTask(id, description)
    print(f"Task {id} updated to '{description}'")


@app.command()
def delete(id: int):
    """remove a task by its ID"""
    taskManager.deleteTask(id)
    print(f"Task {id} deleted")


@app.command()
def mark_to_do(id: int):
    """mark task as to-do"""
    taskManager.changeTaskStatus(id, "to-do")

@app.command()
def mark_done():
    """mark task as done"""
    taskManager.changeTaskStatus(id, "done")

@app.command()
def list():
    """list all tasks"""
    print(taskManager.listTasks())


if __name__ == '__main__':
    app()

