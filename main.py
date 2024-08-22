import typer
from task import Task

app = typer.Typer()

@app.command()
def add(task: str):
    tk1 = Task(id = 1, description = task)
    print(tk1)
    """add task to the list"""

@app.command()
def update():
    """update a task by its ID"""

@app.command()
def delete():
    """remove a task by its ID"""

@app.command()
def mark_in_progress():
    """mark task as in progress"""

@app.command()
def mark_done():
    """mark task as done"""

@app.command()
def list():
    """list all tasks"""



if __name__ == '__main__':
    app()

