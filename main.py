# main.py
from constants import SMALLEST_TIME_MEASUREMENT_UNIT, WORK_DAY
from worker import Worker
from task import Task
from team import Team

workers = {
    1: Worker("Shmuli"),
    2: Worker("Mod"),
    3: Worker("Shneur"),
    4: Worker("Sarah"),
    5: Worker("Mendy"),
    6: Worker("Yona"),
}

tasks = [
    Task(1, "Check tire", 45, [1]),
    Task(2, "Clean truck", 30, [1, 3]),
    Task(3, "Clean floor", 30, [2, 4]),
    Task(4, "Paint walls", 30, [5, 6]),
    Task(5, "Clean windows", 45, [1, 2]),
    Task(6, "Move boxes", 45, [3, 4, 2]),
    Task(7, "Sweep floor", 45, [5, 6, 2]),
    Task(8, "Fill gas", 15, [2, 4]),
    Task(9, "Check brake", 15, [5, 6]),
]

rolling_kosher = Team(workers=workers, tasks=tasks)







rolling_kosher.make_schedule_from_tasks()


rolling_kosher.display()











import matplotlib.pyplot as plt
import numpy as np

# Assuming `team` is an instance of the Team class
# And `team.workers` is a dictionary of Worker instances

# def plot_task_distribution(team):
#     # Task Distribution among Workers
#     task_counts = {worker.name: len([task for task in team.tasks if worker.name in task.assigned_to]) for worker in team.workers.values()}

#     plt.figure(figsize=(10, 6))
#     plt.bar(task_counts.keys(), task_counts.values(), color='lightblue')
#     plt.title("Task Distribution Among Workers")
#     plt.xlabel("Workers")
#     plt.ylabel("Number of Tasks Assigned")
#     plt.grid(True)
#     plt.show()

def plot_worker_utilization(team):
    # Worker Time Utilization (in minutes)
    time_utilized = {worker.name: sum(worker.time_slots) * SMALLEST_TIME_MEASUREMENT_UNIT for worker in team.workers.values()}
    total_available_time = WORK_DAY  # Total workday time (in minutes)

    plt.figure(figsize=(10, 6))
    plt.bar(time_utilized.keys(), time_utilized.values(), color='skyblue', label='Utilized Time')
    plt.axhline(y=total_available_time, color='r', linestyle='--', label='Workday Limit')
    plt.title("Worker Time Utilization")
    plt.xlabel("Workers")
    plt.ylabel("Minutes Utilized")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_task_completion_timeline(team):
    # Task Completion Timeline for each worker (time slots occupied by tasks)
    fig, ax = plt.subplots(figsize=(10, 6))

    for worker in team.workers.values():
        # Each worker's occupied time slots
        task_start_times = [i for i, slot in enumerate(worker.time_slots) if slot != 0]
        task_end_times = [i + SMALLEST_TIME_MEASUREMENT_UNIT for i in task_start_times]

        ax.barh(worker.name, task_end_times, left=task_start_times, color='orange')

    ax.set_xlabel("Time Slots")
    ax.set_title("Task Completion Timeline for Each Worker")
    plt.grid(True)
    plt.show()

# Plot the graphs
# plot_task_distribution(rolling_kosher)
plot_worker_utilization(rolling_kosher)
plot_task_completion_timeline(rolling_kosher)
