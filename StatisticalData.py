from SystemClass import System


class StatisticalData:
    def __init__(self, input_data):
        self.in_data = input_data
        self.time_spent_in_system_type_1 = []  # this list does'nt contains tasks that left because of deadline TODO check it
        self.time_spent_in_system_type_2 = []  # this list does'nt contains tasks that left because of deadline
        self.time_waiting_in_queue_type_1 = []  # this list does'nt contains tasks that left because of deadline
        self.time_waiting_in_queue_type_2 = []  # this list does'nt contains tasks that left because of deadline
        self.mean_time_spent_in_system_type_1 = []
        self.mean_time_spent_in_system_type_2 = []
        self.mean_time_waiting_in_queue_type_1 = []
        self.mean_time_waiting_in_queue_type_2 = []
        self.sum_of_time_spent_in_system_type_1 = 0
        self.sum_of_time_spent_in_system_type_2 = 0
        self.sum_of_time_waiting_in_queue_type_1 = 0
        self.sum_of_time_waiting_in_queue_type_2 = 0
        self.number_of_passed_deadline_type_1 = 0
        self.number_of_passed_deadline_type_2 = 0
        self.mean_passed_deadline_type_1 = []
        self.mean_passed_deadline_type_2 = []
        self.mean_passed_deadline = []
        self.scheduler_queue_length = []  # this list does'nt contains tasks that left because of deadline
        self.servers_queue_length = []
        for _ in input_data["servers"]:
            self.servers_queue_length += [[]]
        self.number_of_task_simulated = 0  # this list does'nt contains tasks that left because of deadline

    def reset(self, system, now):  # this function resets all the lists
        self.time_spent_in_system_type_1 = []
        self.time_spent_in_system_type_2 = []
        self.time_waiting_in_queue_type_1 = []
        self.time_waiting_in_queue_type_2 = []
        self.time_spent_in_system_type_1 = []
        self.time_spent_in_system_type_2 = []
        self.time_waiting_in_queue_type_1 = []
        self.time_waiting_in_queue_type_2 = []
        self.sum_of_time_spent_in_system_type_1 = 0
        self.sum_of_time_spent_in_system_type_2 = 0
        self.sum_of_time_waiting_in_queue_type_1 = 0
        self.sum_of_time_waiting_in_queue_type_2 = 0
        self.number_of_passed_deadline_type_1 = 0
        self.number_of_passed_deadline_type_2 = 0
        self.mean_passed_deadline_type_1 = []
        self.mean_passed_deadline_type_2 = []
        self.mean_passed_deadline = []
        self.scheduler_queue_length = []
        self.servers_queue_length = []
        for _ in self.in_data["servers"]:
            self.servers_queue_length += [[]]
        self.number_of_task_simulated = 0
        system.scheduler.last_update_time = now
        system.scheduler.sum_of_queue_length = 0
        for server in system.servers:
            server.last_update_time = now
            server.sum_of_queue_length = 0

    def leave_task(self, task):  # this function works when
        sys_time = task.end_core_service_time - task.arrival_time
        queue_time = (task.end_core_service_time - task.start_core_service_time) + (
                    task.end_scheduler_service_time - task.start_scheduler_service_time)
        if task.task_type == 1:
            self.time_spent_in_system_type_1.append(sys_time)
            self.sum_of_time_spent_in_system_type_1 += sys_time
            self.time_waiting_in_queue_type_1.append(queue_time)
            self.sum_of_time_waiting_in_queue_type_1 += queue_time
        else:
            self.time_spent_in_system_type_2.append(sys_time)
            self.sum_of_time_spent_in_system_type_2 += sys_time
            self.time_waiting_in_queue_type_2.append(queue_time)
            self.sum_of_time_waiting_in_queue_type_2 += queue_time
        if self.time_spent_in_system_type_1:
            self.mean_time_spent_in_system_type_1 += [self.sum_of_time_spent_in_system_type_1 / len(self.time_spent_in_system_type_1)]
        if self.time_spent_in_system_type_2:
            self.mean_time_spent_in_system_type_2 += [self.sum_of_time_spent_in_system_type_2 / len(self.time_spent_in_system_type_2)]
        if self.time_waiting_in_queue_type_1:
            self.mean_time_waiting_in_queue_type_1 += [self.sum_of_time_waiting_in_queue_type_1 / len(self.time_waiting_in_queue_type_1)]
        if self.time_waiting_in_queue_type_2:
            self.mean_time_waiting_in_queue_type_2 += [self.sum_of_time_waiting_in_queue_type_2 / len(self.time_waiting_in_queue_type_2)]
        self.number_of_task_simulated += 1

    def update_removed_tasks(self, removed_task):  # this function updates the removed tasks list
        if removed_task is not None:
            for task in removed_task:
                if task.task_type == 1:
                    self.number_of_passed_deadline_type_1 += 1
                else:
                    self.number_of_passed_deadline_type_2 += 1
        if self.number_of_passed_deadline_type_1 + len(self.time_spent_in_system_type_1) != 0:
            self.mean_passed_deadline_type_1 += [self.number_of_passed_deadline_type_1 / (
                        self.number_of_passed_deadline_type_1 + len(self.time_spent_in_system_type_1))]
        if self.number_of_passed_deadline_type_2 + len(self.time_spent_in_system_type_2) != 0:
            self.mean_passed_deadline_type_2 += [self.number_of_passed_deadline_type_2 / (
                        self.number_of_passed_deadline_type_2 + len(self.time_spent_in_system_type_2))]
        if len(self.time_spent_in_system_type_1) != 0:
            self.mean_passed_deadline += [
                (self.number_of_passed_deadline_type_2 + self.number_of_passed_deadline_type_1) / (
                            self.number_of_passed_deadline_type_2 + len(
                        self.time_spent_in_system_type_2) + self.number_of_passed_deadline_type_1 + len(
                        self.time_spent_in_system_type_1))]

    def update_queue_length(self, system, now, start_main_simulation_time):  # this function updates the length of queue
        if now == start_main_simulation_time:
            return
        self.scheduler_queue_length.append(
            system.scheduler.get_sum_of_queue_length(now) / (now - start_main_simulation_time))

        for i in range(len(self.servers_queue_length)):
            self.servers_queue_length[i].append(
                system.servers[i].get_sum_of_queue_length(now) / (now - start_main_simulation_time))
