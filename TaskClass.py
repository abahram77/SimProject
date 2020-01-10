# This class shows the tasks that arrives in system with attributes of its arrival time, deadline, task type and number
# This class also has some attributes about starting and ending of scheduler service time, and starting and ending of core service time
class Task:
    def __init__(self, arrival_time, deadline, task_type, number):
        self.arrival_time = arrival_time
        self.deadline = deadline
        self.task_type = task_type
        self.number = number
        self.start_scheduler_service_time = None
        self.end_scheduler_service_time = None
        self.start_core_service_time = None
        self.end_core_service_time = None

    def __str__(self):
        return "number: " + str(self.number) + ", arrival: " + str(self.arrival_time) + ", deadline: " + str(
            self.deadline) + ", type: " + str(self.task_type)
