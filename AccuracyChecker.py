import StatisticalData
import numpy
import math

time_in_system_type_1_is_enough = False
time_in_system_type_2_is_enough = False
time_in_system_is_enough = False
time_in_queue_type_1_is_enough = False
time_in_queue_type_2_is_enough = False
time_in_queue_is_enough = False
mean_passed_deadline_type_1 = False
mean_passed_deadline_type_2 = False
mean_passed_deadline = False
mean_scheduler_queue_length = False
mean_servers_queue_length = []


def initial(system):
    global mean_servers_queue_length
    for _ in system.servers:
        mean_servers_queue_length += [False]


def get_accuracy(ls):
    if len(ls) == 0:
        return 1
    mean = numpy.mean(ls)
    sigma = numpy.std(ls)
    if len(ls) != 0 and mean != 0:
        return (1.96 * sigma) / (math.sqrt(len(ls)) * mean)
    else:
        return 1


def is_enough():
    for x in mean_servers_queue_length:
        if not x:
            return False
    if not time_in_system_type_1_is_enough:
        return False
    if not time_in_system_type_2_is_enough:
        return False
    if not time_in_system_is_enough:
        return False
    if not time_in_queue_type_1_is_enough:
        return False
    if not time_in_queue_type_2_is_enough:
        return False
    if not time_in_queue_is_enough:
        return False
    if not mean_passed_deadline_type_1:
        return False
    if not mean_passed_deadline_type_2:
        return False
    if not mean_passed_deadline:
        return False
    if not mean_scheduler_queue_length:
        return False
    return True


def check_time_in_system_type_1_is_enough(statistical_data):
    global time_in_system_type_1_is_enough
    if get_accuracy(statistical_data.mean_time_spent_in_system_type_1) < 0.05:
        time_in_system_type_1_is_enough = True


def check_time_in_system_is_enough(statistical_data):
    global time_in_system_is_enough
    if get_accuracy(statistical_data.mean_time_spent_in_system_type_1 + statistical_data.mean_time_spent_in_system_type_2) < 0.05:
        time_in_system_is_enough = True


def check_time_in_system_type_2_is_enough(statistical_data):
    global time_in_system_type_2_is_enough
    if get_accuracy(statistical_data.mean_time_spent_in_system_type_2) < 0.05:
        time_in_system_type_2_is_enough = True


def check_time_in_queue_type_1_is_enough(statistical_data):
    global time_in_queue_type_1_is_enough
    if get_accuracy(statistical_data.mean_time_waiting_in_queue_type_1) < 0.05:
        time_in_queue_type_1_is_enough = True


def check_time_in_queue_type_2_is_enough(statistical_data):
    global time_in_queue_type_2_is_enough
    if get_accuracy(statistical_data.mean_time_waiting_in_queue_type_2) < 0.05:
        time_in_queue_type_2_is_enough = True


def check_time_in_queue_is_enough(statistical_data):
    global time_in_queue_is_enough
    if get_accuracy(statistical_data.mean_time_waiting_in_queue_type_1 + statistical_data.mean_time_waiting_in_queue_type_2) < 0.05:
        time_in_queue_is_enough = True


def check_mean_passed_deadline_type_1(statistical_data):
    global mean_passed_deadline_type_1
    if get_accuracy(statistical_data.mean_passed_deadline_type_1) < 0.05:
        mean_passed_deadline_type_1 = True


def check_mean_passed_deadline_type_2(statistical_data):
    global mean_passed_deadline_type_2
    if get_accuracy(statistical_data.mean_passed_deadline_type_2) < 0.05:
        mean_passed_deadline_type_2 = True


def check_mean_passed_deadline(statistical_data):
    global mean_passed_deadline
    if get_accuracy(statistical_data.mean_passed_deadline) < 0.05:
        mean_passed_deadline = True


def check_mean_scheduler_queue_length(statistical_data):
    global mean_scheduler_queue_length
    if get_accuracy(statistical_data.scheduler_queue_length) < 0.05:
        mean_scheduler_queue_length = True


def check_mean_servers_queue_length(statistical_data):
    global mean_servers_queue_length
    for i in range(len(mean_servers_queue_length)):
        if get_accuracy(statistical_data.servers_queue_length[i]) < 0.05:
            mean_servers_queue_length[i] = True


def check(statistical_data):
    check_time_in_system_type_1_is_enough(statistical_data)
    check_time_in_system_type_2_is_enough(statistical_data)
    check_time_in_system_is_enough(statistical_data)
    check_time_in_queue_type_1_is_enough(statistical_data)
    check_time_in_queue_type_2_is_enough(statistical_data)
    check_time_in_queue_is_enough(statistical_data)
    check_mean_passed_deadline_type_1(statistical_data)
    check_mean_passed_deadline_type_2(statistical_data)
    check_mean_passed_deadline(statistical_data)
    check_mean_scheduler_queue_length(statistical_data)
    check_mean_servers_queue_length(statistical_data)
