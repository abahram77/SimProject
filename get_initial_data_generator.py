import generate_random_number
from TaskClass import *


# this class generates arrival times by our random generator numbers
class ArrivalTimeGenerator:
    def __init__(self, lambdaa):
        self.pre_arrival = None
        self.lambdaa = lambdaa
        self.time_between_arrivals_generator = generate_random_number.get_exponential_generator(1 / lambdaa)

    def get_next_task_arrival(self):
        if self.pre_arrival is None:
            self.pre_arrival = 0
            return 0
        self.pre_arrival += self.time_between_arrivals_generator.next_random()
        return self.pre_arrival


def get_arrival_time_generator(input_data):
    return ArrivalTimeGenerator(1 / input_data["lambda"])  # TODO check if input is exponential


# this class generates deadline time for our tasks from our random generator numbers
class DeadLineTimeGenerator:
    def __init__(self, alpha):
        self.alpha = alpha
        self.deadline_generator = generate_random_number.get_exponential_generator(alpha)

    def get_next_task_deadline(self):
        return self.deadline_generator.next_random()


def get_arrival_deadline_generator(input_data):
    return DeadLineTimeGenerator(input_data["alpha"])


# this class generates service time for our scheduler
class SchedulerServiceTimesGenerator:
    def __init__(self, mu):
        self.mu = mu
        self.service_time_generator = generate_random_number.get_exponential_generator(mu)

    def get_next_scheduler_service_time(self):
        return self.service_time_generator.next_random()


def get_scheduler_service_time_generator(mu):
    return SchedulerServiceTimesGenerator(mu)  # TODO check if input is exponential


# this class sets our tasks to type 1 or 2
class TaskTypeGenerator:
    def __init__(self, p, true_value, false_value):
        self.p = p
        self.true_val = true_value
        self.false_val = false_value
        self.task_type_generator = generate_random_number.get_bernoulli_generator(0.1, 1, 2)

    def get_next_task_type(self):
        return self.task_type_generator.next_random()


def get_arrival_types_generator():
    return TaskTypeGenerator(0.1, 1, 2)


# this class generates service time for our core
class CoreServiceTimeGenerator:
    def __init__(self, mu):
        self.exponential_generator = generate_random_number.get_exponential_generator(mu)

    def get_next_core_service_time(self):
        return self.exponential_generator.next_random()


def get_service_time_of_core_generator(mu):
    return CoreServiceTimeGenerator(mu)


# this class generates tasks for us
class TaskGenerator:
    def __init__(self, input_data):
        self.num = -1
        self.input_data = input_data
        self.arrival_time_generator = get_arrival_time_generator(input_data)
        self.arrival_deadline_generator = get_arrival_deadline_generator(input_data)
        self.arrival_type_generator = get_arrival_types_generator()

    def get_next_task(self):
        arrival = self.arrival_time_generator.get_next_task_arrival()
        deadline = self.arrival_deadline_generator.get_next_task_deadline()
        t_type = self.arrival_type_generator.get_next_task_type()
        self.num += 1
        return Task(arrival, arrival + deadline, t_type, self.num)


def get_task_generator(input_data):
    return TaskGenerator(input_data)
