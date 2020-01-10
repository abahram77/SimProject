import get_data
import get_initial_data_generator
import simulation
from SystemClass import System
from StatisticalData import StatisticalData

max_number_of_tasks = 50_000_000
number_of_warm_up_task = 5_000

input_data = get_data.get(input("input file address: "))
task_generator = get_initial_data_generator.get_task_generator(input_data)
system = System(input_data)

simulation_result = simulation.simulate(number_of_warm_up_task, max_number_of_tasks, task_generator, system,
                                        StatisticalData(input_data))
