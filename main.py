import matplotlib.pyplot as plt
from numpy import diff
import scipy.integrate as integrate
import numpy as np
import threading
import time


time = np.arange(0, 10, 0.1)


# The input Object is reponsible for generating input into the system
class Input(threading.Thread):
  def __init__(self, process_variable):
    threading.Thread.__init__(self)
    self.measured_process_variable = process_variable

  def run(self):
    measured_variable_pool.insert(0, self.measured_process_variable)
    if len(measured_variable_pool) > 5:
      del measured_variable_pool[-1]
    print("INPUT", measured_variable_pool)
    return measured_variable_pool


# Controller Object using input, feedback and setpoint to adjust controller signal
class PID_Controller(threading.Thread):
  def __init__(self, measured_process_variable, set_point):
    threading.Thread.__init__(self)
    self.measured_process_variable = measured_process_variable
    self.C = 0
    self.set_point = set_point
    self.difference = setpoint - measured_process_variable
    self.P_gain = 0.8
    self.I_gain = 0.05
    self.D_gain = 0.02
    self.dt = 1
    self.P = self.P_gain * self.difference
    self.I = self. I_gain * self.difference * self.dt
    self.D = self. D_gain * self.difference / self.dt


  def run(self):
    controller_signal = self.C + self.P + self.I + self.D
    round(controller_signal, 2)
    controller_signal_pool.insert(0, controller_signal)
#    controller_signal_pool.insert(0, 4)
    print("PROCESS", controller_signal_pool)
    if len(controller_signal_pool) > 4:
      del controller_signal_pool[-1]
    return controller_signal_pool


# Output Object provide feedback
class Output_Process(threading.Thread):
  def __init__(self, initial_state, controller_output, disturbance):
    threading.Thread.__init__(self)
    self.initial_state = initial_state
    self.controller_output = controller_output
    self.disturbance = disturbance

  def run(self):
    self.process_variable = self.initial_state + self.controller_output + self.disturbance
    process_variable_pool.insert(0, self.process_variable)
    if len(process_variable_pool) > 5:
      del process_variable_pool[-1]

    print("OUTPUT", process_variable_pool, self.controller_output)
    return process_variable_pool

  def plot(self):
    self.process_variable = self.initial_state + self.controller_output + self.disturbance
    plot_process_variable.append(self.process_variable)
    return plot_process_variable

# Initial Parameters Setup
process_variable_pool = [0]
measured_variable_pool = [0]
controller_signal_pool = [0]
disturbance = [0]
plot_process_variable = [0]

setpoint = 15
controller_signal = 0


# Try Different Disturbance Situations to verify PID Module
# disturbance = np.sin(time)
disturbance = 0
# disturbance = [12, 34, 32, 27, 30, 12, 123, 12, 43, 85]


# Create 3 threads
thread_input = Input(process_variable_pool[0])
thread_process = PID_Controller(measured_variable_pool[0], setpoint)
thread_output = Output_Process(process_variable_pool[0], controller_signal_pool[0], disturbance)


thread_input.start()
thread_process.start()
thread_output.start()


n = 0
while n < 10:
  measured_variable_pool = Input(process_variable_pool[0]).run()
  controller_signal_pool =PID_Controller(measured_variable_pool[0], setpoint).run()
  process_variable_pool = Output_Process(process_variable_pool[0], controller_signal_pool[0], disturbance).run()
  plot_process_variable = Output_Process(process_variable_pool[0], controller_signal_pool[0], disturbance).plot()
  n = n + 0.5


#   Visualize PID Control Process
plt.axhline(y = setpoint, color = 'k', label = 'Setpoint')
plt.axhline(y = disturbance, color = 'g', label = 'Disturbance')
plt.plot(plot_process_variable, color = 'pink', label = 'Process')
plt.title('PID Control Process')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True, which='both')
plt.legend()
plt.show()

