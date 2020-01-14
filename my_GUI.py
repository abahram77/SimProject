import PySimpleGUI as sg
import get_data
import get_initial_data_generator
import simulation
import threading
from SystemClass import System
from StatisticalData import StatisticalData
import Report
import AccuracyChecker

sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Welcome to system SIMULATION.:)')],
          [sg.Text('Enter input address  '), sg.InputText()],
          [sg.Text('Enter output address'), sg.InputText()],
          [sg.Button('simulate!'), sg.Button('Exit'), sg.Text('_________________', key='_OUTPUT_')]]

# Create the Window
window = sg.Window('simulation app', layout)
# Event Loop to process "events" and get the "values" of the inputs

done = False


def thread_function(input_address, output_address):
    global done
    global is_simulating
    max_number_of_tasks = 50_000_000  # maximum number of tasks
    number_of_warm_up_task = 5_000  # after this number of tasks we begin to collect the statistics

    input_data = get_data.get(input_address)  # getting data from an input file
    task_generator = get_initial_data_generator.get_task_generator(input_data)  # make a task generator
    system = System(input_data)  # make a main system
    AccuracyChecker.initial(system)

    simulation.simulate(number_of_warm_up_task, max_number_of_tasks, task_generator, system,
                        StatisticalData(input_data))
    Report.print_report(output_address)
    window.close()
    exit()


is_simulating = False
while True:
    event, values = window.read()
    if event in (None, 'Exit'):  # if user closes window or clicks cancel
        break
    elif event is 'simulate!' and not is_simulating:
        is_simulating = True
        window.Element('_OUTPUT_').Update('simulating ...')
        input_address = values[0]
        output_address = values[1]
        x = threading.Thread(target=thread_function, args=(input_address, output_address,))
        x.start()

window.close()
