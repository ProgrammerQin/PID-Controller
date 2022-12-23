import matplotlib.pyplot as plt
from numpy import diff
import scipy.integrate as integrate
import numpy as np

time = np.arange(0, 10, 0.1)


class Input:
  def __init__(self, process_variable):
    self.measured_process_variable = process_variable


class PID_Controller:
  def __init__(self, measured_process_variable, set_point):
    self.measured_process_variable = measured_process_variable
    self.C = 0
    self.set_point = set_point
    self.difference = setpoint - measured_process_variable
    self.P_gain = 1.3
    self.I_gain = 0.2
    self.D_gain = 0.05
    self.dt = 1
    self.P = self.P_gain * self.difference
    self.I = self. I_gain * self.difference * self.dt
    self.D = self. D_gain * self.difference / self.dt


  def control(self):
    controller_output = self.C + self.P + self.I + self.D
    round(controller_output, 2)
    return controller_output


class Output_Process:
  def __init__(self, initial_state, controller_output, disturbance):
    self.process_variable = initial_state + controller_output + disturbance


process_variable_pool = [0]
measured_variable_pool = [0]
controller_output_pool = [0]
disturbance = [0]
plot_process_variable = [0]


setpoint = 15
controller_output = 0

# disturbance = np.sin(time)
disturbance = 0
# disturbance = [12, 34, 32, 27, 30, 12, 123, 12, 43, 85]
process_memory = 0
n = 0

while n < 10:
  input = Input(process_variable_pool[0])
  measured_variable_pool.insert(0, input.measured_process_variable)
  if len(measured_variable_pool) > 4:
      del measured_variable_pool[-1]


  PID_controller = PID_Controller(measured_variable_pool[0], setpoint)
  controller_output_pool.insert(0, PID_controller.control())
  if len(controller_output_pool) > 4:
    del controller_output_pool[-1]


  output = Output_Process(process_memory, controller_output_pool[0], disturbance)
  process_variable_pool.insert(0, output.process_variable)
  process_memory = output.process_variable
  if len(process_variable_pool) > 4:
      del process_variable_pool[-1]
  plot_process_variable.append(output.process_variable)
  n = n + 1
  print("n:", n, "Difference", PID_controller.difference)
  print("n:", n, "Input", input.measured_process_variable, "Controller", PID_controller.control(), "Output", output.process_variable)


print(plot_process_variable)

#   Visualize PID Control Process
# plt.plot(time, disturbance, setpoint, process_variable_pool[0])
plt.axhline(y = setpoint, color = 'k', label = 'Setpoint')
plt.axhline(y = disturbance, color = 'g', label = 'Disturbance')
# plt.plot(test_disturbance, color = 'g', label = 'Disturbance')
plt.plot(plot_process_variable, color = 'pink', label = 'Process')
plt.title('PID Control Process')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True, which='both')
# plt.axhline(y=0, color='k')
plt.legend()
plt.show()

