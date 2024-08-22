from datetime import datetime

class Task():
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.status = 'in_progress'
        self.createdAt = datetime.now()
        self.updatedAt = datetime.now()

    def __str__(self):
        return f"Task ID: {self.id}, Description: {self.description}, Status: {self.status}, Created At: {self.createdAt}, Updated At: {self.updatedAt}"
