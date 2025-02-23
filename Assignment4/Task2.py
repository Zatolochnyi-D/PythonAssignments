class TaskManager:
    def __init__(self):
        self.__tasks = []

    def add_task(self, task):
        self.__tasks.append(task)

class Task:
    def __init__(self, description, status, deadline):
        self.__description = description
        self.__status = status
        self.__deadline = deadline

mngr = TaskManager()
mngr.add_task(Task("desc", "important", "04.51.1984"))
mngr.__tasks  # Expected: AttributeError