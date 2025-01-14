# worker.py
from constants import SMALLEST_TIME_MEASUREMENT_UNIT, WORK_DAY

class Worker:
    def __init__(self, name):
        self.time_slots = [0 for _ in range(int(WORK_DAY / SMALLEST_TIME_MEASUREMENT_UNIT))]
        self.name = name

    def __repr__(self):
        return f"Worker: {self.name}, Time Slots: {self.time_slots}"

    def find_first_opportunity_to_do_task(self, task) -> int | None:
        required_time_slots = int(task.time / SMALLEST_TIME_MEASUREMENT_UNIT)
        consecutive_time_slots_found = 0
        index_of_task_start = None

        for i, time_slot in enumerate(self.time_slots):
            if time_slot:
                consecutive_time_slots_found = 0
                index_of_task_start = None
            else:
                if index_of_task_start is None:
                    index_of_task_start = i
                consecutive_time_slots_found += 1
                if consecutive_time_slots_found == required_time_slots:
                    return index_of_task_start
        return None

    def pick_up_task(self, task, index_of_task_start: int):
        
        required_time_slots = int(task.time / SMALLEST_TIME_MEASUREMENT_UNIT)
        for i in range(index_of_task_start, index_of_task_start + required_time_slots):
            self.time_slots[i] = task.task_id
