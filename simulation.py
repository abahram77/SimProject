from EventClass import Event
from EventClass import EventType
from TaskClass import Task
from StatisticalData import StatisticalData
import math

FEL = []


# starting the simulation
def simulate(number_of_warm_up_task, max_number_of_tasks, task_generator, system, statistical_data):
    global FEL

    def add_to_right_time_place(event):
        temp_stack = []
        put = False
        while FEL:
            e = FEL.pop()
            if e.time > event.time:
                FEL.append(e)
                FEL.append(event)
                put = True
                break
            elif e.time < event.time:
                temp_stack.append(e)
            else:
                if event.event_type > e.event_type:
                    FEL.append(e)
                    FEL.append(event)
                    put = True
                    break
                else:
                    temp_stack.append(e)
        if not put:
            FEL.append(event)
        while temp_stack:
            FEL.append(temp_stack.pop())

    def add_to_best_server(task, now):
        if system.has_idle_core():
            server, core = system.get_idle_core()
            core.set_busy()
            task.start_core_service_time = now
            add_to_right_time_place(
                Event(EventType.departure_of_core, now + core.get_next_service_time(), task, server, core))
            return
        min_index = -1
        min_length = math.inf
        for index in range(len(system.servers)):
            if system.servers[index].queue_length() < min_length:
                min_length = system.servers[index].queue_length()
                min_index = index
        else:
            system.servers[min_index].add_to_queue(task, now)

    def get_next_scheduler_task(now):
        if system.scheduler.queue_length() != 0:
            return system.scheduler.pop_of_queue(now)
        return None

    def remove_all_passed_deadlines(now):
        removed_task = system.remove_passed_deadlines(now)
        statistical_data.update_removed_tasks(removed_task)

    task = task_generator.get_next_task()
    add_to_right_time_place(Event(EventType.arrival_to_scheduler, task.arrival_time, task))

    warm_up_passed = False
    start_main_simulation_time = -1

    while FEL:  # future event list
        event = FEL.pop()
        print("time:", event.time, ", type:", event.event_type)
        now = event.time
        remove_all_passed_deadlines(now)
        if event.event_type is EventType.arrival_to_scheduler:
            task = task_generator.get_next_task()
            add_to_right_time_place(Event(EventType.arrival_to_scheduler, task.arrival_time, task))
            if system.scheduler.is_idle:
                system.scheduler.set_busy()
                event.task.start_scheduler_service_time = now
                add_to_right_time_place(Event(EventType.departure_of_scheduler,
                                              now + system.scheduler.get_next_service_time(), event.task))
            else:
                system.scheduler.add_to_queue(event.task, now)
        elif event.event_type is EventType.departure_of_scheduler:
            event.task.end_scheduler_service_time = now
            add_to_best_server(event.task, now)
            next_task = get_next_scheduler_task(now)
            if next_task is None:
                system.scheduler.set_idle()
            else:
                next_task.start_scheduler_service_time = now
                add_to_right_time_place(Event(EventType.departure_of_scheduler,
                                              now + system.scheduler.get_next_service_time(), event.task))
        elif event.event_type is EventType.departure_of_core:
            event.task.end_core_service_time = now
            statistical_data.leave_task(event.task)
            if event.server.queue_length() == 0:
                event.core.set_idle()
            else:
                new_task = event.server.pop_of_queue(now)
                new_task.start_core_service_time = now
                add_to_right_time_place(Event(EventType.departure_of_core, now + event.core.get_next_service_time()
                                              , new_task, event.server, event.core))
        if not warm_up_passed and statistical_data.number_of_task_simulated == number_of_warm_up_task:
            statistical_data.reset()
            warm_up_passed = True
            start_main_simulation_time = now
        if warm_up_passed:
            statistical_data.update_queue_length(system, now, start_main_simulation_time)
    return FEL
