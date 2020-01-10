import get_data
import get_initial_data_generator
import simulation
from SystemClass import System
from StatisticalData import StatisticalData

max_number_of_tasks = 50_000_000  # maximum number of tasks
number_of_warm_up_task = 5_000  # after this number of tasks we begin to collect the statistics

input_data = get_data.get(input("input file address: "))  # getting data from an input file
task_generator = get_initial_data_generator.get_task_generator(input_data)  # make a task generator
system = System(input_data)  # make a main system

simulation_result = simulation.simulate(number_of_warm_up_task, max_number_of_tasks, task_generator, system,
                                        StatisticalData(input_data))
