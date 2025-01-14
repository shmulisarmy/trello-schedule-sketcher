# task.py
class Task:
    def __init__(self, task_id, name, time, assigned_to):
        self.task_id = task_id
        self.name = name
        self.time = time
        self.assigned_to = assigned_to
        self.picked_up_by = []

    def __repr__(self):
        return f"Task(task_id={self.task_id}, task_id={self.name}, time={self.time}, assigned_to={self.assigned_to}), picked_up_by={self.picked_up_by}"

    def display(self):
        print(self)
