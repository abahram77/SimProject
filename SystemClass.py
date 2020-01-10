import get_initial_data_generator
from LinkedListClass import LinkedList


# mu is the service rate in the scheduler
# is_idle shows the scheduler is busy or not
# queue_type_1 is our queue from type 1 task
# queue_type_2 is our queue from type 2 task

class Scheduler:
    def __init__(self, mu):
        self.last_update_time = 0
        self.sum_of_queue_length = 0
        self.mu = mu
        self.is_idle = True
        self.queue_type_1 = LinkedList()
        self.queue_type_2 = LinkedList()
        self.service_time_generator = get_initial_data_generator.get_scheduler_service_time_generator(mu)

    def set_idle(self):
        self.is_idle = True

    def set_busy(self):
        self.is_idle = False

    def add_to_queue(self, task, now):
        self.sum_of_queue_length += (now - self.last_update_time) * self.queue_length()
        if task.task_type == 1:
            self.queue_type_1.insert_at_start(task)
        else:
            self.queue_type_2.insert_at_start(task)

    def pop_of_queue(self, now):
        self.sum_of_queue_length += (now - self.last_update_time) * self.queue_length()
        if self.queue_type_1:
            return self.queue_type_1.pop_last()
        elif self.queue_type_2:
            return self.queue_type_2.pop_last()
        else:
            return None

    def queue_length(self):
        return self.queue_type_2.length + self.queue_type_1.length

    def get_next_service_time(self):
        return self.service_time_generator.get_next_scheduler_service_time()

    def get_sum_of_queue_length(self, now):
        return self.sum_of_queue_length + (now - self.last_update_time) * self.queue_length()


class Core:
    def __init__(self, mu):
        self.mu = mu
        self.is_idle = True
        self.service_time_generator = get_initial_data_generator.get_service_time_of_core_generator(mu)

    def get_next_service_time(self):
        return self.service_time_generator.get_next_core_service_time()

    def set_idle(self):
        self.is_idle = True

    def set_busy(self):
        self.is_idle = False


class Server:
    def __init__(self, mus):
        self.last_update_time = 0
        self.sum_of_queue_length = 0
        self.mus = mus
        self.cores = []
        for mu in mus:
            self.cores += [Core(mu)]
        self.queue_type_1 = LinkedList()
        self.queue_type_2 = LinkedList()

    def add_to_queue(self, task, now):
        self.sum_of_queue_length += (now - self.last_update_time) * self.queue_length()
        if task.task_type == 1:
            self.queue_type_1.insert_at_start(task)
        else:
            self.queue_type_2.insert_at_start(task)

    def get_idle_core(self):
        for core in self.cores:
            if core.is_idle:
                return core

    def pop_of_queue(self, now):
        self.sum_of_queue_length += (now - self.last_update_time) * self.queue_length()
        if self.queue_type_1:
            return self.queue_type_1.pop_last()
        elif self.queue_type_2:
            return self.queue_type_2.pop_last()
        else:
            return None

    def queue_length(self):
        return self.queue_type_2.length + self.queue_type_1.length

    def has_idle_core(self):
        for core in self.cores:
            if core.is_idle:
                return True
        return False

    def get_core(self, i):
        return self.cores[i]

    def get_number_of_cores(self):
        return len(self.mus)

    def get_sum_of_queue_length(self, now):
        return self.sum_of_queue_length + (now - self.last_update_time) * self.queue_length()


def remove_passed_deadlines_from_queue(linked_list, now):
    linked_list.filter(lambda task: task.deadline >= now)


class System:
    def __init__(self, input_data):
        self.scheduler = Scheduler(input_data['mu'])
        self.servers = []
        for server in input_data['servers']:
            self.servers += [Server(server)]

    def remove_passed_deadlines(self, now):
        remove_passed_deadlines_from_queue(self.scheduler.queue_type_1, now)
        remove_passed_deadlines_from_queue(self.scheduler.queue_type_2, now)
        for server in self.servers:
            remove_passed_deadlines_from_queue(server.queue_type_1, now)
            remove_passed_deadlines_from_queue(server.queue_type_2, now)

    def get_idle_core(self):
        for server in self.servers:
            for core in server.cores:
                if core.is_idle:
                    return server, core

    def has_idle_core(self):
        return self.get_idle_core() is not None
