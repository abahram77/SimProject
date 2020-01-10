from SystemClass import System


class StatisticalData:
    def __init__(self, input_data):
        self.in_data = input_data
        self.time_spent_in_system_type_1 = []  # this list does'nt contains tasks that left because of deadline TODO check it
        self.time_spent_in_system_type_2 = []  # this list does'nt contains tasks that left because of deadline
        self.time_waiting_in_queue_type_1 = []  # this list does'nt contains tasks that left because of deadline
        self.time_waiting_in_queue_type_2 = []  # this list does'nt contains tasks that left because of deadline
        self.number_of_passed_deadline_type_1 = 0
        self.number_of_passed_deadline_type_2 = 0
        self.scheduler_queue_length = []  # this list does'nt contains tasks that left because of deadline
        self.servers_queue_length = []
        for _ in input_data["servers"]:
            self.servers_queue_length += [[]]
        self.number_of_task_simulated = 0  # this list does'nt contains tasks that left because of deadline

    def reset(self):
        self.time_spent_in_system_type_1 = []
        self.time_spent_in_system_type_2 = []
        self.time_waiting_in_queue_type_1 = []
        self.time_waiting_in_queue_type_2 = []
        self.number_of_passed_deadline_type_1 = 0
        self.number_of_passed_deadline_type_2 = 0
        self.scheduler_queue_length = []
        self.servers_queue_length = []
        for _ in self.in_data["servers"]:
            self.servers_queue_length += [[]]
        self.number_of_task_simulated = 0

    def leave_task(self, task):
        if task.task_type == 1:
            self.time_spent_in_system_type_1.append(task.end_core_service_time - task.arrival_time)
            self.time_waiting_in_queue_type_1.append((task.end_core_service_time - task.start_core_service_time) + (
                    task.end_scheduler_service_time - task.start_scheduler_service_time))
        else:
            self.time_spent_in_system_type_2.append(task.end_core_service_time - task.arrival_time)
            self.time_waiting_in_queue_type_2.append((task.end_core_service_time - task.start_core_service_time) + (
                    task.end_scheduler_service_time - task.start_scheduler_service_time))
        self.number_of_task_simulated += 1

    def update_removed_tasks(self, removed_task):
        if removed_task:
            for task in removed_task:
                if task.task_type == 1:
                    self.number_of_passed_deadline_type_1 += 1
                else:
                    self.number_of_passed_deadline_type_2 += 1

    def update_queue_length(self, system, now, start_main_simulation_time):
        if now == start_main_simulation_time:
            return
        self.scheduler_queue_length.append(system.scheduler.get_sum_of_queue_length(now) / (now - start_main_simulation_time))

        for i in range(len(self.servers_queue_length)):
            self.servers_queue_length[i].append(system.servers[i].get_sum_of_queue_length(now) / (now - start_main_simulation_time))
