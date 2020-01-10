import AccuracyChecker
report = ""


def add_report_simulation_finished_successfully(statistical_data, number_task, simulation_length, system, now):
    global report
    report += "simulation finished successfully\n"
    report += "number of task generated: " + str(number_task) + "\n"
    add_number_of_tasks(statistical_data)
    add_in_system_time(statistical_data)
    add_in_queue_time(statistical_data)
    add_passed_dead_line(statistical_data)
    add_queues_data(statistical_data, simulation_length, system, now)


def add_report_simulation_not_finished(statistical_data, number_task, simulation_length, system, now):
    global report
    report += "simulation didn't converge:(\n"
    report += "number of task generated: " + str(number_task) + "\n"
    add_number_of_tasks(statistical_data)
    add_in_system_time(statistical_data)
    add_in_queue_time(statistical_data)
    add_passed_dead_line(statistical_data)
    add_queues_data(simulation_length, system, now)


def add_number_of_tasks(statistical_data):
    global report
    report += "number of task finished their task: " + str(statistical_data.number_of_task_simulated) + "\n"
    report += "number of task finished their task type 1: " + str(
        len(statistical_data.time_spent_in_system_type_1)) + "\n"
    report += "number of task finished their task type 2: " + str(
        len(statistical_data.time_spent_in_system_type_2)) + "\n"


def add_in_system_time(statistical_data):
    global report
    report += "average time in system type 1: " + str(
        sum(statistical_data.time_spent_in_system_type_1) / len(statistical_data.time_spent_in_system_type_1)) + "  with accuracy: " + str(AccuracyChecker.get_accuracy(statistical_data.mean_time_spent_in_system_type_1)) + "\n"
    report += "average time in system type 2: " + str(
        sum(statistical_data.time_spent_in_system_type_2) / len(statistical_data.time_spent_in_system_type_2)) + "  with accuracy: " + str(AccuracyChecker.get_accuracy(statistical_data.mean_time_spent_in_system_type_2)) + "\n"
    report += "average time in system overall: " + str(
        (sum(statistical_data.time_spent_in_system_type_2) + sum(statistical_data.time_spent_in_system_type_1)) / (
                len(statistical_data.time_spent_in_system_type_2) + len(
            statistical_data.time_spent_in_system_type_1))) + "  with accuracy: " + str(AccuracyChecker.get_accuracy(statistical_data.mean_time_spent_in_system_type_1 + statistical_data.mean_time_spent_in_system_type_2)) + "\n"


def add_in_queue_time(statistical_data):
    global report
    report += "average time in queue type 1: " + str(
        sum(statistical_data.time_waiting_in_queue_type_1) / len(statistical_data.time_waiting_in_queue_type_1)) + "  with accuracy: " + str(AccuracyChecker.get_accuracy(statistical_data.mean_time_waiting_in_queue_type_1)) + "\n"
    report += "average time in queue type 2: " + str(
        sum(statistical_data.time_waiting_in_queue_type_2) / len(statistical_data.time_waiting_in_queue_type_2)) + "  with accuracy: " + str(AccuracyChecker.get_accuracy(statistical_data.mean_time_waiting_in_queue_type_2)) + "\n"
    report += "average time in queue overall: " + str(
        (sum(statistical_data.time_waiting_in_queue_type_1) + sum(statistical_data.time_waiting_in_queue_type_2)) / (
                len(statistical_data.time_waiting_in_queue_type_1) + len(
            statistical_data.time_waiting_in_queue_type_2))) + "  with accuracy: " + str(AccuracyChecker.get_accuracy(statistical_data.mean_time_waiting_in_queue_type_1 + statistical_data.mean_time_waiting_in_queue_type_2)) + "\n"


def add_passed_dead_line(statistical_data):
    global report
    report += "number of passed deadline type 1: " + str(statistical_data.number_of_passed_deadline_type_1) + "\n"
    report += "number of passed deadline type 2: " + str(statistical_data.number_of_passed_deadline_type_2) + "\n"
    report += "average passed deadline task type 1: " + str(statistical_data.number_of_passed_deadline_type_1 / (
            statistical_data.number_of_passed_deadline_type_1 + len(
        statistical_data.time_spent_in_system_type_1))) + "  with accuracy: " + str(AccuracyChecker.get_accuracy(statistical_data.mean_passed_deadline_type_1)) + "\n"
    report += "average passed deadline task type 2: " + str(statistical_data.number_of_passed_deadline_type_2 / (
            statistical_data.number_of_passed_deadline_type_2 + len(
        statistical_data.time_spent_in_system_type_2))) + "  with accuracy: " + str(AccuracyChecker.get_accuracy(statistical_data.mean_passed_deadline_type_2)) + "\n"
    report += "average passed deadline task overall: " + str(
        (statistical_data.number_of_passed_deadline_type_2 + statistical_data.number_of_passed_deadline_type_1) / (
                statistical_data.number_of_passed_deadline_type_2 + statistical_data.number_of_passed_deadline_type_1 + len(
            statistical_data.time_spent_in_system_type_2) + len(
            statistical_data.time_spent_in_system_type_1))) + "  with accuracy: " + str(AccuracyChecker.get_accuracy(statistical_data.mean_passed_deadline)) + "\n"


def add_queues_data(statistical_data, simulation_length, system, now):
    global report
    report += "scheduler average length: " + str(
        system.scheduler.get_sum_of_queue_length(now) / simulation_length) + "  with accuracy: " + str(AccuracyChecker.get_accuracy(statistical_data.scheduler_queue_length)) + "\n"
    for i in range(len(system.servers)):
        report += "server " + str(i) + " average length: " + str(
            system.servers[i].get_sum_of_queue_length(now) / simulation_length) + "  with accuracy: " + str(AccuracyChecker.get_accuracy(statistical_data.servers_queue_length[i])) + "\n"


def print_report(address):
    global report
    file = open(address, "w")
    file.write(report)
