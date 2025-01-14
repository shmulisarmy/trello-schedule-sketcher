# team.py
from collections import defaultdict
from worker import Worker
from task import Task

class Team:
    def __init__(self, workers, tasks):
        self.workers = workers
        self.tasks: list[Task] = tasks

        # Compute total time needed per worker
        self.time_needed_to_complete_all_tasks = defaultdict(int)
        for task in self.tasks:
            for worker_id in task.assigned_to:
                self.time_needed_to_complete_all_tasks[worker_id] += task.time

        # Sort tasks by busyness score
        self.tasks.sort(key=lambda task: sum(self.time_needed_to_complete_all_tasks[worker_id] for worker_id in task.assigned_to), reverse=True)

    def display(self):
        print("******tasks******")
        for task in self.tasks:
            task.display()

        print("******workers******")
        for worker_id, worker in self.workers.items():
            print(worker)

    def first_consecutive_available_spot(self, task) -> int | None:
        first_available_slot = float('inf')
        for worker_id in task.assigned_to:
            worker: Worker = self.workers[worker_id]
            available_slot = worker.find_first_opportunity_to_do_task(task)
            if available_slot is not None:
                first_available_slot = min(first_available_slot, available_slot)
        return first_available_slot if first_available_slot != float('inf') else None

    def assign_to_first_consecutive_available_spot(self, task: Task) -> bool:
        first_available_slot = self.first_consecutive_available_spot(task)
        if first_available_slot is not None:
            for worker_id in task.assigned_to:
                worker: Worker = self.workers[worker_id]
                worker.pick_up_task(task, first_available_slot)
            task.picked_up_by.extend(task.assigned_to)
            return True
        return False
    
    def make_schedule_from_tasks(self):
        for task in self.tasks:
            if not self.assign_to_first_consecutive_available_spot(task):
                print(f"Couldn't assign task #{task.task_id} due to schedule conflicts.")

