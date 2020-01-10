from enum import IntEnum


# This class shows types of future event list
class EventType(IntEnum):
    arrival_to_scheduler = 300111
    departure_of_scheduler = 200111
    departure_of_core = 100111


# This class shows the details of an event in system
class Event:
    def __init__(self, event_type, time, task, server=None, core=None):
        self.event_type = event_type
        self.time = time
        self.task = task
        self.core = core
        self.server = server

    def __str__(self):
        return "time: " + str(self.time) + ", type: " + str(self.event_type) + ", task: {" + str(self.task) + "}"
